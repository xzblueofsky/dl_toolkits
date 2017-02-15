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
#FILE(GLOB_RECURSE TEST_SRC_FILES *.cpp *.cc *.c)
FILE(GLOB LIB_SRC_FILES "src/lib/*.cpp")
FILE(GLOB LIB_HEADER_FILES "src/lib/*.h")

add_library(predict_lib ${LIB_SRC_FILES} )  
#target_link_libraries(predict ${LINKER_LIBS})  
FILE(GLOB MAIN_FILES "src/*.cxx")
foreach(test_src ${MAIN_FILES})
    GET_FILENAME_COMPONENT(ONE_TEST_TARGET ${test_src} NAME_WE)
    add_executable(${ONE_TEST_TARGET} ${test_src})  
    # 链接时候的库文件  
    target_link_libraries(${ONE_TEST_TARGET} predict_lib ${LINKER_LIBS})  
endforeach(test_src)

