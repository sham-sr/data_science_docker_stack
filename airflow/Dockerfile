FROM apache/airflow:2.0.1-python3.8

USER root

RUN pip install --upgrade pip
COPY pip_requirements.txt .	
RUN pip install --requirement ./pip_requirements.txt
#RUN pip install azure-storage-blob sshtunnel google-api-python-client oauth2client docker

USER airflow