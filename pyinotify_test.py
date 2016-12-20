#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import os
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY, IN_ATTRIB

class MyEventHandler(ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Create file: {0}".format(os.path.join(event.path, event.name)))

    def process_IN_DELETE(self, event):
        print("Delete file: {0}".format(os.path.join(event.path, event.name)))

    def process_IN_MODIFY(self, event):
        print("Modify file: {0}".format(os.path.join(event.path, event.name)))

    def process_IN_ATTRIB(self, event):
        print("Modify file {0}'s attribute.".format(os.path.join(event.path, event.name)))


class FileSystemMonitor(object):
    def __init__(self, path):
        self.path = path

    def run(self):
        wm = WatchManager()
        mask = IN_DELETE | IN_CREATE | IN_MODIFY | IN_ATTRIB
        notifier = Notifier(wm, MyEventHandler())
        wm.add_watch(self.path, mask, auto_add=True, rec=True)
        print("Now starting monitor {0}".format(self.path))
        while True:
            try:
                notifier.process_events()
                if notifier.check_events():
                    notifier.read_events()
            except KeyboardInterrupt:
                notifier.stop()
                break

if __name__ == '__main__':
    monitor = FileSystemMonitor('/home/python/Cource')
    monitor.run()
