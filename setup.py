# -*- coding: utf-8 -*-
#
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the docs/COPYING file.
#

from setuptools import setup, find_packages
from os import listdir, system
import glob


langs = []
for l in listdir('languages'):
    if l.endswith('ts'):
        #Temporary bindir to avoid qt4 conflicts
        #system('lrelease-qt5 languages/%s' % l)
        system('lrelease languages/%s' % l)
        langs.append(('languages/%s' % l).replace('.ts', '.qm'))

datas = [('/usr/share/kservices5/ServiceMenus', glob.glob('data/servicemenu/*.desktop')),
         ('/usr/share/applications', ['data/PiSiYaP.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['data/icons/pisiyap.svg']),
         ('/usr/share/pisiyap/languages', langs)]

setup(name = "pisiyap",
      version = "0.7",
      license="GPL v3",
      description = "PiSi Source Files Creator.",
      author = "Metehan Özbek",
      author_email = "mthnzbk@gmail.com",
      url = "https://www.github.com/mthnzbk/pisiyap",
      packages = find_packages(),
      data_files = datas,
      scripts = ['pisiyap']
      )
