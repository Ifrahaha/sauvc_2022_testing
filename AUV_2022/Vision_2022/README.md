### Install YoloV7 on jetson
```
sudo apt-get install python3-pip libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev

python3 -m pip install -U pip
python3 -m pip install gdown


gdown "https://drive.google.com/file/d/1TqC6_2cwqiYacjoLhLgrZoap6-sVL2sd/view?usp=sharing" --fuzzy
python3 -m pip install ./torch-1.10.0a0+git36449ea-cp36-cp36m-linux_aarch64.whl


gdown "https://drive.google.com/file/d/1C7y6VSIBkmL2RQnVy8xF9cAnrrpJiJ-K/view?usp=sharing" --fuzzy
python3 -m pip install ./torchvision-0.11.0a0+fa347eb-cp36-cp36m-linux_aarch64.whl

git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
python3 -m pip install -r ./requirements.txt
```
#### Run the inference 
```
python3 ./detect.py --source 0 --device 0 --weights model.pt
```