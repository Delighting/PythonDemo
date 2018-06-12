#!/usr/bin/env python3

import mypackage

from mypackage2 import module21,module22

print(mypackage.__name__,mypackage.__file__,mypackage.__package__)

module21.m1()

module22.m1()