#!/bin/sh
#
# Kuha2 script to 
# (1) Pull the latest content from the SSHOC EMM registry and update the DDI-XML files in /metadata
# (2) Update document store from DDI-XML documents stored under the /metadata directory
# The Output of kuha_upsert is logged under /var/log/kuha2
#
ME=$(basename $0)
LOGSTAMP=$(date +'%Y%m%d')

# Setup environment
cd /usr/local/kuha2
. kuha_client-env/bin/activate

# Pull content from eregistry and update metadata
NOW=$(date +'%Y-%m-%d %H:%M:%S,%3N')
echo >&1 "$NOW $ME: Pulling EMM registry and updating DDI"
python3 emm-harvester.py -o /metadata 2>>/var/log/kuha2/kuha2-update_$LOGSTAMP.log

# Update Kuha2 metadata (studies only)
NOW=$(date +'%Y-%m-%d %H:%M:%S,%3N')
echo >&1 "$NOW $ME: Updating Kuha2 metadata"
python3 -m kuha_client.kuha_upsert --document-store-url http://localhost:6001/v0 --remove-absent --collection studies /metadata 2>>/var/log/kuha2/kuha2-update_$LOGSTAMP.log 
NOW=$(date +'%Y-%m-%d %H:%M:%S,%3N')
echo >&1 "$NOW $ME: Kuha2 update completed"
