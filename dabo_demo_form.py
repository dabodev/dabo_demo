import sys
import glob
import importlib
import os
import sys

import dabo
from dabo import events
from dabo import ui
from dabo.lib.utils import ustr
from dabo.dLocalize import _

from modules import DemoModules
from modules import DemoError
from modules import DemoErrorPanel


class DaboDemoForm(ui.dForm):
    def __init__(self):
        super().__init__(
            parent=None,
            Name="DaboDemoForm",
            Caption="Dabo: A Demonstration",
            SaveRestorePosition=True,
        )
        self.Sizer = None
        self._activeCode = 0

        parentStack = []
        sizerDict = {}
        currParent = self
        currSizer = None
        sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dSplitter(
            currParent, attProperties={"Split": "False", "ShowPanelSplitMenu": "False"}
        )
        ui.setAfter(obj, "Orientation", "Vertical")
        ui.setAfter(obj, "Split", True)
        ui.setAfter(obj, "SashPosition", 307)

        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Center",
                    "VAlign": "Middle",
                    "Border": 0,
                    "Expand": True,
                },
            )

        splt_35589 = obj
        splt_35589.createPanes(self.getCustControlClass("dPanel_84311"), pane=1)
        splt_35589.createPanes(self.getCustControlClass("dPanel_30872"), pane=2)
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = obj
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        currParent = splt_35589.Panel1
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = self.getCustControlClass("dTreeView_55394")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Center",
                    "VAlign": "Middle",
                    "Border": 0,
                    "Expand": True,
                },
            )

        def _addDesTreeNode(_nodeParent, _nodeAtts, _kidNodes):
            _nodeCaption = self._extractKey(_nodeAtts, "Caption", "")
            if _nodeParent is None:
                obj.clear()
                _currNode = obj.setRootNode(_nodeCaption)
            else:
                _currNode = _nodeParent.appendChild(_nodeCaption)
            # Remove the name and designerClass atts
            self._extractKey(_nodeAtts, "name")
            self._extractKey(_nodeAtts, "designerClass")
            for _nodeProp, _nodeVal in _nodeAtts.items():
                setattr(_currNode, _nodeProp, _nodeVal)
                # try:
                #    exec "_currNode.%s = %s" % (_nodeProp, _nodeVal) in locals()
                # except (SyntaxError, NameError):
                #    exec "_currNode.%s = '%s'" % (_nodeProp, _nodeVal) in locals()
            for _kidNode in _kidNodes:
                _kidAtts = _kidNode.get("attributes", {})
                _kidKids = _kidNode.get("children", {})
                _addDesTreeNode(_currNode, _kidAtts, _kidKids)

        # Set the root
        _rootNode = {
            "name": "dNode",
            "attributes": {
                "Caption": "This is the root",
                "designerClass": "controlMix",
            },
            "children": [
                {
                    "name": "dNode",
                    "attributes": {
                        "Caption": "First Child",
                        "designerClass": "controlMix",
                    },
                },
                {
                    "name": "dNode",
                    "attributes": {
                        "Caption": "Second Child",
                        "designerClass": "controlMix",
                    },
                    "children": [
                        {
                            "name": "dNode",
                            "attributes": {
                                "Caption": "Grandkid #1",
                                "designerClass": "controlMix",
                            },
                        },
                        {
                            "name": "dNode",
                            "attributes": {
                                "Caption": "Grandkid #2",
                                "designerClass": "controlMix",
                            },
                            "children": [
                                {
                                    "name": "dNode",
                                    "attributes": {
                                        "Caption": "Great-Grandkid #1",
                                        "designerClass": "controlMix",
                                    },
                                }
                            ],
                        },
                        {
                            "name": "dNode",
                            "attributes": {
                                "Caption": "Grandkid #3",
                                "designerClass": "controlMix",
                            },
                        },
                    ],
                },
                {
                    "name": "dNode",
                    "attributes": {
                        "Caption": "Third Child",
                        "designerClass": "controlMix",
                    },
                },
            ],
        }
        _rootNodeAtts = _rootNode.get("attributes", {})
        _rootNodeKids = _rootNode.get("children", {})
        _addDesTreeNode(None, _rootNodeAtts, _rootNodeKids)

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = splt_35589.Panel2
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = self.getCustControlClass("dPageFrameNoTabs_66797")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Center",
                    "VAlign": "Middle",
                    "Border": 0,
                    "Expand": True,
                },
            )

        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = obj
        sizerDict[currParent] = []

        # save a reference to the parent control
        pgf_92394 = obj

        pg = ui.dPage(pgf_92394, attProperties={"Caption": ""})
        pgf_92394.appendPage(pg)
        currSizer = pg.Sizer = None
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = pg
        sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = self.getCustControlClass("dHtmlBox_63039")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Left",
                    "VAlign": "Top",
                    "Border": 0,
                    "Expand": True,
                },
            )

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        pg = ui.dPage(pgf_92394, attProperties={"Caption": "", "NameBase": "dPage1"})
        pgf_92394.appendPage(pg)
        currSizer = pg.Sizer = None
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = pg
        sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = self.getCustControlClass("dPageFrame_96145")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Left",
                    "VAlign": "Middle",
                    "Border": 0,
                    "Expand": True,
                },
            )

        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = obj
        sizerDict[currParent] = []

        # save a reference to the parent control
        pgf_87462 = obj

        pg = ui.dPage(pgf_87462, attProperties={"Caption": "Overview"})
        pgf_87462.appendPage(pg)
        currSizer = pg.Sizer = None
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = pg
        sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dHtmlBox(currParent, attProperties={"RegID": "moduleOverview"})
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Left",
                    "VAlign": "Top",
                    "Border": 0,
                    "Expand": True,
                },
            )

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        pg = ui.dPage(
            pgf_87462,
            attProperties={
                "RegID": "codePage",
                "Caption": "Demo Code",
                "NameBase": "dPage1",
            },
        )
        pgf_87462.appendPage(pg)
        currSizer = pg.Sizer = None
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = pg
        sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dSizer(Orientation="Horizontal")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 0,
                    "HAlign": "Left",
                    "VAlign": "Top",
                    "Border": 0,
                    "Expand": True,
                },
            )

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = self.getCustControlClass("dRadioList_75068")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Left",
                    "VAlign": "Middle",
                    "Border": 4,
                    "Expand": True,
                },
            )

        if currSizer:
            itm = currSizer.appendSpacer(12)
            currSizer.setItemProps(itm, {"VAlign": "Top", "Border": 0, "Expand": True})

        obj = self.getCustControlClass("dButton_30196")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 0,
                    "HAlign": "Center",
                    "VAlign": "Middle",
                    "Border": 5,
                    "Expand": False,
                },
            )

        obj = self.getCustControlClass("dButton_77264")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 0,
                    "HAlign": "Center",
                    "VAlign": "Middle",
                    "Border": 5,
                    "Expand": False,
                },
            )

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        obj = self.getCustControlClass("dEditor_67614")(currParent)
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Center",
                    "VAlign": "Top",
                    "Border": 0,
                    "Expand": True,
                },
            )

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        pg = self.getCustControlClass("dPage_7431")(pgf_87462)
        pgf_87462.appendPage(pg)
        currSizer = pg.Sizer = None
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = pg
        sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dSplitter(
            currParent, attProperties={"Split": "False", "ShowPanelSplitMenu": "False"}
        )
        ui.setAfter(obj, "Orientation", "Horizontal")
        ui.setAfter(obj, "Split", True)
        ui.setAfter(obj, "SashPosition", 536)

        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Left",
                    "VAlign": "Middle",
                    "Border": 0,
                    "Expand": True,
                },
            )

        splt_14990 = obj
        splt_14990.createPanes(self.getCustControlClass("dPanel_61778"), pane=1)
        splt_14990.createPanes(self.getCustControlClass("dPanel_76865"), pane=2)
        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = obj
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        currParent = splt_14990.Panel1
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dPanel(
            currParent, attProperties={"RegID": "demoPanel", "AlwaysResetSizer": "True"}
        )
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Center",
                    "VAlign": "Middle",
                    "Border": 0,
                    "Expand": True,
                },
            )

        parentStack.append(currParent)
        sizerDict[currParent].append(currSizer)
        currParent = obj
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dPanel(currParent, attProperties={})
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "Expand": True,
                    "Proportion": 1,
                    "BorderSides": ["All"],
                    "HAlign": "Left",
                    "VAlign": "Top",
                    "Border": 0,
                },
            )

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if not (currParent in sizerDict):
            sizerDict[currParent] = []
            currSizer = None
        else:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = splt_14990.Panel2
        currSizer = None
        if not (currParent in sizerDict):
            sizerDict[currParent] = []

        obj = ui.dSizer(Orientation="Vertical")
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(obj, {})

        if currSizer:
            sizerDict[currParent].append(currSizer)
        currSizer = obj
        if not currParent.Sizer:
            currParent.Sizer = obj

        obj = ui.dEditBox(currParent, attProperties={"RegID": "log", "ReadOnly": "True"})
        if currSizer:
            currSizer.append(obj)
            currSizer.setItemProps(
                obj,
                {
                    "BorderSides": ["All"],
                    "Proportion": 1,
                    "HAlign": "Center",
                    "VAlign": "Top",
                    "Border": 0,
                    "Expand": True,
                },
            )

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if not (currParent in sizerDict):
            sizerDict[currParent] = []
            currSizer = None
        else:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if not (currParent in sizerDict):
            sizerDict[currParent] = []
            currSizer = None
        else:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if not (currParent in sizerDict):
            sizerDict[currParent] = []
            currSizer = None
        else:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

        currParent = parentStack.pop()
        if not (currParent in sizerDict):
            sizerDict[currParent] = []
            currSizer = None
        else:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass

        if sizerDict[currParent]:
            try:
                currSizer = sizerDict[currParent].pop()
            except (KeyError, IndexError):
                pass
        else:
            currSizer = None

    def editorChanged(self):
        self.saveModButton.Enabled = self.codeEditor.Modified

    def logit(self, txt):
        self.log.Value += "%s\n" % txt
        self.log.scrollToEnd()
        self.log.ShowPosition(self.log.GetLastPosition())

    def _setActiveCode(self, val):
        self.demoModules.setActive(val)
        self.loadDemo()
        self.loadDemoSource()
        self.radMod.Value = val

    def _getActiveCode(self):
        try:
            ret = self.demoModules.getActive()
        except Exception as e:
            ret = 0
        return ret

    def showCode(self, line=-1):
        self.codeEditor.showContainingPage()
        if line is not None:
            self.codeEditor.LineNumber = line

    def afterInit(self):
        self.BasePrefKey = "demo.dabo_demo"
        self._defaultLeft = 50
        self._defaultTop = 50
        w, h = dabo.ui.getDisplaySize()
        self._defaultWidth = w - 100
        self._defaultHeight = h - 100
        self.setupMenu()

    def setOverview(self):
        module = self.demoModules.getActive()
        ov = module.overview
        self.moduleOverview.Source = ov

    def afterInitAll(self):
        pth = os.path.abspath(os.path.join(self.Application.HomeDirectory, "samples"))
        if pth not in sys.path:
            sys.path.insert(0, pth)
        self.demos = demos = {}
        exFiles = glob.glob(os.path.join(pth, "*.py"))
        for f in exFiles:
            justFname = os.path.splitext(os.path.split(f)[1])[0]
            if justFname.startswith("_"):
                continue
            exx = importlib.import_module(justFname)
            maincat, subcat = exx.category.split(".")
            if maincat not in demos:
                demos[maincat] = {}
            demos[maincat][subcat] = justFname
            del locals()["exx"]
        # Create the tree
        tree = self.tree
        tree.clear()
        root = tree.setRootNode(_("Dabo Overview"))
        for mc in sorted(demos):
            nd = tree.appendNode(root, mc)
            for sc in sorted(demos[mc]):
                sn = tree.appendNode(nd, sc)
                sn._obj = demos[mc][sc]
        tree.expandAll()
        tree.setFocus()

    def saveModCode(self):
        self.demoModules.saveMod(self.codeEditor.Value)
        self.ActiveCode = 1
        self.demoModules.updateFile()
        self.radMod.reset(self.codeEditor.Modified)

    def onClearOutput(self, evt):
        self.log.Value = ""

    def loadDemo(self):
        dpnl = self.demoPanel
        sz = dpnl.Sizer
        for kid in dpnl.Children:
            sz.remove(kid, True)
        try:
            pnl = self.demoModules.getActive().TestPanel(dpnl)
        except Exception as e:
            pnl = DemoErrorPanel(dpnl)
            err = DemoError(sys.exc_info())
            pnl.setErrorInfo(self.codePage, err)
        sz.append1x(pnl)
        if self.displayFrame.SelectedPageNumber != 2:
            # Switch to the demo
            ui.callAfter(self.demoPageFrame.showDemoPage)
        self.demoPanel.layout(resetMin=True)

    def treeSelection(self):
        try:
            sel = self.tree.Selection._obj
            self.demoModules = DemoModules(sel)
            self.setOverview()
            self.loadDemoSource()
            self.loadDemo()
            self.log.Value = ""
            ok = True
        except AttributeError:
            ok = False
        self.displayFrame.showContents(ok)

    def loadDemoSource(self):
        dm = self.demoModules
        self.codeEditor.Value = dm.getSource()
        mod = dm.hasModified()
        self.radMod.reset(mod)
        self.saveModButton.Enabled = False
        self.delModButton.Enabled = mod

    def deleteModCode(self):
        self.demoModules.deleteModified()
        self.ActiveCode = 0

    def setupMenu(self):
        mb = self.MenuBar
        vm = mb.getMenu("base_view")
        vm.remove("view_showsizerlines")
        vm.append(
            _("Clear Ou&tput"),
            HotKey="Ctrl+Back",
            ItemID="view_clearoutput",
            OnHit=self.onClearOutput,
            help=_("Clear the output area"),
        )

    ActiveCode = property(
        _getActiveCode, _setActiveCode, None, """Zero for Original; 1 for modified"""
    )

    def getCustControlClass(self, clsName):
        # Define the classes, and return the matching class
        class dPanel_84311(ui.dPanel):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "Width": "305",
                    "AlwaysResetSizer": "True",
                    "NameBase": "dPanel2",
                    "Height": "680",
                },
                *args,
                **kwargs,
            ):
                ui.dPanel.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

        class dPanel_30872(ui.dPanel):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "Width": "725",
                    "AlwaysResetSizer": "True",
                    "NameBase": "dPanel1",
                    "Height": "680",
                },
                *args,
                **kwargs,
            ):
                ui.dPanel.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

        class dTreeView_55394(ui.dTreeView):
            def __init__(self, parent=None, attProperties={"RegID": "tree"}, *args, **kwargs):
                ui.dTreeView.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def onTreeSelection(self, evt):
                self.Form.treeSelection()

        class dPageFrameNoTabs_66797(ui.dPageFrameNoTabs):
            def __init__(
                self, parent=None, attProperties={"RegID": "displayFrame"}, *args, **kwargs
            ):
                ui.dPageFrameNoTabs.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def showContents(self, showCode):
                self.SelectedPageNumber = {True: 1, False: 0}[showCode]

        class dHtmlBox_63039(ui.dHtmlBox):
            def __init__(
                self, parent=None, attProperties={"RegID": "mainOverview"}, *args, **kwargs
            ):
                ui.dHtmlBox.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def afterInit(self):
                self.Source = """<div align="center"><img src="dabo_lettering_250x100.png"></div>
                <h1 align="center">Dabo Demonstration</h1>
                """

        class dPageFrame_96145(ui.dPageFrame):
            def __init__(
                self, parent=None, attProperties={"RegID": "demoPageFrame"}, *args, **kwargs
            ):
                ui.dPageFrame.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def showDemoPage(self):
                self.SelectedPageNumber = 2

        class dRadioList_75068(ui.dRadioList):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "ValueMode": "position",
                    "Orientation": "Horizontal",
                    "Value": "0",
                    "Choices": "[u'Original', u'Modified']",
                    "Caption": "Active Version",
                    "DataField": "ActiveCode",
                    "RegID": "radMod",
                    "DataSource": "form",
                },
                *args,
                **kwargs,
            ):
                ui.dRadioList.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def reset(self, hasMod):
                self.enableString("Modified", hasMod)

            def afterInit(self):
                self.reset(False)

        class dButton_30196(ui.dButton):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "RegID": "saveModButton",
                    "Width": "111",
                    "Caption": "Save Changes",
                },
                *args,
                **kwargs,
            ):
                ui.dButton.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def onHit(self, evt):
                # Save modified code
                self.Form.saveModCode()

        class dButton_77264(ui.dButton):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "NameBase": "dButton1",
                    "Caption": "Delete Modified",
                    "Width": "124",
                    "RegID": "delModButton",
                },
                *args,
                **kwargs,
            ):
                ui.dButton.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def onHit(self, evt):
                # Delete modified code
                self.Form.deleteModCode()

        class dEditor_67614(ui.dEditor):
            def __init__(self, parent=None, attProperties={"RegID": "codeEditor"}, *args, **kwargs):
                ui.dEditor.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

            def afterInit(self):
                self.Language = "Python"
                self.bindKey("F5", self.autoComplete)

            def onContentChanged(self, evt):
                self.Form.editorChanged()

        class dPage_7431(ui.dPage):
            def __init__(
                self,
                parent=None,
                attProperties={"Caption": "Demo", "NameBase": "dPage2"},
                *args,
                **kwargs,
            ):
                ui.dPage.__init__(self, parent=parent, attProperties=attProperties, *args, **kwargs)

            def onPageEnter(self, evt):
                if hasattr(self, "_shown"):
                    return
                self._shown = True
                ht = 1.0 * self.Height
                pos = self.dSplitter.SashPosition
                if pos / ht < 0.75:
                    self.dSplitter.SashPosition = ht * 0.75
                    self.layout(resetMin=True)

        class dPanel_61778(ui.dPanel):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "Width": "715",
                    "AlwaysResetSizer": "True",
                    "NameBase": "dPanel2",
                    "Height": "534",
                },
                *args,
                **kwargs,
            ):
                ui.dPanel.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

        class dPanel_76865(ui.dPanel):
            def __init__(
                self,
                parent=None,
                attProperties={
                    "Width": "715",
                    "AlwaysResetSizer": "True",
                    "NameBase": "dPanel1",
                    "Height": "95",
                },
                *args,
                **kwargs,
            ):
                ui.dPanel.__init__(
                    self, parent=parent, attProperties=attProperties, *args, **kwargs
                )

        return eval(clsName)
