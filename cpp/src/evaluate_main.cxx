//@author: xinzhao
//@email: xinzhao@deepglint.com

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>

#include "lib/classification_caffe.h"

using namespace std;
using namespace cv;

#define DEBUG_PRINT() printf("%s, %s===============%d\n", __FILE__, __FUNCTION__, __LINE__)

typedef pair<string, float> Record;

void ParseTag(const string& fn, vector<Record> &records) {
    ifstream ifs(fn.c_str(), ios::in);
    string line;
    while( getline(ifs, line) ) {
        cout<<line<<endl;
        Record record;
        stringstream ss;
        ss<<line;
        ss>>record.first;
        ss>>record.second; 
        records.push_back(record);
        printf("first = %s, second = %f\n", record.first.c_str(), record.second);
    } 
    ifs.close();
} 

int main(int argc, char* argv[]) {
    if (argc<5) {
        printf("Usage: ./evaluate_main <deploy_file> <model_file> <ground_truth_loc> <result_loc>\n");
        printf("ground truth format:\n");
        printf("<path/to/img> <tag>");
        return -1;
    }

    string deploy_loc = argv[1];
    string model_loc = argv[2];
    string ground_truth_loc = argv[3];
    string result_loc = argv[4];

    vector<Record> records;
    ParseTag(ground_truth_loc, records);

    int batch_size = CaffeClassifier::kBatchSize;
    int batch_num = records.size()/batch_size;
    float avg_time = 0;

    DEBUG_PRINT();
    CaffeClassifier *classifier_ = new CaffeClassifier(argv[1], argv[2]);
    DEBUG_PRINT();
    // batch operation of images
    for ( int batch_count = 0; batch_count<batch_num; batch_count++) {
        vector<Mat> batch_inputs;
        vector<string> batch_img_fns;
        vector< vector<float> > batch_preds;
        for ( int k=batch_count*batch_size; k<(batch_count+1)*batch_size; k++ ) {
            Mat img = imread(records[k].first);
            batch_inputs.push_back(img);
            batch_img_fns.push_back(records[k].first);
        }

        unsigned long long begin = GetCurrentMicroSecond();
        DEBUG_PRINT();
        classifier_->Predict(batch_inputs, batch_preds);
        DEBUG_PRINT();
        unsigned long long end = GetCurrentMicroSecond();
        printf("batch time %lldms\n", end - begin);
        avg_time += end-begin;

        for (int i=0; i<batch_size; i++) {
            cout<<batch_img_fns[i]<<"\t";
            for (vector< vector<float> >::size_type j=0; j<batch_preds[i].size(); j++) {
                cout<<batch_preds[i][j]<<"\t";
            }
            cout<<endl;
        }

    }

    // operation of tail of images 
    vector<Mat> batch_inputs;
    vector<string> batch_img_fns;
    vector< vector<float> > batch_preds;
    for ( vector<string>::size_type i = batch_size*batch_num; i<records.size(); i++) {
        Mat img = imread(records[i].first);
        batch_img_fns.push_back(records[i].first);
        batch_inputs.push_back(img);
    }
    classifier_->Predict(batch_inputs, batch_preds);
    for (vector<string>::size_type i=0; i<batch_img_fns.size(); i++) {
        cout<<batch_img_fns[i]<<"\t";
        for (vector< vector<float> >::size_type j=0; j<batch_preds[i].size(); j++) {
            cout<<batch_preds[i][j]<<"\t";
        }
        cout<<endl;
    }

    delete classifier_;

    return 0;
}
