Usage: ./parse_tag.py <tag_file> <src_img_dir> <tag_name> <result_dir>
Output:  <result_dir>/<tag_name>_result.txt 
        <img_loc0> <tag_0>
        <img_loc1> <tag_1>
        <img_loc2> <tag_2>
        ... ...

Example:
./parse_tag.py realage20161206_20161213_134852.json crop_faces gender .

output: gender/gender_result.txt
/home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/06200177_1_crop.jpg 1
/home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/12630020_0_crop.jpg 0
/home/zhaoxin/Dataset/ONI/face/from_yangyang/crop_faces/12602000_0_crop.jpg 1
... ...
