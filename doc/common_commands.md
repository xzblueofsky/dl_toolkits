# deal with result file to wanted format
awk '{printf("%s\t%s\t%s\n",$1, $3, $4)}' result > tmp
Example:
>>>src
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/1884.jpg  1   0   0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/4038.jpg  1   0   0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/3602.jpg  1   0   0
... ...
>>>dest
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/1884.jpg  0   0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/4038.jpg  0   0
/home/zhaoxin/workspace/dataset/face/blur/tag/for_operation/clear/3602.jpg  0   0
... ...
