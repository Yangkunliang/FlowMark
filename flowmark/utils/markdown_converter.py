#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark Markdown 转换类
"""

import markdown

class MarkdownConverter:
    """Markdown 转换类"""
    
    def to_markdown(self, text):
        """将文本转换为 Markdown 格式"""
        # 这里简化处理，实际需要根据富文本格式进行转换
        # 由于我们的编辑器直接使用 Markdown 语法，所以这里直接返回原文
        return text
    
    def to_html(self, text):
        """将 Markdown 转换为 HTML 格式"""
        return markdown.markdown(text)
