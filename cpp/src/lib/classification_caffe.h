#ifndef CLASSIFICATION_CAFFE_
#define CLASSIFICATION_CAFFE_
#include <caffe/caffe.hpp>
#include <opencv2/core/core.hpp>
#include <memory>
#include <string>
#include <vector>
#include <cassert>
#include "timing_profiler.h"

class CaffeClassifier {
public:
	CaffeClassifier(const std::string& deploy_file,
                    const std::string& model_file);
	void Predict(const std::vector<cv::Mat> &imgs,
			std::vector<std::vector<float> > &pred);
	static const int kBatchSize;
	char *get_detection_time_cost() {
		if (profile_time_)
			return time_profiler_.getSmoothedTimeProfileString();
		else
			return "TimeProfiling is not opened!";
	}
private:
	caffe::shared_ptr<caffe::Net<float> > net_;
	caffe::Blob<float>* input_layer_;
	std::vector<caffe::Blob<float>*> outputs_;
	cv::Size input_geometry_;
	std::string model_file_;
	std::string trained_file_;
	int num_channels_;
	int crop_w_;
	int crop_h_;
	cv::Mat mean_;
	bool useGPU_;
	bool profile_time_;
	std::string time_profiler_str_;
	timing_profiler time_profiler_;
	void PredictBatch(const std::vector<cv::Mat> &imgs);
	void max_min_normalize_img(const cv::Mat &img, float *input_data, int &cnt);
	void mean_normalize_image(const cv::Mat &img, const float mean[3],
			float *input_data, int &cnt);
};
#endif
