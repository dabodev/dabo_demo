# -*- coding: utf-8 -*-
import dabo
from dabo import events
from dabo.dLocalize import _


from dabo import ui
from dabo.ui import dLabel
from dabo.ui import dPanel
from dabo.ui import dSizer
from dabo.ui import dLed
from dabo.ui import dGridSizer
from dabo.ui import dSpinner
from dabo.ui import dTextBox

dBorderlessButton = ui.dBorderlessButton


class TestPanel(dPanel):
    def afterInit(self):
        sz = self.Sizer = dSizer("v", DefaultBorder=20, DefaultBorderLeft=True)
        sz.appendSpacer(25)

        btn = dBorderlessButton(
            self,
            Caption="I have no border",
            Name="noborder",
            Width=200,
            Height=100,
        )
        btn.bindEvent(events.Hit, self.onButtonHit)
        sz.append(btn, halign="center")
        sz.appendSpacer(40)

        hs = dSizer("h")

        lbl = dLabel(self, Caption="Caption")
        txt = dTextBox(self, RegID="TXT", DataSource="self.Parent.noborder", DataField="Caption")
        hs.append(lbl, halign="right")
        hs.append(txt)

        sz.append(hs, halign="center")
        self.update()
        self.layout()

    def onButtonHit(self, evt):
        obj = evt.EventObject
        self.Form.logit(_("Hit"))


category = "Controls.dBorderlessButton"

overview = """
<p>The <b>dBorderlessButton</b> class is intended for designs where you want a button that doesn't
have the typical appearance for buttons, but would rather have it blend in seamlessly with the
background.</p>
"""
