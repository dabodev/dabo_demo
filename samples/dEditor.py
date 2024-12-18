# -*- coding: utf-8 -*-
import dabo
from dabo import events
from dabo import ui
from dabo.dLocalize import _
from dabo.ui import dLabel
from dabo.ui import dButton
from dabo.ui import dDropdownList
from dabo.ui import dPanel
from dabo.ui import dSizer
from dabo.ui import dSpinner

dEditor = ui.dEditor


class TestPanel(dPanel):
    def afterInit(self):
        sz = self.Sizer = dSizer("h")
        sz.appendSpacer(10)

        self.edt = dEditor(self)
        open_btn = dButton(self, Caption="Open...", OnHit=self.open_file)
        save_btn = dButton(
            self,
            Caption="Save",
            Enabled=False,
            Name="EdSave",
            OnHit=self.save_file,
        )
        save_btn.DynamicEnabled = self.edt.isChanged
        vsz = dSizer("v")
        vsz.appendSpacer(10)
        vsz.append(open_btn, border=5)
        vsz.append(save_btn, border=5)
        self.languages = self.edt.getAvailableLanguages()
        self.sel_lang = dDropdownList(
            self,
            Choices=self.languages,
            DataSource=self.edt,
            DataField="Language",
            OnHit=self.set_syntax_lang,
        )
        self.fonts = ui.getAvailableFonts()
        self.sel_font = dDropdownList(
            self, Choices=self.fonts, Value=self.edt.FontFace, OnHit=self.set_font
        )
        self.spn_sz = dSpinner(
            self,
            Increment=1,
            Max=256,
            Min=6,
            DataSource=self.edt,
            DataField="FontSize",
        )
        self.update_btn = dButton(self, Caption="Update", OnHit=self.call_update)
        vsz.append(self.sel_lang, border=5)
        vsz.append(self.sel_font, border=5)
        vsz.append(self.spn_sz, border=5)
        vsz.append(self.update_btn, border=5)
        sz.append(vsz, halign="center")
        sz.appendSpacer(10)
        sz.append1x(self.edt, halign="center", border=33)
        sz.appendSpacer(10)

    def isEditorChanged(self):
        chg = self.edt.isChanged()
        return chg

    def open_file(self, evt):
        self.edt.openFile()
        self.update()

    def save_file(self, evt):
        self.edt.saveFile()
        self.update()

    def call_update(self, evt):
        self.update()

    def set_syntax_lang(self, evt):
        idx = evt.EventData["index"]
        self.edt.Language = self.languages[idx]
        self.update()

    def set_font(self, evt):
        idx = evt.EventData["index"]
        self.edt.FontFace = self.fonts[idx]
        self.update()


category = "Controls.dEditor"

overview = """
<p>The <b>dEditor</b> allows you to embed a code editor in your app, complete with syntax
highlighting and code completion. The editor is based on the Scintilla tool
(https://www.scintilla.org/)</p>
"""
