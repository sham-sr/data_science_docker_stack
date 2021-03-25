ARG JUPYTERHUB_VERSION
FROM jupyterhub/jupyterhub:$JUPYTERHUB_VERSION

COPY jupyterhub_config.py .

RUN pip install --no-cache dockerspawner \
                           jupyterhub-idle-culler \
                           jupyter oauthenticator \
                           pyjwt==1.7.1 \
                           keycloakauthenticator==1.0.0 
                           
