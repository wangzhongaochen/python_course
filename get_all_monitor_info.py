#!/usr/bin/python
#-*- coding: UTF-8 -*-
import psutil
import datetime


GIGA_BYTE_FORMAT = "{:.2f}G"


def get_cpu_info():
    # cpu related
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=2)
    return locals()


def get_memory_info():
    # mem related
    virtual_mem = psutil.virtual_memory()
    mem_total = GIGA_BYTE_FORMAT.format(virtual_mem.total / 1024 / 1024 / 1024.0)
    mem_percent = virtual_mem.percent
    mem_free = GIGA_BYTE_FORMAT.format((virtual_mem.free + virtual_mem.buffers +
        virtual_mem.cached) / 1024 / 1024 / 1024.0)
    return dict(mem_total=mem_total, mem_percent=mem_percent, mem_free=mem_free)


def get_disk_info():
    # disk related
    disk_usage = psutil.disk_usage('/')
    disk_total = GIGA_BYTE_FORMAT.format(disk_usage.total / 1024 / 1024 / 1024.0)
    disk_percent = disk_usage.percent
    disk_free = GIGA_BYTE_FORMAT.format(disk_usage.free / 1024 / 1024 / 1024.0)
    return dict(disk_total=disk_total, disk_percent=disk_percent, disk_free=disk_free)


def get_boot_info():
    # boot related
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    boot_time = boot_time.strftime('%D %T')
    return locals()


def get_all_monitor_info():
    data = {}
    data.update(get_boot_info())
    data.update(get_cpu_info())
    data.update(get_memory_info())
    data.update(get_disk_info())
    return data

print get_all_monitor_info()
