FROM condaforge/miniforge3
    
COPY ./docker/dm-openscad/conda-env.yml .

RUN conda env create -f conda-env.yml

RUN conda init bash

SHELL ["bash", "-lc"]

ENV PATH /opt/conda/envs/dm-openscad/bin:$PATH
RUN echo "conda activate dm-openscad" >> ~/.bashrc

WORKDIR /app/src
ENV ENGINE=solid