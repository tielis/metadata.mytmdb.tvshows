# -*- coding: UTF-8 -*-
#
# Copyright (C) 2020, Team Kodi
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# pylint: disable=missing-docstring

"""Misc utils"""

from __future__ import absolute_import, unicode_literals

import xbmc, unicodedata
from os import path
from xbmcaddon import Addon

try:
    from typing import Text, Optional, Any, Dict  # pylint: disable=unused-import
except ImportError:
    pass

ADDON_ID = 'metadata.tvshows.themoviedb.org.python'
ADDON = Addon()


class logger:
    log_message_prefix = '[{} ({})]: '.format(ADDON_ID, ADDON.getAddonInfo('version'))

    @staticmethod
    def log(message, level=xbmc.LOGDEBUG):
        # type: (Text, int) -> None
        if isinstance(message, bytes):
            message = message.decode('utf-8')
        message = logger.log_message_prefix + message
        xbmc.log(message, level)

    @staticmethod
    def info(message):
        # type: (Text) -> None
        logger.log(message, xbmc.LOGINFO)

    @staticmethod
    def error(message):
        # type: (Text) -> None
        logger.log(message, xbmc.LOGERROR)

    @staticmethod
    def debug(message):
        # type: (Text) -> None
        logger.log(message, xbmc.LOGDEBUG)


def safe_get(dct, key, default=None):
    # type: (Dict[Text, Any], Text, Any) -> Any
    """
    Get a key from dict

    Returns the respective value or default if key is missing or the value is None.
    """
    if key in dct and dct[key] is not None:
        return dct[key]
    return default

def trailer_log(key, msg, title):
   
    addonDataDir = xbmc.translatePath(Addon(ADDON_ID).getAddonInfo('profile'))
    Logtxt = path.join(addonDataDir, "Trailer_log.txt")

    lines =  []
    found = False
    title = unicodedata.normalize('NFC',str(title))
    txt_msg = key + msg + title + '\n'
    try:
        makedirs(addonDataDir)
       
    except:   
        pass
    f = open(Logtxt, "a+", encoding='utf-8')
    f.seek(0)
    lines = f.readlines()
    f.close()
    if lines:
        for i, line in enumerate(lines):        
            if title in line:
                found = True
                if not msg in line:
                    lines[i] = txt_msg
                    f = open(Logtxt, "w", encoding='utf-8')
                    f.write("".join(lines))
                    f.close()
                break        
    if not found:
        f = open(Logtxt, "a", encoding='utf-8')
        f.write(txt_msg)
        f.close()  
    return