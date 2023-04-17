#!/bin/bash

# install dependencies
brew install ant
brew install openexr
brew install opencv

# download opencv source code
wget https://github.com/opencv/opencv/archive/4.5.0.zip -O opencv-4.5.0.zip
unzip opencv-4.5.0.zip

# build and install opencv with java bindings
cd opencv-4.5.0
mkdir build
cd build
cmake -DBUILD_SHARED_LIBS=OFF -DBUILD_opencv_java=ON -DOPENCV_GENERATE_PKGCONFIG=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local ..
make -j4
sudo make install

# set opencv java library path
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

# clean up
cd ../..
rm -rf opencv-4.5.0
rm opencv-4.5.0.zip
