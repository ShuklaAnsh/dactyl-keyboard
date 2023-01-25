FROM condaforge/miniforge3

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*
    
COPY ./docker/dm-cadquery/conda-env.yml .

RUN conda env create -f conda-env.yml

RUN conda init bash

SHELL ["bash", "-lc"]

ENV PATH /opt/conda/envs/dm-cadquery/bin:$PATH
RUN echo "conda activate dm-cadquery" >> ~/.bashrc

WORKDIR /app/src
ENV ENGINE=cadquery
