#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rcvu rcvu'
SITENAME = 'Big Blogging'
SITEURL = 'rcvurcvu.icu'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "pelican-themes/lightweight"


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['photos']

### PHOTOS PLUGIN SETTINGS
PHOTO_LIBRARY = "content/images"
PHOTO_GALLERY = (1920, 1080, 99)
PHOTO_ARTICLE = (760, 506, 99)
PHOTO_THUMB = (192, 144, 60)
PHOTO_RESIZE_JOBS = 5
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_AUTOROTATE = True
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
