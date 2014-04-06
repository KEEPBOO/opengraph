#!/usr/bin/env python
# encoding: utf-8
import sys
from keepboo.opengraph import OpenGraph


""" Creates an OpenGraph object and prints data in json and html """
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "url parameter is required"
        exit(1)
    print "url:", sys.argv[1]
    url = sys.argv[1]
    og = OpenGraph(url=url)
    print 'json', og.to_json()
    print 'html', og.to_html()
    exit(0)