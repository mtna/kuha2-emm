# SSHOC EMM Kuha2
#
# Run:
# docker container run -it --rm --name kuha2 -p 80:80 -p 27017:27017 -p 6001:6001 -p 6002:6002 -p 6003:6003 mtna/kuha2-emm
#
# Run with persistence
# docker container run -it --rm --name kuha2 -p 80:80 -p 27017:27017 -p 6001:6001 -p 6002:6002 -p 6003:6003 -v $(pwd)/volumes/metadata:/metadata -v $(pwd)/volumes/db:/data/db -v $(pwd)/volumes/log/kuha2:/var/log/kuha2 -v $(pwd)/volumes/log/nginx:/var/log/nginx mtna/kuha2-emm
#
# Shell:
# docker container exec -it kuha2 bash
#
#
FROM mtna/kuha2:latest

LABEL maintainer="mtna@mtna.us"

#
# ADD SSHOC EMM Harvester
#
RUN cd /usr/local/kuha2 \
    && . kuha_client-env/bin/activate \
    && pip install datetime python-dateutil requests 
COPY emm-harvester.py /usr/local/kuha2/

#
# REPLACE kuha2-update script
#
COPY kuha2-update.sh /usr/local/kuha2
RUN chmod 0744 /usr/local/kuha2/kuha2-update.sh

#
# CRON JOBS
#
COPY kuha2-cron /etc/cron.d
RUN chmod 0644 /etc/cron.d/kuha2-cron \
    && crontab /etc/cron.d/kuha2-cron
