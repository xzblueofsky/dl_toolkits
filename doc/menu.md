# MENU

***
## CPP

***
### evaluate
* Usage:
```
 ./evaluate_main <deploy_file> <model_file> <ground_truth_loc> <result_loc>
```

* Attention:
```
result file need to be processed furthermore to get final statistical result, such as accurancy precion/recall etc.
```

* Output:
```
file: <result_loc>
```

* Format:
```
<image_loc> <prediction> <ground_truth>

Example:
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/1884.jpg  0.204664    0    
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/4038.jpg  -0.0109329  0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/3602.jpg  -0.0476089  0
... ...
```

### predict
* Usage:
``` 
./predict_main <deploy_file> <model_file> <image_dir_root> <output_loc>
```
* Warning:
```
<image_dir_root> should end with '/'
```

* Output
```
file: output_loc
/path/to/img0 0.2332
/path/to/img1 0.5314
/path/to/img2 0.8902
... ...
```

***
## PYTHON
***
### parse_tag

* Usage
```
./parse_tag.py <tag_file> <src_img_dir> <tag_name> <result_dir>
```
* Output
```
<result_dir>/<tag_name>_result.txt 
        <img_loc0> <tag_0>
        <img_loc1> <tag_1>
        <img_loc2> <tag_2>
        ... ...
```
* Example:
```
./parse_tag.py realage20161206_20161213_134852.json crop_faces gender .
```


* Output
```
gender/gender_result.txt
/home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/06200177_1_crop.jpg 1
/home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/12630020_0_crop.jpg 0
/home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/12602000_0_crop.jpg 1
```

### generate_img_abspath_list
* Usage
```
./generate_img_abspath_list <src_img_dir>
```

* Output
```
<src_img_dir>/result.txt 
        <img_loc0>
        <img_loc1>
        <img_loc2>
        ... ...
```
* Example:
```
./parse_tag.py /home/zhaoxin/age_sample/

output: /home/zhaoxin/age_sample/gender_result.txt
/home/zhaoxin/age_sample/153.jpg
/home/zhaoxin/age_sample/150.jpg
/home/zhaoxin/age_sample/158.jpg
/home/zhaoxin/age_sample/170.jpg
... ...
```

### wash
* Usage
```
./wash.py <tag_file> <useless flags>
```
* Output
```
    clean.txt
    useless.txt
```
* Example:
```
    ./wash.py gender_result.txt -1
Output:
    *clean.txt
    /home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/06200177_1_crop.jpg 1
    /home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/12630020_0_crop.jpg 0
    /home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/12602000_0_crop.jpg 1
    ... ...

    *useless.txt
    /home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/06500009_0_crop.jpg -1
    /home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/02600216_0_crop.jpg -1
    /home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/10300131_0_crop.jpg -1
    ... ...
```

### acc_pre_recall
* Usage
```
./acc_pre_recall.py <path/to/result>
```
* Warning
```
This is is flexiable to adapt different result file. 
Should be modified for each different task.
```

### compare_model

* Usage:
```
1.cd python/
2.Usage:./compare_models.py <deploy_path> <caffe_model_dir> <ground_truth_loc>
```
* Output
```
files of evaluate file
```

* Example:
```
-lenet_cls_with_tag_iter_10000.txt
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/1884.jpg  1   0   0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/4038.jpg  1   0   0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/3602.jpg  1   0   0


-lenet_cls_with_tag_iter_20000.txt


-lenet_cls_with_tag_iter_30000.txt

... ...
```

### compare_result
* Usage:
```
1.cd python/
2../compare_result.py <results_dir> 
```

* Output
```
Draw precision_recall curve using pyplot.
```
* Warning
```
You need to save the result image manually.
```

### select_badcase
* Usage
```
./selece_badcase.py <result_file_loc> <pos_thresh> <output_dir>
```

* Output
```
Two folders named '<output_dir>/false_pos' and '<output_dir>/false_neg' respectively, containing false_positive images and false_negative images.

Input <result_file> example:
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/blur/5830.jpg   0   1
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/blur/4574.jpg   0.167253    1    
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/blur/4024.jpg   0.461771    1    
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/blur/23424.jpg  0.471229    1    
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/blur/18187.jpg  0.511773    1 
... ...
```
