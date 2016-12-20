#!/usr/bin/python
#-*- coding: UTF-8 -*o
import logging, logging.config
import os
import sys

pkg_root = os.path.realpath(os.path.join(os.path.realpath(__file__),
os.path.pardir, os.path.pardir))
sys.path.append(pkg_root)
#
# Config Logger
#
log_cnf = os.path.join(pkg_root, 'conf', 'logging.cnf')
logging.config.fileConfig(log_cnf, disable_existing_loggers=False)
LOG = logging.getLogger(__name__)


LOG.debug('often makes a very good meal of %s', 'visiting tourists')
