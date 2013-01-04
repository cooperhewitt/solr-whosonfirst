#!/usr/bin/env python

import sys
import pysolr
import unicodecsv
import machinetag

if __name__ == '__main__':

    people = sys.argv[1]
    fh = open(people, 'r')

    reader = unicodecsv.UnicodeReader(fh)
    docs = []

    endpoint = 'http://localhost:8984/solr/whosonfirst'
    solr = pysolr.Solr(endpoint)

    for row in reader:

        doc = {
            'uri': 'x-urn:ch:id=%s' % row['id'],
            'collection': 'cooper-hewitt',
            'collection_id': row['id'],
            'name' : row['name']
            }

        concordances = []

        for k, v in row.items():

            if not v:
                continue

            if k == 'tms:id':
                continue

            parts = k.split(':')

            if len(parts) == 2 and parts[1] == 'id':
                mt = "=".join((k, v))
                concordances.append(mt)

        if len(concordances):
            doc['concordances'] = concordances

        docs.append(doc)

        if len(docs) == 1000:
            solr.add(docs)
            docs = []

    if len(docs) == 1000:
        solr.add(docs)
        docs = []
