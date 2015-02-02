#!/usr/bin/python
# -*- coding: utf-8 -*-

import platform

profile = [
	platform.architecture(),
	platform.dist(),
	platform.libc_ver(),
	platform.mac_ver(),
	platform.machine(),
	platform.node(),
	platform.processor(),
	platform.python_compiler(),
	platform.python_version(),
	platform.system(),
	platform.uname(),
	platform.version(),
	]

for item in profile:
    print item
