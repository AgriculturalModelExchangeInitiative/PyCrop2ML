FROM continuumio/conda-ci-linux-64-python3.7:latest

ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH="${CONDA_DIR}/bin:${PATH}" \
    HOME="/home/${USER}"

USER root

RUN apt-get update

USER ${USER}

#RUN conda install -y jupyterlab=2.3.2 -c conda-forge
RUN conda install -y graphviz pydot -c conda-forge
# OpenAlea INSTALLATION
RUN conda install -y -c openalea3 -c conda-forge openalea.core



# Pycrop2ml_ui installation
WORKDIR ${HOME}
COPY . PyCrop2ML
WORKDIR PyCrop2ML
RUN pip install -r requirements.txt
RUN pip install -e .
WORKDIR ${HOME}
RUN git clone https://github.com/AgriculturalModelExchangeInitiative/SoilTemperatureModels.git

WORKDIR SoilTemperatureModels/Platforms



# Set root directory to /home/joyvan/work
#WORKDIR ${HOME}/work/
#CMD ["/usr/local/bin/start.sh", "jupyter", "lab", "AppLauncher.ipynb"]
