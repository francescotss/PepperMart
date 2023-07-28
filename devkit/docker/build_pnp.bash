#!/bin/bash

# Use  ./build.bash [version] [Dockerfile] [--no-cache]

IMAGENAME=pepper-hri-pnp

VERSION=0.7
PNP_VERSION=1.4.7
GRPC_VERSION=1.48.2


if [ ! "$1" == "" ]; then
  VERSION=$1
fi

DOCKERFILE=Dockerfile.pnp
if [ ! "$2" == "" ]; then
  DOCKERFILE=$2
fi

NAOQI=""
if [ -f downloads/naoqi-sdk-2.5.5.5-linux64.tar.gz ]; then
    echo "NAOqi files found"
    NAOQI="OK"
fi


docker build $3 --no-cache -t $IMAGENAME:$VERSION --build-arg NAOQI=$NAOQI -f $DOCKERFILE .

docker tag $IMAGENAME:$VERSION $IMAGENAME:latest


