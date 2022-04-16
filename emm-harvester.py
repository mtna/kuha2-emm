import argparse
from datetime import date, datetime, timedelta
from dateutil import parser as dateparser
import glob
import hashlib
import logging
import os
import re
import requests
import xml.etree.ElementTree as ET

args = None
namespaces = {'ddi': 'ddi:codebook:2_5', 'dc':'http://purl.org/dc/elements/1.1/', 'dcterms':'http://purl.org/dc/terms/'}

def parse_registry(root):
    global args, namespaces
    stats = {'changed':0, 'unchanged':0, 'new':0, 'saved':0, 'skipped':0, 'total':0}
    ET.register_namespace('','ddi:codebook:2_5')
    ET.register_namespace('dc','http://purl.org/dc/elements/1.1/')
    ET.register_namespace('dcterms','http://purl.org/dc/terms/')
    codeBookIds = [] # this is used to collect ids and check for deleted 
    for codeBook in root:
        stats['total'] += 1
        codeBookId = codeBook.attrib['ID']
        codeBookIds.append(codeBookId)
        saveCodebook = True
        # check country filter
        if args.country:
            nation = codeBook.find('ddi:stdyDscr/ddi:stdyInfo/ddi:sumDscr/ddi:nation', namespaces=namespaces)
            if nation is not None:
                countryCode = nation.get('abbr')
                if args.country != str(countryCode):
                    saveCodebook = False # skip: nation mismatch
            else:
                saveCodebook = False  # skip: no nation found
        # compare with existing file
        ddiFilename = codeBookId+'.xml'
        ddiFilePath = os.path.join(args.out, ddiFilename)
        if os.path.isfile(ddiFilePath):
            tree = ET.parse(ddiFilePath)
            codeBook2 = tree.getroot()
            # compare both DDI
            hash1 = hashlib.md5(ET.tostring(codeBook,encoding='utf-8')).hexdigest()
            hash2 = hashlib.md5(ET.tostring(codeBook2,encoding='utf-8')).hexdigest()
            if hash1 == hash2:
                stats['unchanged'] += 1
                saveCodebook = False # skip: no change
            else:
                stats['changed'] += 1
        else:
            stats['new'] += 1
        # save DDI file
        if saveCodebook:
            logging.info("Updating "+codeBookId);
            if not args.nosave:
                ddiTree = ET.ElementTree(codeBook)
                ddiTree.write(ddiFilePath, encoding='UTF-8')
                stats['saved'] += 1
        else:
            stats['skipped'] += 1
    # check for deleted files (can only do this when no fiolter is set)
    if args.country:
        logging.info("Skipping deleted as filters have been specified")
    else:
        path = os.path.join(args.out, '*.xml')
        for file in glob.glob(path):
            filename = os.path.basename(file)
            fileId = os.path.splitext(filename)[0]
            if fileId not in codeBookIds:
                logging.info("Deleting "+fileId)
                os.remove(file)
        
    logging.info(stats)


def save_ddi(codeBook):
    pass

def main():
    global args
    """Main"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--out", default=".", help="The directory where to write the DDI-XML files")
    parser.add_argument("--country", help="Only process DDI for this country (2-letter ISO code)")
    parser.add_argument("--debug", action='store_true')
    parser.add_argument("-f","--file", help="Use the specified file instead of retrieving from the registry")
    parser.add_argument("--nosave", action='store_true', help="Do not save DDI XML files")
    parser.add_argument("--url", default="https://registry.ethmigsurveydatahub.eu/api/xml-surveys", help="The url to retrieve the EMM DDI collection from")
    args = parser.parse_args()
    print(args)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s EMMHarvester %(levelname)s: %(message)s')
    if args.debug:
        logging.root.setLevel(logging.DEBUG)

    if args.file:
        logging.info("Loading DDI from file "+args.file)
        tree = ET.parse(args.file)
        root = tree.getroot()
    else: 
        logging.info("Retrieving DDI from EMM registry....")
        results = requests.get(args.url, allow_redirects=True)
        root = ET.fromstring(results.content)

    logging.info("Parsing registry...")
    parse_registry(root)

if __name__ == '__main__':
    main()
