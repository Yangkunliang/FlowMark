#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark 启动脚本
"""

import os
import sys
import subprocess

# 检查并安装依赖
def install_dependencies():
    print("正在检查依赖...")
    try:
        # 检查是否已安装 pip
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        
        # 安装依赖
        print("正在安装依赖...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
        print("依赖安装成功！")
    except Exception as e:
        print(f"依赖安装失败: {str(e)}")
        sys.exit(1)

# 启动应用
def start_app():
    print("正在启动 FlowMark...")
    try:
        subprocess.run([sys.executable, "-m", "flowmark.main"])
    except Exception as e:
        print(f"启动应用失败: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # 切换到脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 安装依赖
    install_dependencies()
    
    # 启动应用
    start_app()
