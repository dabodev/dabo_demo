# -*- coding: utf-8 -*-
import dabo
import dabo.ui
from dabo.dLocalize import _
from dabo.ui import makeProxyProperty
import random
from dabo.ui import dPanel


class BubblePanel(dPanel):
    def afterInit(self):
        self.Buffered = False

        self._popped = False
        self._selected = False
        self._colors = ["blue", "green", "red", "yellow", "purple"]
        self._color = random.choice(self._colors)
        # Used to detect size changes
        self._sizeCache = (0, 0)

        plat = self.Application.Platform
        self.selectedBackColor = (192, 192, 255) if plat == "Win" else (128, 128, 192)
        self.unselectedBackColor = "white"
        self.autoClearDrawings = plat in ("Win", "Gtk")
        self.row = -1
        self.col = -1
        # Create a dummy circle, and store the reference
        self.circle = self.drawCircle(50, 50, 1)
        self.text = self.drawText("X", 25, 25)
        self.text.DynamicText = self._get_text
        self.DynamicVisible = lambda: not self.Popped
        self.MinimumSize = (50, 50)
        self.onResize(None)
        self.update()

    def _get_text(self):
        return f"{'P' if self.Popped else ' '}{'S' if self.Selected else 'x'}"

    def setRandomColor(self, repaint=False):
        self.Color = random.choice(self._colors)
        if repaint:
            self.Popped = False

    def update(self):
        dabo.ui.callAfter(self._delayedUpdate)

    def _delayedUpdate(self):
        circ = self.circle
#         circ.AutoUpdate = False
        selct = self.Selected
        poppd = self.Popped
        self.BackColor = {
            True: self.selectedBackColor,
            False: self.unselectedBackColor,
        }[selct]
        if poppd:
            circ.Visible = False
        else:
            circ.FillColor = self.Color
            circ.PenWidth = 1
        wd, ht = self.Size
        pos = (round(wd / 2), round(ht / 2))
        rad = round(min(wd, ht) / 2)
        circ.Xpos = round(wd / 2)
        circ.Ypos = round(ht / 2)
        circ.Radius = rad
        circ.AutoUpdate = True
        self._needRedraw = True
        super().update()

    def onResize(self, evt):
        sz = self.Size
        if sz != self._sizeCache:
            self._sizeCache = sz
            self.update()

    def onMouseLeftClick(self, evt):
        self.Parent.bubbleClick(self)

    def _getColor(self):
        return self._color

    def _setColor(self, val):
        if val != self._color:
            if val is None:
                self._color = None
            else:
                self._color = val.lower()

    def _getPopped(self):
        return self._popped

    def _setPopped(self, val):
        if val != self._popped:
            self._popped = self.Visible = val
            self.update()

    def _getSelected(self):
        return self._selected

    def _setSelected(self, val):
        if val != self._selected:
            self._selected = val

    Color = property(_getColor, _setColor, None, _("Color for this bubble  (str or tuple)"))

    Popped = property(_getPopped, _setPopped, None, _("Is the bubble popped?  (bool)"))

    Selected = property(_getSelected, _setSelected, None, _("Selection Status  (bool)"))

    _proxyDict = {}
    Visible = makeProxyProperty(_proxyDict, "Visible", ("circle",))
