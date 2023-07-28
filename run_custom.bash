#!/bin/bash

# Use  ./run.bash [version]

IMAGENAME=pepper-hri-pnp

VERSION=latest
if [ ! "$1" == "" ]; then
  VERSION=$1
fi

# change setings here if needed
CAMERA_DEVICE=/dev/video0
PEPPER_TOOLS_HOME=$HOME/eai2/pepper_tools
MODIM_HOME=$HOME/eai2/modim
PLAYGROUND_FOLDER=$HOME/eai2/playground
PEPPER_IP=172.17.0.2


echo "Running image $IMAGENAME:$VERSION ..."

if [ -f $CAMERA_DEVICE ]; then
  echo "Camera device $CAMERA_DEVICE enabled"
  CAMERA_DEVICE_STR="--device=$CAMERA_DEVICE"
fi

if [ -d /run/user/$(id -u)/pulse ]; then
  AUDIO_STR="--device=/dev/snd \
           -v /run/user/$(id -u)/pulse:/run/user/1000/pulse \
           -v $HOME/.config/pulse/cookie:/opt/config/pulse/cookie"
  echo "Audio support enabled"
fi

chmod go+rw ~/.config/pulse/cookie # this file needed by docker user

echo "Pepper IP is $PEPPER_IP"
echo "starting docker container"

docker run -it -d \
    --name pepperhri-pnp \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/.Xauthority:/home/robot/.Xauthority:rw \
    -e DISPLAY=$DISPLAY \
    -p 9000-9200:9000-9200 \
    --privileged \
    $CAMERA_DEVICE_STR \
    $AUDIO_STR \
    -v $PLAYGROUND_FOLDER:/home/robot/playground \
    -v $PEPPER_TOOLS_HOME:/home/robot/src/pepper_tools \
    -v $MODIM_HOME:/home/robot/src/modim \
    -v $HOME/.qibullet:/home/robot/.qibullet \
    -e MODIM_HOME=/home/robot/src/modim \
    -e PNP_HOME=/home/robot/src/PetriNetPlans \
    -e PEPPER_IP=$PEPPER_IP \
    $IMAGENAME:$VERSION


echo "Attaching... ( docker exec -it pepperhri /bin/bash )"


# docker exec -it pepperhri-pnp /bin/bash
docker exec -it pepperhri /bin/bash
