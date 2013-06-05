#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Pelican Contributors"
SITENAME = u"Pelican Development Blog"
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

#MENUITEMS = (('documentation', 'http://docs.getpelican.com'), )

# Blogroll
LINKS = (('Pelican', 'http://docs.getpelican.com'),
         ('Python.org', 'http://python.org'),
         ('Jinja2', 'http://jinja.pocoo.org'))

DEFAULT_PAGINATION = 5

PLUGIN_PATH = "plugins"
PLUGINS = ['cacause',]

CACAUSE_DIR = "comments"

THEME = 'themes/simple'
