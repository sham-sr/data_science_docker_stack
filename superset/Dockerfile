FROM amancevice/superset:latest
#LABEL maintainer="company<jupyter@domain.com>"
USER root
# Copy requirements into stage
ENV SUPERSET_HOME=/var/lib/superset/
WORKDIR ${SUPERSET_HOME}
COPY pip_requirements.txt .	
# Install pip pkg	
RUN pip install --requirement ${SUPERSET_HOME}/pip_requirements.txt
# Make uploads folder
RUN mkdir /uploads && \
 chown -R superset:superset /uploads
USER superset

