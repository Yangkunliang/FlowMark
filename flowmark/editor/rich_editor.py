#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark 富文本编辑器类
"""

from PyQt6.QtWidgets import QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt6.QtCore import Qt

class RichEditor(QTextEdit):
    """富文本编辑器类"""
    
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("在此输入内容...")
        
    def format_text(self, format_type):
        """格式化文本"""
        cursor = self.textCursor()
        char_format = QTextCharFormat()
        
        if format_type == "bold":
            char_format.setFontWeight(QFont.Weight.Bold if not cursor.charFormat().fontWeight() == QFont.Weight.Bold else QFont.Weight.Normal)
        elif format_type == "italic":
            char_format.setFontItalic(not cursor.charFormat().fontItalic())
        elif format_type == "underline":
            char_format.setFontUnderline(not cursor.charFormat().fontUnderline())
        
        cursor.mergeCharFormat(char_format)
        self.setTextCursor(cursor)
        
    def set_heading(self, level):
        """设置标题级别"""
        cursor = self.textCursor()
        # 在文本前添加 # 符号
        cursor.insertText("#" * level + " ")
        self.setTextCursor(cursor)
        
    def insert_list(self, list_type):
        """插入列表"""
        cursor = self.textCursor()
        if list_type == "unordered":
            cursor.insertText("- ")
        else:
            cursor.insertText("1. ")
        self.setTextCursor(cursor)
        
    def insert_quote(self):
        """插入引用"""
        cursor = self.textCursor()
        cursor.insertText("> ")
        self.setTextCursor(cursor)
        
    def insert_code_block(self):
        """插入代码块"""
        cursor = self.textCursor()
        code_block = "```\ncode\n```\n"
        cursor.insertText(code_block)
        # 移动光标到代码块内部
        cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.MoveAnchor, 4)
        self.setTextCursor(cursor)
        
    def insert_table(self):
        """插入表格"""
        cursor = self.textCursor()
        table = "| 表头1 | 表头2 |\n| --- | --- |\n| 内容1 | 内容2 |\n"
        cursor.insertText(table)
        self.setTextCursor(cursor)
        
    def insert_image(self):
        """插入图片"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.jpeg *.gif *.bmp)")
        
        if file_path:
            cursor = self.textCursor()
            cursor.insertText(f"![alt text]({file_path})")
            self.setTextCursor(cursor)
        else:
            # 如果用户取消选择，插入默认占位符
            cursor = self.textCursor()
            cursor.insertText("![alt text](image_url)")
            self.setTextCursor(cursor)
        
    def insert_link(self):
        """插入链接"""
        cursor = self.textCursor()
        if cursor.hasSelection():
            text = cursor.selectedText()
            cursor.insertText(f"[{text}](url)")
        else:
            cursor.insertText("[链接文本](url)")
        self.setTextCursor(cursor)
        
    def insert_horizontal_rule(self):
        """插入分割线"""
        cursor = self.textCursor()
        cursor.insertText("\n---\n")
        self.setTextCursor(cursor)
        
    def to_plain_text(self):
        """获取纯文本内容"""
        return self.toPlainText()
    
    def set_plain_text(self, text):
        """设置纯文本内容"""
        self.setPlainText(text)
        
    def clear(self):
        """清空编辑器内容"""
        self.setPlainText("")
