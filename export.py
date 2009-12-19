__doc__ = """
Usage: export.py [TRAC_URL] [REPORT_NUMBER]

e.g. python export.py https://projects.openplans.org/deliverance 9 > report9.html
"""

import urllib2
from BeautifulSoup import BeautifulSoup

_head = """
<head>
  <link rel="stylesheet" href="%s/chrome/common/css/trac.css" type="text/css" />
  <link rel="stylesheet" href="%s/chrome/common/css/report.css" type="text/css" />
</head>
"""

def main(url, base):
    doc = BeautifulSoup(urllib2.urlopen(url).read())
    
    content = doc.findAll('div', attrs={'id':'content'})[0]

    head = _head % (base, base)

    print "<html>", head, "<body>", content, "<body></html>"

import sys
if __name__ == '__main__':
    url = "%s/report/%s" % (sys.argv[1], sys.argv[2])
    main(url, sys.argv[1])
