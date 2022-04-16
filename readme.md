# Kuha2 for SSHOC Ethnic and Migrant Minority Registry

The purpose of this Docker image it to provide a public OAI-PMH end point, hosted at <https://oai-pmh.ethmigsurveydatahub.eu/oai?Verb=Identify>, for the EMM Registry. It is an extension of [mtna/kuha2](https://github.com/mtna/kuha2) customized for use with the [Ethnic and Migrant Minority (EMM) Survey Registry](https://ethmigsurveydatahub.eu/emmregistry/), a free publicly available tool allowing users to learn about existing quantitative surveys to EMM (sub)populations. 

Please consult [mtna/kuha2](https://github.com/mtna/kuha2) for general information and guidance. The only difference is that this container automatically pulls the latest version of the DDI-XML version of the the EMM Registry and drop in the /metadata directory for indexing bu Kuha2. The harvesting code is in emm-harvester.py which has been added to the cron scheduled kuha2-update.sh shell script.

This project was developed under the umbrella of the H2020 [Social Sciences and Humanities Open Cloud (SSHOC)](https://sshopencloud.eu/) project.

## MIT License

Copyright © `2022` `Metadata Technology North America Inc.`

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.


## Contact
For feedback, questions, or suggestions contact <pascal.heus@mtna.us>



