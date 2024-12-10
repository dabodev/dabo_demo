# -*- coding: utf-8 -*-
import random

import dabo
import dabo.ui
from dabo.application import dApp
from dabo.dLocalize import _
from dabo.ui import dLabel
from dabo.ui import dPanel
from dabo.ui import dSizer
from dabo.ui import dBorderSizer

dGauge = dabo.ui.dGauge

SIZE = (150, 150)


class TestPanel(dPanel):
    def afterInit(self):
        sz = self.Sizer = dSizer("v")
        sz.appendSpacer(25)

        self.gaugeH = dGauge(self, Orientation="h", Size=SIZE)
        self.gaugeV = dGauge(self, Orientation="v", Size=SIZE)
        self.lblH = dLabel(self)
        self.lblV = dLabel(self)
        hg_sz = dSizer("h")
        hg_sz.append(self.gaugeH, valign="middle")
        hg_sz.appendSpacer(10)
        hg_sz.append(self.lblH, valign="middle")
        vg_sz = dSizer("h")
        vg_sz.append(self.gaugeV, valign="middle")
        vg_sz.append(self.lblV, valign="middle")
        sz.append(hg_sz, halign="center")
        sz.appendSpacer(20)
        sz.append(vg_sz, halign="center")

        self.tmr = dabo.ui.callEvery(500, self.updateGauges)
        self.update()
        self.layout()

    @dabo.ui.deadCheck
    def updateGauges(self):
        increase = random.randrange(3, 10)
        gh = self.gaugeH
        val = gh.Value + increase
        if val > gh.Range:
            val -= gh.Range
        gh.Value = val
        self.lblH.Caption = "%s%% complete" % int(gh.Percentage)

        increase = random.randrange(3, 10)
        gv = self.gaugeV
        val = gv.Value + increase
        if val > gv.Range:
            val -= gv.Range
        gv.Value = val
        self.lblV.Caption = "%s%% complete" % int(gv.Percentage)
        self.layout()

    def onDestroy(self, evt):
        self.tmr.stop()


category = "Controls.dGauge"

overview = """
<p>A <b>dGauge</b> is a horizontal or vertical bar which shows a quantity in a graphical
fashion. It is often used to indicate progress through lengthy tasks, such as file copying or
data analysis.</p>

<p>You set the Range property of dGauge to set the 'total' for the task, and then update it
by setting the <b>Value</b> property to the current value; the gauge then updates to
reflect the percentage of the total for that value. You can alternately set the <b>Percentage</b>
property, and the appropriate Value for that Percentage will be set.</p>

<p>Gauges do not raise any events, or respond to user interaction. They are simply a convenient 
way to display the progress of a task or process.</p>
"""

if __name__ == "__main__":
    app = dApp(MainFormClass=None)
    app.setup()
    frm = dabo.ui.dForm()
    pan = TestPanel(frm)
    frm.Sizer.append1x(pan)
    frm.show()
    app.start()
