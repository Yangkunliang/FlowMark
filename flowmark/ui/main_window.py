#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FlowMark 主窗口类
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter, QStatusBar, QMenuBar, QMenu, QFileDialog, QMessageBox, QTabWidget, QToolBar
from PyQt6.QtGui import QFont, QKeySequence, QAction
from PyQt6.QtCore import Qt, QSettings

from flowmark.editor.rich_editor import RichEditor
from flowmark.preview.markdown_preview import MarkdownPreview
from flowmark.utils.file_handler import FileHandler
from flowmark.utils.markdown_converter import MarkdownConverter

class MainWindow(QMainWindow):
    """主窗口类"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_settings()
        self.init_shortcuts()
        
        # 初始化工具类
        self.file_handler = FileHandler()
        self.markdown_converter = MarkdownConverter()
        
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle("FlowMark")
        self.setGeometry(100, 100, 1000, 800)
        
        # 中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 工具栏
        self.toolbar = QToolBar("编辑工具")
        self.addToolBar(self.toolbar)
        
        # 编辑器和预览区域
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(self.splitter)
        
        # 富文本编辑器
        self.editor = RichEditor()
        self.editor.textChanged.connect(self.update_preview)
        self.splitter.addWidget(self.editor)
        
        # 预览标签页
        self.preview_tab = QTabWidget()
        
        # Markdown 源码预览
        self.md_preview = MarkdownPreview()
        self.preview_tab.addTab(self.md_preview, "Markdown 源码")
        
        # 渲染预览
        self.render_preview = MarkdownPreview()
        self.render_preview.set_render_mode(True)
        self.preview_tab.addTab(self.render_preview, "渲染预览")
        
        self.splitter.addWidget(self.preview_tab)
        
        # 状态栏
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.update_status()
        
        # 菜单栏
        self.create_menu()
        
        # 工具栏按钮
        self.create_toolbar()
        
    def init_settings(self):
        """初始化设置"""
        self.settings = QSettings("FlowMark", "FlowMark")
        
        # 加载窗口大小
        if self.settings.contains("window/size"):
            self.resize(self.settings.value("window/size"))
        if self.settings.contains("window/position"):
            self.move(self.settings.value("window/position"))
        
        # 加载字体设置
        font_family = self.settings.value("editor/font_family", "Arial")
        font_size = int(self.settings.value("editor/font_size", 12))
        font = QFont(font_family, font_size)
        self.editor.setFont(font)
        
    def init_shortcuts(self):
        """初始化快捷键"""
        # 粗体
        bold_action = QAction("粗体", self)
        bold_action.setShortcut(QKeySequence("Ctrl+B"))
        bold_action.triggered.connect(lambda: self.editor.format_text("bold"))
        self.addAction(bold_action)
        
        # 斜体
        italic_action = QAction("斜体", self)
        italic_action.setShortcut(QKeySequence("Ctrl+I"))
        italic_action.triggered.connect(lambda: self.editor.format_text("italic"))
        self.addAction(italic_action)
        
        # 下划线
        underline_action = QAction("下划线", self)
        underline_action.setShortcut(QKeySequence("Ctrl+U"))
        underline_action.triggered.connect(lambda: self.editor.format_text("underline"))
        self.addAction(underline_action)
        
    def create_menu(self):
        """创建菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        
        new_action = QAction("新建", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction("打开", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("保存", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("另存为", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        export_menu = file_menu.addMenu("导出")
        
        export_md_action = QAction("导出为 Markdown", self)
        export_md_action.triggered.connect(self.export_md)
        export_menu.addAction(export_md_action)
        
        export_html_action = QAction("导出为 HTML", self)
        export_html_action.triggered.connect(self.export_html)
        export_menu.addAction(export_html_action)
        
        export_pdf_action = QAction("导出为 PDF", self)
        export_pdf_action.triggered.connect(self.export_pdf)
        export_menu.addAction(export_pdf_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("退出", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        
        copy_md_action = QAction("复制为 Markdown", self)
        copy_md_action.setShortcut("Ctrl+Shift+C")
        copy_md_action.triggered.connect(self.copy_as_markdown)
        edit_menu.addAction(copy_md_action)
        
        # 视图菜单
        view_menu = menubar.addMenu("视图")
        
        theme_menu = view_menu.addMenu("主题")
        
        light_theme_action = QAction("浅色主题", self)
        light_theme_action.triggered.connect(lambda: self.set_theme("light"))
        theme_menu.addAction(light_theme_action)
        
        dark_theme_action = QAction("深色主题", self)
        dark_theme_action.triggered.connect(lambda: self.set_theme("dark"))
        theme_menu.addAction(dark_theme_action)
        
    def create_toolbar(self):
        """创建工具栏"""
        # 标题按钮
        for i in range(1, 7):
            action = QAction(f"H{i}", self)
            action.triggered.connect(lambda checked, level=i: self.editor.set_heading(level))
            self.toolbar.addAction(action)
        
        self.toolbar.addSeparator()
        
        # 格式按钮
        bold_action = QAction("粗体", self)
        bold_action.triggered.connect(lambda: self.editor.format_text("bold"))
        self.toolbar.addAction(bold_action)
        
        italic_action = QAction("斜体", self)
        italic_action.triggered.connect(lambda: self.editor.format_text("italic"))
        self.toolbar.addAction(italic_action)
        
        underline_action = QAction("下划线", self)
        underline_action.triggered.connect(lambda: self.editor.format_text("underline"))
        self.toolbar.addAction(underline_action)
        
        self.toolbar.addSeparator()
        
        # 列表按钮
        ul_action = QAction("无序列表", self)
        ul_action.triggered.connect(lambda: self.editor.insert_list("unordered"))
        self.toolbar.addAction(ul_action)
        
        ol_action = QAction("有序列表", self)
        ol_action.triggered.connect(lambda: self.editor.insert_list("ordered"))
        self.toolbar.addAction(ol_action)
        
        self.toolbar.addSeparator()
        
        # 其他按钮
        quote_action = QAction("引用", self)
        quote_action.triggered.connect(self.editor.insert_quote)
        self.toolbar.addAction(quote_action)
        
        code_action = QAction("代码块", self)
        code_action.triggered.connect(self.editor.insert_code_block)
        self.toolbar.addAction(code_action)
        
        table_action = QAction("表格", self)
        table_action.triggered.connect(self.editor.insert_table)
        self.toolbar.addAction(table_action)
        
        image_action = QAction("图片", self)
        image_action.triggered.connect(self.editor.insert_image)
        self.toolbar.addAction(image_action)
        
        link_action = QAction("链接", self)
        link_action.triggered.connect(self.editor.insert_link)
        self.toolbar.addAction(link_action)
        
        hr_action = QAction("分割线", self)
        hr_action.triggered.connect(self.editor.insert_horizontal_rule)
        self.toolbar.addAction(hr_action)
        
    def update_preview(self):
        """更新预览"""
        text = self.editor.to_plain_text()
        md_text = self.markdown_converter.to_markdown(text)
        
        self.md_preview.set_content(md_text)
        self.render_preview.set_content(md_text)
        
        self.update_status()
        
    def update_status(self):
        """更新状态栏"""
        text = self.editor.to_plain_text()
        words = len(text.split())
        lines = text.count('\n') + 1
        self.status_bar.showMessage(f"字数: {words}, 行数: {lines}")
        
    def set_theme(self, theme):
        """设置主题"""
        if theme == "dark":
            # 简化处理，实际需要更复杂的样式设置
            self.editor.setStyleSheet("background-color: #333; color: #fff;")
            self.md_preview.setStyleSheet("background-color: #333; color: #fff;")
            self.render_preview.setStyleSheet("background-color: #333; color: #fff;")
        else:
            self.editor.setStyleSheet("")
            self.md_preview.setStyleSheet("")
            self.render_preview.setStyleSheet("")
        
    def new_file(self):
        """新建文件"""
        self.editor.clear()
        self.update_preview()
        
    def open_file(self):
        """打开文件"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "打开文件", "", "Markdown Files (*.md);;All Files (*)")
        
        if file_path:
            try:
                content = self.file_handler.open_file(file_path)
                self.editor.set_plain_text(content)
                self.update_preview()
            except Exception as e:
                QMessageBox.critical(self, "错误", f"打开文件失败: {str(e)}")
        
    def save_file(self):
        """保存文件"""
        # 这里简化处理，实际需要检查文件是否已保存过
        self.save_as_file()
        
    def save_as_file(self):
        """另存为文件"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "保存文件", "", "Markdown Files (*.md);;All Files (*)")
        
        if file_path:
            try:
                content = self.editor.to_plain_text()
                self.file_handler.save_file(file_path, content)
                QMessageBox.information(self, "成功", "文件保存成功")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存文件失败: {str(e)}")
        
    def export_md(self):
        """导出为 Markdown"""
        self.save_as_file()
        
    def export_html(self):
        """导出为 HTML"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "导出为 HTML", "", "HTML Files (*.html);;All Files (*)")
        
        if file_path:
            try:
                content = self.editor.to_plain_text()
                html = self.markdown_converter.to_html(content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html)
                
                QMessageBox.information(self, "成功", "导出为 HTML 成功")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"导出为 HTML 失败: {str(e)}")
        
    def export_pdf(self):
        """导出为 PDF"""
        # 简化处理，实际需要使用 PyQt6 的 PDF 导出功能
        QMessageBox.information(self, "提示", "PDF 导出功能暂未实现")
        
    def copy_as_markdown(self):
        """复制为 Markdown"""
        import pyperclip
        content = self.editor.to_plain_text()
        md_text = self.markdown_converter.to_markdown(content)
        pyperclip.copy(md_text)
        QMessageBox.information(self, "成功", "Markdown 内容已复制到剪贴板")
        
    def closeEvent(self, event):
        """关闭事件"""
        # 保存窗口设置
        self.settings.setValue("window/size", self.size())
        self.settings.setValue("window/position", self.pos())
        
        # 保存字体设置
        font = self.editor.font()
        self.settings.setValue("editor/font_family", font.family())
        self.settings.setValue("editor/font_size", font.pointSize())
        
        event.accept()
