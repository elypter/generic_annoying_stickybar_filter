#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from StringIO import StringIO
from zipfile import ZipFile
from urllib2 import urlopen
from urlparse import urlparse
from collections import defaultdict
import operator

response = urlopen('https://web.archive.org/web/20111219160932id_/https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
tlds = response.readlines()[1:]

response = urlopen('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
archive = ZipFile(StringIO(response.read()))
top1m = archive.open('top-1m.csv')
domains = top1m.readlines()
rankings = defaultdict(int)

for domain in domains:
    tld = domain.strip().split('.')[-1]
    rankings[tld]+=1

sorted_tlds = sorted(rankings.items(), key=operator.itemgetter(1), reverse=True)


with open("prefixes.txt") as f:
    prefixes = f.readlines()

with open("suffixes.txt") as f:
    suffixes = f.readlines()

filters=[]

for i in range(20):
    tld=""+sorted_tlds[i][0]
    print(tld)
    for suffix in suffixes:
        suffix=suffix.strip()
        for prefix in prefixes:
             prefix=prefix.strip()
             filters+=[tld+"##."+prefix+suffix+":style(position: relative !important; top: 0 !important;)"]
             filters+=[tld+"##."+prefix+"-"+suffix+":style(position: relative !important; top: 0 !important;)"]
             filters+=[tld+"###"+prefix+suffix+":style(position: relative !important; top: 0 !important;)",]
             filters+=[tld+"###"+prefix+"-"+suffix+":style(position: relative !important; top: 0 !important;)"]
#for tld in tlds:
#    tld=tld.strip()
#    filters+=[tld+"##:xpath(.//*[matches(@class,'(sticky|header|head|navigation|nav|fixed|fix|ribbon|logo|app|footer|locked|main|top|pinned|banner|social|share|sharing|shares|like|follow|login|teaser|tease|related|recommend|recommended|action|scrolled|stuck|smart|mobile|index|icon|pagenav|row|static|tray|global|rail|tab|float|floating|scrolled|menu|bar|bottom|panel|mast|master)[_-]?(menu|bar|header|head|main|top|banner|sticky|navigation|nav)?')]:style(position:fixed))"]



outfile = open('generic_header_list.txt', 'w')

for line in filters:
  outfile.write("%s\n" % line)
outfile.close()
