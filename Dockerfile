FROM oraclelinux:8-slim

ARG release=19
ARG update=9
ARG usr=worker
ARG homedir=/home/${usr}

RUN  microdnf install oracle-release-el8 && \
     microdnf install oracle-instantclient${release}.${update}-basic oracle-instantclient${release}.${update}-devel oracle-instantclient${release}.${update}-sqlplus && \
     microdnf clean all

RUN microdnf install -y oracle-epel-release-el8 && \
    microdnf install -y python3 && \
    microdnf install -y python3-virtualenv && \
    microdnf clean all

RUN adduser -s /bin/bash -m worker
ENV PYTHONUNBUFFERED=1
WORKDIR ${homedir}
USER ${usr}
RUN virtualenv myenv && source myenv/bin/activate && \
    pip install cx_oracle

COPY ${PWD}/*.py ${homedir}/
CMD ["/usr/bin/python3']

