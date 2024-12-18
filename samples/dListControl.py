# -*- coding: utf-8 -*-
import dabo
import dabo.ui
from dabo import events
from dabo.dLocalize import _


from dabo.ui import dLabel
from dabo.ui import dPanel
from dabo.ui import dSizer
from dabo.ui import dCheckBox
from dabo.ui import dSpinner

dListControl = dabo.ui.dListControl


class TestPanel(dPanel):
    def afterInit(self):
        sz = self.Sizer = dSizer("v")
        sz.appendSpacer(25)

        self.list_control = lc = dListControl(
            self,
            MultipleSelect=True,
            HorizontalRules=True,
            VerticalRules=True,
            OnHit=self.onHit,
            OnListSelection=self.onListSelection,
            OnListDeselection=self.onListDeselection,
        )
        sz.append(lc, proportion=1, border=10, halign="center")
        lc.setColumns(("Title", "Subtitle", "Release Year"))
        lc.setColumnWidth(0, 150)
        lc.setColumnWidth(1, 100)
        lc.setColumnWidth(2, 200)
        lc.append(("The Phantom Menace", "Episode 1", 1999))
        lc.append(("Attack of the Clones", "Episode 2", 2002))
        lc.append(("Revenge of the Sith", "Episode 3", 2005))
        lc.append(("A New Hope", "Episode 4", 1977))
        lc.append(("The Empire Strikes Back", "Episode 5", 1980))
        lc.append(("Return of the Jedi", "Episode 6", 1983))
        lc.append(("The Force Awakens", "Episode 7", 2015))
        lc.append(("The Last Jedi", "Episode 8", 2017))
        lc.append(("The Rise of Skywalker", "Episode 9", 2019))
        lc.Keys = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        sz.appendSpacer(25)
        chk_hrules = dCheckBox(self, Caption="Horizontal Rules", DataSource=lc,
                               DataField="HorizontalRules")
        chk_vrules = dCheckBox(self, Caption="Vertical Rules", DataSource=lc,
                               DataField="VerticalRules")
        chk_header = dCheckBox(self, Caption="Show Header", DataSource=lc,
                               DataField="HeaderVisible")
        chk_sort = dCheckBox(self, Caption="Sort on Header Click", DataSource=lc,
                               DataField="SortOnHeaderClick")
        sz.append(chk_hrules, border=200, borderSides=["left"])
        sz.append(chk_vrules, border=200, borderSides=["left"])
        sz.append(chk_header, border=200, borderSides=["left"])
        sz.append(chk_sort, border=200, borderSides=["left"])
        sz.appendSpacer(25)


    def onHit(self, evt):
        print("KeyValue: ", self.list_control.KeyValue)
        print("PositionValue: ", self.list_control.PositionValue)
        print("StringValue: ", self.list_control.StringValue)
        print("Value: ", self.list_control.Value)

    def onListSelection(self, evt):
        print(
            "List Selection!",
            self.list_control.Value,
            self.list_control.LastSelectedIndex,
            self.list_control.SelectedIndices,
        )

    def onListDeselection(self, evt):
        print("Row deselected:", evt.EventData["index"])


category = "Controls.dListControl"

overview = """
<p>The <b>dListControl</b> class is a handy UI tool to display a value in relation
to a range of possible values.</p>

<p>You control the range of the slider using the <b>Min</b> and <b>Max</b>
properties, and set its value with the <b>Value</b> property. The slider will then
display its 'thumb control' in a position proportional to its value in relation to the Min and
Max values. Dragging the 'thumb control' changes the Value property, and also generates
a <b>Hit event</b>.</p>

<p>There are two modes for generating Hit events in a slider, and this is controlled
by the <b>Continuous</b> property. When Continuous is False (<i>default</i>), Hit events
are only raised when the thumb control is released. With Continuous set to True, however,
Hit events are generated continuously as the thumb control is dragged.</p>

<p>If the <b>ShowLabels</b> property is True, then the slider will also display
its Min and Max values, as well as its current Value. Please note that this is must be
set when the control is created; it has no effect once the control exists.</p>
"""
