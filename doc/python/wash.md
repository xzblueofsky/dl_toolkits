Usage:./wash.py <tag_file> <useless flags>
Output:
    clean.txt
    useless.txt

Example:
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
