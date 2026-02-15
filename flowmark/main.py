#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark 主入口文件
"""

import sys
from PyQt6.QtWidgets import QApplication
from flowmark.ui.main_window import MainWindow

def main():
    """主函数"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
