#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <sys/time.h>
#include "classification_caffe.h"

using namespace caffe;
using namespace cv;
using namespace std;

const int CaffeClassifier::kBatchSize = 16;

CaffeClassifier::CaffeClassifier(const string& deploy_file,
                const string& model_file) {
	int input_height, input_width;
	useGPU_ = true;
	profile_time_ = true;

	model_file_ =
			model_file;
	trained_file_ = deploy_file;
	input_height = 64;
	input_width = 64;

	// set GPU mode
	if (useGPU_) {
		Caffe::set_mode(Caffe::GPU);
		Caffe::SetDevice(0);
	} else
		Caffe::set_mode(Caffe::CPU);
	// Load the network.
	net_.reset(new Net<float>(trained_file_, TEST));
	net_->CopyTrainedLayersFrom(model_file_);
	CHECK_EQ(net_->num_inputs(), 1) << "Network should have exactly one input.";
	input_layer_ = net_->input_blobs()[0];
	num_channels_ = input_layer_->channels();
	CHECK(num_channels_ == 3) << "Input layer should have 3 channels.";
	input_geometry_ = Size(input_layer_->width(), input_layer_->height());
    printf("input_geometry_.height = %d, input_geometry_.width = %d\n", input_geometry_.height, input_geometry_.width);
	num_channels_ = 3;
	input_layer_->Reshape(kBatchSize, num_channels_, input_geometry_.height,
			input_geometry_.width);
	const vector<shared_ptr<Layer<float> > >& layers = net_->layers();
	const vector<vector<Blob<float>*> >& bottom_vecs = net_->bottom_vecs();
	const vector<vector<Blob<float>*> >& top_vecs = net_->top_vecs();
	for (int i = 0; i < layers.size(); ++i)
		layers[i]->Forward(bottom_vecs[i], top_vecs[i]);

}

void CaffeClassifier::max_min_normalize_img(const Mat &img, float *input_data,
		int &cnt) {
	float max_val = 0;
	float min_val = 255;
	for (int i = 0; i < img.rows; i++) {
		const uchar *data = img.ptr < uchar > (i);
		for (int j = 0; j < img.cols * 3; j++) {
			if (data[j] > max_val)
				max_val = data[j];
			if (data[j] < min_val)
				min_val = data[j];
		}
	}
	max_val = max_val - min_val;
	if (max_val < 1)
		max_val = 1;
	for (int k = 0; k < img.channels(); k++) {
		for (int i = 0; i < img.rows; i++) {
			for (int j = 0; j < img.cols; j++) {
				input_data[cnt] = (float(img.at < uchar > (i, j * 3 + k))
						- min_val) / max_val - 0.5;
				cnt += 1;
			}
		}
	}
}

void CaffeClassifier::mean_normalize_image(const Mat &img, const float mean[3],
		float *input_data, int &cnt) {
    //imshow("img", img);
    //imwrite("pred_area.jpg", img);
    //waitKey(0);
	for (int k = 0; k < img.channels(); k++) {
		for (int i = 0; i < img.rows; i++) {
			for (int j = 0; j < img.cols; j++) {
				input_data[cnt] = (float(img.at < uchar > (i, j * 3 + k))
						- mean[k])/255;
                //printf("img[%d] = %d\n", i*img.cols + j * 3 + k, img.at < uchar > (i, j * 3 + k));
                //printf("img[%d][%d][%d] = %d\n", i, j, k, img.at < uchar > (i, j * 3 + k));
                //printf("img[%d][%d][%d] = %f\n", i, j, k, input_data[cnt]);
                //printf("input_data[%d] = %.3f\n", cnt, input_data[cnt]);
				cnt += 1;
			}
		}
	}
}

void CaffeClassifier::PredictBatch(const vector<Mat> &imgs) {
	float* input_data = input_layer_->mutable_cpu_data();
	int cnt = 0;
	for (int i = 0; i < imgs.size(); i++) {
		Mat sample;
		Mat img = imgs[i].clone();
        //imwrite("pred_org.jpg", img);
        sample = img;

	    resize(sample, sample, Size(input_geometry_.width, input_geometry_.height), 0, 0, INTER_LINEAR);
		float mean[3] = { 128, 128, 128 };
		mean_normalize_image(sample, mean, input_data, cnt);
	}
	// Forward dimension change to all layers.
	net_->Reshape();
	net_->ForwardPrefilled();
	if (useGPU_) {
		cudaDeviceSynchronize();
	}
	// Copy the output layer to a vector
	for (int i = 0; i < net_->num_outputs(); i++) {
		Blob<float>* output_layer = net_->output_blobs()[i];
		outputs_.push_back(output_layer);
	}
}

void CaffeClassifier::Predict(const vector<Mat> &imgs,
		vector<vector<float> > &pred) {
	if (profile_time_)
		time_profiler_.reset();
	PredictBatch(imgs);
	pred.clear();
	int class_num_ = outputs_[0]->channels();
	const float *begin = outputs_[0]->cpu_data();
	const float *end = begin + outputs_[0]->channels() * imgs.size();
	vector<float> output_batch = vector<float>(begin, end);
	for (int j = 0; j < imgs.size(); j++) {
		vector<float> sgl_pred(output_batch.begin() + j * class_num_,
				output_batch.begin() + (j + 1) * class_num_);
		pred.push_back(sgl_pred);
	}

	if (profile_time_) {
		time_profiler_str_ = "DetectionCost";
		time_profiler_.update(time_profiler_str_);
	}
}
