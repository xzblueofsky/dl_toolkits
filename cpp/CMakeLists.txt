cmake_minimum_required(VERSION 2.8)
project(predict)

set(LINKER_LIBS "")
  
# opencv  
find_package(OpenCV REQUIRED)  
include_directories(${OpenCV_INCLUDE_DIRS})  
list(APPEND LINKER_LIBS ${OpenCV_LIBS})  
  
# glog  
# 这是从caffe中获取的  
include("cmake/FindGlog.cmake")  
#find_package(lib_glog REQUIRED)  
include_directories(SYSTEM ${GLOG_INCLUDE_DIRS})  
list(APPEND LINKER_LIBS ${GLOG_LIBRARIES})  
  
# gflags  
# 这是从caffe中获取的  
include("cmake/FindGFlags.cmake")  
#find_package(GFlags REQUIRED)  
include_directories(SYSTEM ${GFLAGS_INCLUDE_DIRS})  
list(APPEND LINKER_LIBS ${GFLAGS_LIBRARIES})  

# cuda
include("cmake/Cuda.cmake")
include_directories(SYSTEM ${CUDA_INCLUDE_DIRS})
list(APPEND LINKER_LIBS ${CUDA_CUDART_LIBRARY} ${CUDA_curand_LIBRARY} ${CUDA_CUBLAS_LIBRARIES})

# caffe
#find_package(Caffe REQUIRED)
set(Caffe_INCLUDE_DIRS "/home/zhaoxin/workspace/caffe/distribute/include")
set(Caffe_LIBRARIES "/home/zhaoxin/workspace/caffe/distribute/lib/libcaffe.so")
include_directories(SYSTEM ${Caffe_INCLUDE_DIRS})
list(APPEND LINKER_LIBS ${Caffe_LIBRARIES})

#boost
#find_package(Boost REQUIRED)
find_package(Boost REQUIRED COMPONENTS system)
include_directories(system Boost_INCLUDE_DIRS)
list(APPEND LINKER_LIBS ${Boost_LIBRARIES})
  
# 加入你自己编译成可执行文件的名称以及对应的代码  
file(GLOB SOURCES "src/*.cpp")
add_executable(predict ${SOURCES})  
# 链接时候的库文件  
target_link_libraries(predict ${LINKER_LIBS})  
