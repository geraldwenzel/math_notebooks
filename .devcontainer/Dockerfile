FROM quay.io/jupyter/datascience-notebook:latest

USER root
# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.
RUN groupadd jovyan \
    && usermod -g jovyan -a -G users jovyan

# Install nodejs and npm
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

# Install `n` version manager globally via `npm`
RUN npm install -g n diff-so-fancy \
    && n stable

# Install python packages
RUN pip install --upgrade pytest nbval pre-commit nbstripout

USER jovyan

# Configure shell
RUN echo 'alias g=git' >> /home/jovyan/.bash_aliases

