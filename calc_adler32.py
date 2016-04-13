#!/usr/bin/env python
BLOCKSIZE=32*1024*1024
import sys
from zlib import adler32

for f in sys.argv[1:]:
        val = 1
        if f=='-':
                fp=sys.stdin
        else:   
                fp=open(f)
        while True:
                data = fp.read(BLOCKSIZE)
                if not data:
                        break
                val = adler32(data, val)
        if val < 0:
                val += 2**32
        print hex(val)[2:10].zfill(8).lower()
