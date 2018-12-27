#!/usr/bin/env python

# assume existing list 'a'

tmp = a[0]
a[0] = a[len(a) - 1]
a[len(a) - 1] = tmp