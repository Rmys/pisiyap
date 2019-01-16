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

from PyQt5.QtWidgets import QDialog
from .gui.finishedui import FinishDialog as Ui_FinishDialog

class FinishDialog(QDialog):
    def __init__(self,parent = None,modal = 0,fl = 0):
        QDialog.__init__(self, parent)
        self.files = None
        self.ui = Ui_FinishDialog()
        self.ui.setupUi(self)
