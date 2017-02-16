//@author: xinzhao
//@email: xinzhao@deepglint.com

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <sys/types.h>
#include <dirent.h>

#include "lib/classification_caffe.h"

using namespace std;
using namespace cv;

#define DEBUG_PRINT() printf("%s, %s===============%d\n", __FILE__, __FUNCTION__, __LINE__)

void EnumPathFiles(const std::string &path, const std::string &ext,
                   std::vector<std::string> &fns, bool bRecur = false)
{
    DIR *dir = ::opendir(path.c_str());
    for (dirent *ent = ::readdir(dir); ent != NULL; ent = ::readdir(dir))
    {
        std::string fn = std::string(ent->d_name);
        if (bRecur && ent->d_type == DT_DIR && fn != "." && fn != "..")
        {
            std::string strSubPath = path + fn + '/';
            EnumPathFiles(strSubPath, ext, fns, bRecur);
        }
        if (ent->d_type == DT_REG
                && std::equal(ext.rbegin(), ext.rend(), fn.rbegin()))
        {
            fns.push_back(path + fn);
        }
    }
    ::closedir(dir);
}

void write_with_trunc(ofstream &ofs, float value) {
    DEBUG_PRINT();
    if (value < 0) {
       ofs<<0<<"\t";
    } else if (value > 1) {
       ofs<<1<<"\t";
    } else {
       ofs<<value<<"\t";
    }
}

int main(int argc, char* argv[]) {
    if (argc<5) {
        printf("Usage: ./bin <deploy_file> <model_file> <img_root_dir> <result_loc>\n");
        return -1;
    }

    string deploy_loc = argv[1];
    string model_loc = argv[2];
    string imgs_root = argv[3];
    string result_loc = argv[4];
    vector<string> pathes;
    typedef vector<string>::size_type size_type;
    EnumPathFiles(imgs_root, "jpg", pathes, true);
    cout<<pathes.size()<<endl;
    for (size_type i=0; i<pathes.size(); i++) {
        cout<<pathes[i]<<endl;
    }

    ofstream ofs(result_loc.c_str(), ios::out);
    int batch_size = CaffeClassifier::kBatchSize;
    int batch_num = pathes.size()/batch_size;
    float avg_time = 0;


    CaffeClassifier *classifier_ = new CaffeClassifier(argv[1], argv[2]);
    // batch operation of images
    for ( int batch_count = 0; batch_count<batch_num; batch_count++) {
        vector<Mat> batch_inputs;
        vector<string> batch_img_fns;
        vector< vector<float> > batch_preds;
        for ( int k=batch_count*batch_size; k<(batch_count+1)*batch_size; k++ ) {
            Mat img = imread(pathes[k]);
            batch_inputs.push_back(img);
            batch_img_fns.push_back(pathes[k]);
        }

        unsigned long long begin = GetCurrentMicroSecond();
        classifier_->Predict(batch_inputs, batch_preds);
        unsigned long long end = GetCurrentMicroSecond();
        printf("batch time %lldms\n", end - begin);
        avg_time += end-begin;

        for (int i=0; i<batch_size; i++) {
            ofs<<batch_img_fns[i]<<"\t";
            for (vector< vector<float> >::size_type j=0; j<batch_preds[i].size(); j++) {
                write_with_trunc(ofs, batch_preds[i][j]);
                //ofs<<batch_preds[i][j]<<"\t";
            }
            ofs<<endl;
        }

    }

    // operation of tail of images 
    vector<Mat> batch_inputs;
    vector<string> batch_img_fns;
    vector< vector<float> > batch_preds;
    for ( vector<string>::size_type i = batch_size*batch_num; i<pathes.size(); i++) {
        Mat img = imread(pathes[i]);
        batch_img_fns.push_back(pathes[i]);
        batch_inputs.push_back(img);
    }
    classifier_->Predict(batch_inputs, batch_preds);
    for (vector<string>::size_type i=0; i<batch_img_fns.size(); i++) {
        ofs<<batch_img_fns[i]<<"\t";
        for (vector< vector<float> >::size_type j=0; j<batch_preds[i].size(); j++) {
            write_with_trunc(ofs, batch_preds[i][j]);
            //ofs<<batch_preds[i][j]<<"\t";
        }
        ofs<<endl;
    }

    ofs.close();

    delete classifier_;

    return 0;
}
