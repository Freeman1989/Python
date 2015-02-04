#!/usr/bin/python
# -*- coding: utf-8 -*-

import platform

"""
Fingerprints the following Operating Systems:
* Mac OS X
* Ubuntu
* Red Hat/Cat OS
* FreeBSD
* SunOS

"""

class OpSysType(object):
    """Determins OS Type using platform module"""

    def __getattr__(self, attr):
	if attr == "osx":
	    return "osx"
	elif attr == "rhel":
	    return "rethat"
	elif attr == "ubu":
	    return "ubuntu"
	elif attr == "fbsd":
	    return "FreeBSD"
	elif attr == "sun":
	    return "SunOs"
	elif attr == "unknown_linux":
	    return "unknown_linux"
	elif attr == "unknown":
	    return "unknown"
	else:
	    raise AttributeError, attr

def linuxType(self):
    """Uses various methosd to determine Linux Type"""
    
    if platform.dist()[0] == self.rhel:
	return self.rhel
    elif platform.uname()[1] == self.ubu:
	return self.ubu
    else:
	return self.unknown_linux

def queryOS(self):
    if platform.system() == "Darwin":
	return self.osx
    elif platform.system() == "Linux":
	return self.linuxType()
    elif platform.system() == self.sun:
	return self.sun
    elif platform.system() == self.fbsd:
	return self.fbsd

def fingerprint():
    type = OpSysType()
    print type.queryOS()

if __name__ == "__main__":
    fingerprint()
