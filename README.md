环境为WSL2-Ubuntu22.04

## 从源码安装
sudo apt install g++ cmake libssl-dev

git clone -b master https://github.com/pocoproject/poco.git

cd poco

mkdir cmake-build
cd cmake-build
cmake ..
make -j4
sudo make install


g++ test.cpp -o test -lPocoNet

## 包管理器安装
sudo apt update

sudo apt install libpoco-dev

## 编写测试程序
   ```cpp
   #include <iostream>
   #include <Poco/Net/HTTPRequest.h>
   
   int main()
   {
       Poco::Net::HTTPRequest request;
       std::cout << "Poco library installation successful!" << std::endl;
       return 0;
   }
   ```
## 使用命令行编译链接，运行
g++ test.cpp -o test -lPocoNet

./test
   

## 使用cmake编译链接
若您没有安装cmake:
sudo apt install cmake

在刚才编写的文件的同级文件夹下，创建一个名为 `CMakeLists.txt` 的文件，其内容如下：
```cmake
cmake_minimum_required(VERSION 3.0)
project(PocoExample)
find_package(Poco REQUIRED COMPONENTS Foundation Net)
add_executable(example main.cpp)
target_link_libraries(example Poco::Foundation Poco::Net)
```

创建`build`文件夹，进入`build`文件夹，生成 Makefile，编译，运行
mkdir build
cd build
cmake ..
make
./example
