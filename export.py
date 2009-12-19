__doc__ = """
Usage: export.py TRAC_URL REPORT_NUMBER [PATH_TO_FILE] [PATH_TO_SVN_CHECKOUT_ROOT] [COMMIT_MESSAGE]

 python export.py https://projects.openplans.org/deliverance 9 > report9.html

 python export.py https://projects.openplans.org/deliverance 9 report9.html

 python export.py https://projects.openplans.org/deliverance 9 report9.html ~/tracdocs/

If PATH_TO_SVN_CHECKOUT_ROOT is set and a commit was made, the program
will print "Committed revision <rev>." like `svn`.

"""

from sven.backend import SvnAccess

from datetime import datetime

def main(url, base, to_file=None, svnroot=None, msg=None):
    out = build(url, base)

    if not to_file:
        print out
        return

    if not svnroot:
        fp = open(to_file, 'w')
        fp.write(out)
        fp.close
        return 

    repo = SvnAccess(svnroot)
    
    if msg is None:
        msg = "Report from %s on %s" % (url, datetime.now())
    rev = repo.write(to_file, out, msg=msg)
    if rev:
        print "Committed revision %s." % rev.number

import urllib2
from BeautifulSoup import BeautifulSoup

_head = """
<head>
  <link rel="stylesheet" href="%s/chrome/common/css/trac.css" type="text/css" />
  <link rel="stylesheet" href="%s/chrome/common/css/report.css" type="text/css" />
</head>
"""

def build(url, base):
    doc = BeautifulSoup(urllib2.urlopen(url).read())
    
    content = doc.findAll('div', attrs={'id':'content'})[0]

    head = _head % (base, base)

    return "<html>%s<body>%s<body></html>" % (head, content)
    
import sys

if __name__ == '__main__':
    try:
        url = "%s/report/%s" % (sys.argv[1], sys.argv[2])
    except:
        print __doc__
        exit(0)

    main(url, sys.argv[1], *sys.argv[3:])
