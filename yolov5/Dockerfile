FROM python:3



RUN mkdir -p /root/src/
WORKDIR /root/src
COPY . .

RUN git clone https://github.com/ultralytics/yolov5
RUN cd yolov5 && pip install -U -r yolov5/requirements.txt

CMD ["bash"]
