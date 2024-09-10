FROM quay.io/jupyter/datascience-notebook:latest

USER root
# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.
RUN groupadd jovyan \
    && usermod -g jovyan -a -G users jovyan
RUN pip install --upgrade pytest
RUN pip install --upgrade nbval
RUN pip install --upgrade pre-commit
RUN pip install --upgrade nbstripout
RUN echo "alias g='git'" >> /home/jovyan/.bashrc
USER jovyan
