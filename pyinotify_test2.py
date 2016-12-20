#!/usr/bin/python
#-*- coding: UTF-8 -*-
import pyinotify

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

wdd = wm.add_watch('/home/python/Cource', mask, rec=True)

notifier.loop()
