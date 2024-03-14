FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

RUN apt-get update && apt-get install -y unzip zip

RUN pip3 install numpy scipy torchmetrics lightning lightning-bolts pandas scikit-learn