# Process to Train and Evaluate a Deeplearning Model

***
## 1.Collect and Tag Data
Cooperate with data tagging team.

## 2.Deal with data to make prepare for training
### 2.1Wash tagged data
Use python/wash.py to remove invalid tag data

### 2.1Parse tagged data 
Use python/parse_tag.py to parse tag results, get file like:

file: output_loc
/path/to/img0 0.2332
/path/to/img1 0.5314
/path/to/img2 0.8902
... ...

### 2.2Split train and test
Get files:
train.txt
test.txt

## 2.Train model
Using train.txt to train caffe models

## 3.Test model
### 3.1Generate result txt file
Use python/compare_model.py to generate result txt file.

### 3.2Visualize result txt file
Use python/compare_result.py to visualize result txt file.

### 3.3Watch badcases
Use python/select_badcase.py to select and save badcases, watch these bad cases to find clues for improving model.

***
## Other Tools
### * Generate file path lists
Use python/generate_img_abspath_list.py. Find and generate all image abosolute pathes recursively under a specific folder. The result is a text file located in input root folder.

### * Make predictions
Use cpp/build/predict to make predictions. Set deploy and model and image_folder, abosolute image path. Corresponding prediction will be saved in a text file.
run_prediction.sh could be used to make parameter modification easier.

### * Make evaluation
Use cpp/build/evaluate to make evaluations. Set deploy and model and image_folder, groundtruth path. Corresponding prediction and corresponding groundtruth will be saved in a text file.
run_evaluate.sh could be used to make parameter modification easier.
