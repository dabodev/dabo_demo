# -*- coding: utf-8 -*-
import dabo
from dabo import events
from dabo.dLocalize import _


from dabo.ui import dLabel
from dabo.ui import dPanel
from dabo.ui import dSizer
from dabo.ui import dSpinner
from dabo.ui import dTextBox

dGridSizer = dabo.ui.dGridSizer


class TestPanel(dPanel):
    def afterInit(self):

        sz = self.Sizer = dSizer("V")
        sz.appendSpacer(50)

        intro = _(
            "This demo shows the effect of the HGap and VGap properties on a GridSizer. "
            "The panel containing the grid sizer has a tan background, and the various controls "
            "in the sizer have a light blue background. These colors help you to visualize the effect "
            "of changing these properties."
        )
        cap = dLabel(self, Caption=intro, Width=400, WordWrap=True)
        sz.append(cap, halign="center")
        sz.appendSpacer(25)

        # Create the grid sizer
        gridPanel = dPanel(self, BackColor="moccasin")
        gs = self.demo_grid_sizer = gridPanel.Sizer = dGridSizer(MaxCols=2, HGap=3, VGap=8)

        lbl = dLabel(gridPanel, Caption="First")
        ctl = dTextBox(gridPanel)
        gs.append(lbl, halign="right")
        gs.append(ctl, layout="x")
        lbl = dLabel(gridPanel, Caption="Second")
        ctl = dTextBox(gridPanel)
        gs.append(lbl, halign="right")
        gs.append(ctl, layout="x")
        lbl = dLabel(gridPanel, Caption="Third")
        ctl = dTextBox(gridPanel)
        gs.append(lbl, halign="right")
        gs.append(ctl, layout="x")
        lbl = dLabel(gridPanel, Caption="Fourth")
        ctl = dTextBox(gridPanel)
        gs.append(lbl, halign="right")
        gs.append(ctl, layout="x")

        gs.setColExpand(True, 1)

        hs = dSizer("H")
        hs.append1x(gridPanel, halign="center")

        gs = dGridSizer(MaxCols=2)
        lbl = dLabel(self, Caption=_("HGap:"))
        gs.append(lbl, halign="right")
        spn = dSpinner(self, DataSource="self.Parent.demo_grid_sizer", DataField="HGap")
        spn.bindEvent(events.Hit, self.onChangeLayout)
        gs.append(spn)

        lbl = dLabel(self, Caption=_("VGap:"))
        gs.append(lbl, halign="right")
        spn = dSpinner(self, DataSource="self.Parent.demo_grid_sizer", DataField="VGap")
        spn.bindEvent(events.Hit, self.onChangeLayout)
        gs.append(spn)

        # Add this *before* the first grid sizer
        hs.insert(0, gs, halign="center")
        hs.prependSpacer(30)
        # Now add the horizontal sizer to the main sizer for the panel.
        sz.append(hs, valign="middle", proportion=1, layout="expand")
        # Call update() to set the controls' Value.
        self.update()

    def onChangeLayout(self, evt):
        self.layout()


category = "Layout.dGridSizer"

overview = """
<p><b>dGridSizer</b> is a two-dimensional sizer for laying out items in a grid
of rows and columns. You can specify a particular row/col position when you add
an item, or simply call '<b>append()</b>' and the grid will place it in the first
available cell.</p>

<p>The key properties to set are <b>MaxRows</b> and <b>MaxCols</b>.
You only set one or the other; what this tells the grid is how many rows/columns
to create before starting another row/col in the grid. Example: if you have a series of
controls that you want to add, and they consist of an identifying label and its
matching control, and you want them arranged in a grid with the label in the left
column and the control in the right column, simply set MaxCols to 2, and then append
label, control, label, control, label, control, etc., and the grid sizer will automatically
construct the appropriate grid.</p>

<p>Two other important properties are <b>HGap</b> and <b>VGap</b>, which control
the horizontal and vertical spacing between grid cells, respectively.</p>
"""
