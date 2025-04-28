# -*- coding: utf-8 -*-
import dabo
from dabo import events
from dabo.localization import _


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
            BackColor="blue",
            BackColorHover="purple",
            ButtonShape="square",
            Name="noborder",
#             Width=200,
#             Height=100,
        )
        btn.bindEvent(events.Hit, self.onButtonHit)

        lbl = dLabel(self, Caption="Caption")
        txt = dTextBox(self, DataSource="self.Parent.noborder", DataField="Caption")

        sz.append(lbl, halign="center")
        sz.append(txt, halign="center")
        sz.appendSpacer(40)
        sz.append(btn, valign="center")
        self.update()
        self.layout()

    def onButtonHit(self, evt):
        obj = evt.EventObject
        self.Form.logit(_("Hit"))

    def on_typing(self,evt):
        print(evt.KeyChar)
        self.update()
        evt.Skip()


category = "Controls.dBorderlessButton"

overview = """
<p>The <b>dBorderlessButton</b> class is intended for designs where you want a button that doesn't
have the typical appearance for buttons, but would rather have it blend in seamlessly with the
background.</p>
"""
