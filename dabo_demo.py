#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import platform

import dabo
from dabo.application import dApp

from dabo_demo_form import DaboDemoForm


def main():
    # The splash screen looks great on Mac/Win, and crappy on Linux.
    useSplash = "linux" not in platform.platform().lower()

    app = dApp(
        showSplashScreen=useSplash,
        splashTimeout=3000,
        MainFormClass=DaboDemoForm,
        BasePrefKey="demo.DaboDemo",
    )
    app.setAppInfo("appName", "DaboDemo")
    app.start()


if __name__ == "__main__":
    main()
