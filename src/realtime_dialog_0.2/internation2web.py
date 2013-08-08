#!/usr/bin/env python
import sys
print unicode(str(sys.stdin.read()), "UTF-8").encode('ascii', 'xmlcharrefreplace')
