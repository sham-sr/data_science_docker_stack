FROM jupyter/scipy-notebook:latest

#SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root
RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh && \
    rm -rf "${HOME}/.cache" && \
    code-server --install-extension ms-python.python && \   
    code-server --install-extension ms-azuretools.vscode-docker && \ 
    code-server --install-extension ms-mssql.mssql && \ 
    code-server --install-extension formulahendry.vscode-mysql && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID

RUN mkdir "${HOME}/work/datasets" 
COPY --chown=${NB_UID}:${NB_GID} pip_requirements.txt /tmp/	
COPY --chown=${NB_UID}:${NB_GID} conda_requirements.txt /tmp/

#Install conda pkg
RUN conda config --append channels conda-forge && \
    conda config --set channel_priority true && \
    conda install --yes --file /tmp/conda_requirements.txt && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

#Install pip pkg	
RUN pip install --upgrade --requirement /tmp/pip_requirements.txt && \
    pip cache purge && \ 
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

#Install local jupyter_proxy_extensions
ADD --chown=${NB_UID}:${NB_GID} dev_env ${HOME}/work/dev_env	
ADD --chown=${NB_UID}:${NB_GID} src ${HOME}/work/src
ADD --chown=${NB_UID}:${NB_GID} jupyter_proxy_extensions ${HOME}/work/jupyter_proxy_extensions	
RUN cd ${HOME}/work/jupyter_proxy_extensions/vscode_web && \
    pip install . && \
    cd ${HOME}/work/jupyter_proxy_extensions/flask_web && \
    pip install . && \
    cd ${HOME}/work/jupyter_proxy_extensions/bokeh_web && \
    pip install . && \
    cd ${HOME}/work/jupyter_proxy_extensions/streamlit_web && \
    pip install . && \
    cd ${HOME}/work/jupyter_proxy_extensions/panel_web && \
    pip install . && \
    cd ${HOME}    && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" 

#Install  and build labextension
RUN  \
     jupyter labextension install -y --no-build @jupyterlab/server-proxy && \   
     jupyter lab build --debug && \
     jupyter lab clean && \
     npm cache clean --force && \
     fix-permissions "${CONDA_DIR}" && \
     fix-permissions "/home/${NB_USER}"

#Enable  jupyterlab extension 
RUN jupyter serverextension enable --py jupyterlab --sys-prefix

#Single user mode deploy Bokeh & Streamlit &Flask
#EXPOSE 8501 5000 5006

# Install kite engine
RUN mkdir /tmp/kite && \
    curl -fsSL https://linux.kite.com/dls/linux/current > /tmp/kite/kite-installer.sh && \
    cd /tmp/kite && \
    chmod +x ./kite-installer.sh && \
    ./kite-installer.sh --download && \
    ./kite-installer.sh --install && \
    rm -rf /tmp/kite && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

WORKDIR $HOME