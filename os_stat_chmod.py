#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os
import stat

filename = 'os_stat_chmod_example.txt'
if os.path.exists(filename):
    os.unlink(filename)
f = open(filename,'wt')
f.write('contents')
f.close()

#Determine what permissions are already set using stat
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)
print existing_permissions
if not os.access(filename,os.X_OK):
    print 'Adding execute permission'
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print 'Removing execute permission'
    new_permissions = existing_permissions ^ stat.S_IXUSR
print new_permissions
os.chmod(filename,new_permissions)
