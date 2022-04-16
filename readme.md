# Kuha2 for SSHOC Ethnic and Migrant Minority Registry

The purpose of this Docker image it to provide a public OAI-PMH end point, hosted at <https://oai-pmh.ethmigsurveydatahub.eu/oai?Verb=Identify>, for the EMM Registry. It is an extension of [mtna/kuha2](https://github.com/mtna/kuha2) customized for use with the [Ethnic and Migrant Minority (EMM) Survey Registry](https://ethmigsurveydatahub.eu/emmregistry/), a free publicly available tool allowing users to learn about existing quantitative surveys to EMM (sub)populations. 


Please consult [mtna/kuha2](https://github.com/mtna/kuha2) for general information and guidance. The only difference is that this container automatically pulls the latest version of the DDI-XML version of the the EMM Registry and drop in the /metadata directory for indexing bu Kuha2. The harvesting code is in emm-harvester.py which has been added to the cron scheduled kuha2-update.sh shell script.

This project was developed under the umbrella of the H2020 [Social Sciences and Humanities Open Cloud (SSHOC)](https://sshopencloud.eu/) project.




