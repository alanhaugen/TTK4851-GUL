
FROM python:3

RUN git clone https://github.com/ultralytics/yolov5
RUN pip install -U -r yolov5/requirements.txt

RUN mkdir -p /root/src/
WORKDIR /root/src
COPY . .

CMD ["bash"]
