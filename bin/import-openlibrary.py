#!/usr/bin/env python

import sys
import pysolr
import csv
import bz2

if __name__ == '__main__':

    people = sys.argv[1]
    fh = bz2.BZ2File(people, 'r')

    reader = csv.reader(fh)
    docs = []

    endpoint = 'http://localhost:8984/solr/whosonfirst'
    solr = pysolr.Solr(endpoint)

    for row in reader:

        doc = {
            'uri': 'x-urn:ol:id=%s' % row[0],
            'collection': 'openlibrary',
            'collection_id': row[0],
            'name' : row[1]
            }

        docs.append(doc)

        if len(docs) == 10000:
            solr.add(docs)
            docs = []

    if len(docs) == 10000:
        solr.add(docs)
        docs = []
