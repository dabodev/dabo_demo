# -*- coding: utf-8 -*-
import dabo
import dabo.ui
from dabo import events
from dabo.localization import _


from dabo.ui import dLabel
from dabo.ui import dPanel
from dabo.ui import dSizer
from dabo.ui import dCheckBox
from dabo.ui import dSpinner

dDropdownList = dabo.ui.dDropdownList


class TestPanel(dPanel):
    def afterInit(self):
        sz = self.Sizer = dSizer("v")
        sz.appendSpacer(25)

        self.dropdown_control = ddc = dDropdownList(
            self,
            Choices=[
                "The Phantom Menace",
                "Attack of the Clones",
                "Revenge of the Sith",
                "A New Hope",
                "The Empire Strikes Back",
                "Return of the Jedi",
                "The Force Awakens",
                "The Last Jedi",
                "The Rise of Skywalker",
            ],
            OnHit=self.onHit,
        )
        sz.append(ddc, proportion=1, halign="center")
        self.spinner = dSpinner(self, OnHit=self.on_spin_change)
        self.spinner.Caption = "Selected Position:"
        self.spinner.Increment = 0
        self.spinner.Min = 0
        self.spinner.Max = len(ddc.Choices)-1
        sz.append(self.spinner, proportion=0, border=5, halign="center")

        sz.appendSpacer(25, proportion=3)


    def onHit(self, evt):
        print("KeyValue: ", self.dropdown_control.KeyValue)
        print("PositionValue: ", self.dropdown_control.PositionValue)
        print("StringValue: ", self.dropdown_control.StringValue)
        print("Value: ", self.dropdown_control.Value)
        # Keep the spinner in sync
        self.spinner.Value = self.dropdown_control.PositionValue

    def on_spin_change(self, evt):
        pos = evt.EventObject.Value
        self.dropdown_control.PositionValue = pos
        print("PositionValue: ", self.dropdown_control.PositionValue)
        print("StringValue: ", self.dropdown_control.StringValue)
        print("Value: ", self.dropdown_control.Value)
        self.refresh()



category = "Controls.dDropdownList"

overview = """
<p>The <b>dDropdownList</b> class is a UI tool for enabling the user to select from a small number
of choices.</p>

<p>Like other list-type controls, it has <b>Value</b>, <b>StringValue</b>, and <b>PositionValue</b>
properties for accessing the state of the control.</p>

<p>In general, it is a bad design idea to use this control for more than, say, a dozen or so items.
With greater numbers the control becomes difficult to use due to the need for scrolling.</p>
"""
