# This route advertising daemon was used for Defcon 19 OpenCTF.
# Don't remember if it works with multiple interfaces.

# The reason this exists is because the minimum network allocation
# according to spec is /64 and every other radvd i tried adhered to 
# the spec. Unfortunately we were worried about our switches not
# being able to handle that many addresses and since we were running
# this network in front of a bunch of hackers, I decided fuck the
# spec, we're gonna do this our way, we aint on the interwebs.

import time
from scapy.all import IPv6,ICMPv6ND_RA,ICMPv6NDOptSrcLLAddr,ICMPv6NDOptMTU,ICMPv6NDOptPrefixInfo,send

a = IPv6()
a.dst = "ff02::1"

b = ICMPv6ND_RA()
b.M = 1
b.O = 1

c = ICMPv6NDOptSrcLLAddr()
c.lladdr = "aa:bb:cc:dd:ee:ff"

d = ICMPv6NDOptMTU()

e = ICMPv6NDOptPrefixInfo()
e.prefixlen = 118
e.prefix = "0:c:7:f::"

while True:
	send(a/b/c/d/e)
	time.sleep(1)
