# MENU

---
## CPP

---
### evaluate
1. Usage:
```
 ./evaluate_main <deploy_file> <model_file> <ground_truth_loc> <result_loc>
```

2. Attention:
```
result file need to be processed furthermore to get final statistical result, such as accurancy precion/recall etc.
```

3. Output:
```
file: <result_loc>
```

4. Format:
```
<image_loc> <prediction> <ground_truth>

Example:
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/1884.jpg  0.204664    0    
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/4038.jpg  -0.0109329  0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/3602.jpg  -0.0476089  0
... ...
```

### predict
1. Usage:
``` 
./predict_main <deploy_file> <model_file> <image_dir_root> <output_loc>
```
2. Warning:
```
<image_dir_root> should end with '/'
```

3. Output
```
file: output_loc
/path/to/img0 0.2332
/path/to/img1 0.5314
/path/to/img2 0.8902
... ...
```
