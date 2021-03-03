#!/usr/bin/env bash
function run_python_container()  {
    image_name="ultralytics/yolov5"
    xhost +local:root
    XSOCK=/tmp/.X11-unix
    # docker run -it --rm \
    #    -e DISPLAY=$DISPLAY \
    #    --env="DISPLAY" \
    #    --device=/dev/video0 \
    #     -v $(pwd)/:/root/src \
    #     -v =/tmp/.X11-unix:/tmp/.X11-unix \
    #     -v $HOME/.ssh:/root/.ssh \
    #      -v $HOME/.Xauthority:/root/.Xauthority \
    #      -p 8888:8888 \
    #      --name yolov5_official \
    #       --privileged \
    #       $image_name "$@"

    docker run --device=/dev/video0:/dev/video0 \
        -v /tmp/.X11-unix:/tmp/.X11-unix\
        -e DISPLAY=$DISPLAY \
        -p 5000:5000 \
        -p 8888:8888 \
        -it $image_name /bin/bash

}

run_python_container

