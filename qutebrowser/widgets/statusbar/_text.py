# Copyright 2014 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Text displayed in the statusbar."""

from qutebrowser.widgets.statusbar.textbase import TextBase


class Text(TextBase):

    """Text displayed in the statusbar.

    Attributes:
        _normaltext: The "permanent" text. Never automatically cleared.
                     Accessed via normaltext property.
        _temptext: The temporary text to display.
                   Accessed via temptext property.

        The temptext is shown from StatusBar when a temporary text or error is
        available. If not, the permanent text is shown.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._normaltext = ''
        self._temptext = ''

    @property
    def normaltext(self):
        """Getter for normaltext so we can define a setter."""
        return self._normaltext

    @normaltext.setter
    def normaltext(self, val):
        """Setter for normaltext to update text display after setting."""
        self._normaltext = val
        self._update_text()

    @property
    def temptext(self):
        """Getter for temptext so we can define a setter."""
        return self._temptext

    @temptext.setter
    def temptext(self, val):
        """Setter for temptext to update text display after setting."""
        self._temptext = val
        self._update_text()

    def _update_text(self):
        """Update QLabel text when needed."""
        for text in [self.temptext, self.normaltext]:
            if text:
                self.setText(text)
                break
        else:
            self.setText('')
