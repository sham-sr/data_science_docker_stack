FROM jboss/keycloak:latest

COPY --chown=jboss ./config.batch /tmp/config.batch

RUN cd $JBOSS_HOME \
  && ./bin/jboss-cli.sh --file=/tmp/config.batch \
  && rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history \
  && rm -rf $JBOSS_HOME/standalone/data \
  && rm -rf $JBOSS_HOME/standalone/tmp \
  && rm -rf /tmp/config.batch