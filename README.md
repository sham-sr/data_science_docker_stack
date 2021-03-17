# Data science docker stack  
## What is it  
This is a project for the deployment of popular services for data analysis in the docker environment.  
**Visualization**  
[metabase](https://github.com/metabase/metabase)  
[superset](https://github.com/apache/superset)  
**Development**  
[JupyterLab](https://github.com/jupyterlab/jupyterlab)  
[JupyterHUB](https://github.com/jupyterhub/jupyterhub)  
**Orchestration**  
[Airflow](https://github.com/apache/airflow)  
**Authorization**  
[keycloak](https://github.com/keycloak/keycloak-containers)  
[openldap](https://github.com/osixia/docker-openldap)  
As a backend DB MySQL8  
## How to deploy  
The docker-compose parameters are set in .env files. Before you build or run the docker-compose file, rename the .envexample to .env and edit it to match your environment.  
1. Create a "webproxy" network  
`docker network create webproxy`  
2. Run traefik   
You must have domains defined for all services with the specified" A records " of white IP addresses.
Go to the traefik_proxy folder, Change permissions of acme.json file and run traefik.  
Rename to *.toml and edit traefik.toml.example traefik_dynamic.toml.example
`chmod 600 acme.json
docker-compose up -d`
3. Go to the mysql_prod folder  
In the mysql_prod/db/sql folder, there is an init.sql script that creates databases and users for services. It contains passwords that are not secure so you can not use the script and create empty databases and add users manually. This information will need to be specified in the files .env of specific services.
In the mysql_prod/db/config-file folder,there is an my.cnf file, edit it to suit your needs.   
`docker-compose up –d`
4. Run portainer  
Go to the portainer folder  
`docker-compose up –d`
5. Run keycloak  
Go to the keycloak folder  
`docker-compose build
docker-compose up –d`
wait until the database is initialized (on HHD it can take a long time up to 12 minutes, follow the logs)  
6. Run JupyterLab and create image for JupyterHub users  
Go to the jupyterlab_img_gen folder, to the dokerfile folder for different target notebooks that can be run in single-player mode and after creating images use images in jupyterhub.  
***scipy*** - based on [scipy-notebook](https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook), with add some conda, pip lib conda_requirements.txt, pip_requirements.txt, JupyterLab extensions:  
* lckr-jupyterlab-variableinspector  
* ipyleaflet  
* jupyterlab-git  
* jupyterlab_widgets  
* jupyter-server-proxy  
* jupyterlab_execute_time  
* jupyterlab-kite  
* jupyterlab-system-monitor  
add [code-server](https://github.com/cdr/code-server)  
add self-written **jupyter_proxy_extensions** to be able to run bokeh, panel, flask, streamlit behind a proxy server    
***dotnet*** - based on [dotnet_interactive](https://github.com/dotnet/interactive)  
add code-server, and same vscode extensions  
***osmnx*** - [OSMnx](https://github.com/gboeing/osmnx)  
to build an image select folder and кгт build  
`docker-compose.yml build`
if you want to run notebook in single mode, generate the token with the generate_token script.py and add it to .env  
`docker-compose.yml up -d`
7. Run JupyterHub  
JupyterHub use [KeyCloakAuthenticator](https://github.com/swan-cern/jupyterhub-extensions/tree/master/KeyCloakAuthenticator) 
Edit, .env and jupyterhub_config.py. Run in jupyterhub folder  
`docker-compose build
docker-compose up –d`

