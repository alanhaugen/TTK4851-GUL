#!/usr/bin/env bash
function run_python_container()  {
  image_name="yolov5:latest"
  xhost +local:root
  XSOCK=/tmp/.X11-unix
  docker run -it --rm \
     -e DISPLAY=$DISPLAY \
      -v $(pwd)/:/root/src \
      -v $XSOCK:$XSOCK \
      -v $HOME/.ssh:/root/.ssh \
       -v $HOME/.Xauthority:/root/.Xauthority \
       --name acados \
        --privileged \
        $image_name "$@"
}

run_python_container

