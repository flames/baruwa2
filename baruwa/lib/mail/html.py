# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# Baruwa - Web 2.0 MailScanner front-end.
# Copyright (C) 2010-2015  Andrew Colin Kissa <andrew@topdog.za.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""HTML processing functions"""

from lxml.html import defs
from lxml.html.clean import Cleaner

from baruwa.lib.mail import local_fromstring


class CustomCleaner(Cleaner):
    """Over ride Cleaner to remove class attribute"""
    def __call__(self, doc):
        Cleaner.__call__(self, doc)
        safe_attrs = set(defs.safe_attrs)
        safe_attrs.remove('class')
        for elm in doc.iter():
            attrib = elm.attrib
            for aname in attrib.keys():
                if aname not in safe_attrs:
                    del attrib[aname]


def get_style(msg):
    "Get the styles in a message"
    styles = []
    if msg:
        html = local_fromstring(msg)
        for style in html.xpath('//style'):
            styles.append(style.text or u'')
    return u'\n'.join(styles)
