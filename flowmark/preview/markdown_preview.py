#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark Markdown 预览类
"""

from PyQt6.QtWidgets import QTextEdit

class MarkdownPreview(QTextEdit):
    """Markdown 预览类"""
    
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setPlaceholderText("预览区域...")
        self._render_mode = False
        
    def set_render_mode(self, render_mode):
        """设置渲染模式"""
        self._render_mode = render_mode
        
    def set_content(self, content):
        """设置内容"""
        if self._render_mode:
            # 渲染模式下使用 Markdown 渲染
            self.setMarkdown(content)
        else:
            # 源码模式下使用纯文本显示
            self.setPlainText(content)
        
    def setStyleSheet(self, style_sheet):
        """设置样式表"""
        super().setStyleSheet(style_sheet)
