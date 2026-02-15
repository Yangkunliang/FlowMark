#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark 文件处理类
"""

import os

class FileHandler:
    """文件处理类"""
    
    def __init__(self):
        self.recent_files = []
        
    def open_file(self, file_path):
        """打开文件"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 添加到最近打开的文件列表
        if file_path not in self.recent_files:
            self.recent_files.insert(0, file_path)
            # 只保留最近 10 个文件
            if len(self.recent_files) > 10:
                self.recent_files = self.recent_files[:10]
        
        return content
    
    def save_file(self, file_path, content):
        """保存文件"""
        # 确保目录存在
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # 添加到最近打开的文件列表
        if file_path not in self.recent_files:
            self.recent_files.insert(0, file_path)
            # 只保留最近 10 个文件
            if len(self.recent_files) > 10:
                self.recent_files = self.recent_files[:10]
        
    def get_recent_files(self):
        """获取最近打开的文件列表"""
        return self.recent_files
