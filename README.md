# FlowMark

FlowMark 是一个功能强大的桌面 Markdown 编辑器，提供所见即所得的编辑界面，用户可以直观地编辑内容，并能一键复制对应的 Markdown 格式文本。

## 核心功能

### 富文本编辑器功能
- 提供所见即所得的编辑界面
- 支持基本的富文本格式：
  - 标题（H1-H6）
  - 粗体、斜体、下划线
  - 有序列表和无序列表
  - 引用块
  - 代码块
  - 表格插入与编辑
  - 图片插入（支持本地和网络图片）
  - 超链接
  - 分割线

### Markdown 转换与预览
- 实时将富文本内容转换为 Markdown 语法
- 支持 Markdown 源码预览模式
- 支持渲染预览（查看最终效果）

### 复制功能
- 一键复制 Markdown 格式文本到剪贴板
- 支持选择复制（选区复制为 Markdown）

### 文件管理
- 新建、打开、保存 Markdown 文件（.md）
- 自动保存功能
- 最近打开的文件列表

### 界面要求
- 简洁清爽的界面设计
- 支持浅色/深色主题切换
- 可自定义编辑器字体和大小
- 窗口大小可调整，支持最大化/最小化

### 导出功能
- 导出为 Markdown（.md）
- 导出为 HTML
- 可选的导出为 PDF（暂未实现）

## 技术栈

- Python 3.8+
- GUI 框架：PyQt6
- Markdown 处理库：markdown
- 剪贴板操作：pyperclip
- 图像处理：Pillow

## 安装与运行

### 方法一：使用启动脚本（推荐）

1. **克隆仓库**：
   ```bash
   git clone https://github.com/Yangkunliang/FlowMark.git
   cd FlowMark
   ```

2. **运行启动脚本**：
   ```bash
   python3 run.py
   ```
   启动脚本会自动安装所需的依赖包并启动应用程序。

### 方法二：手动安装依赖

1. **克隆仓库**：
   ```bash
   git clone https://github.com/Yangkunliang/FlowMark.git
   cd FlowMark
   ```

2. **安装依赖**：
   ```bash
   pip3 install -r requirements.txt
   ```

3. **运行应用**：
   ```bash
   python3 -m flowmark.main
   ```

## 使用指南

### 基本编辑

1. **格式化文本**：使用工具栏按钮或快捷键（Ctrl+B 粗体，Ctrl+I 斜体，Ctrl+U 下划线）格式化文本。

2. **插入元素**：使用工具栏按钮插入标题、列表、引用、代码块、表格、图片、链接和分割线。

3. **图片插入**：点击图片按钮，选择本地图片文件，自动生成 Markdown 图片语法。

### 预览功能

- **Markdown 源码**：查看当前内容的 Markdown 源码格式。
- **渲染预览**：查看 Markdown 渲染后的效果。

### 文件操作

- **新建**：点击文件菜单 → 新建，或使用快捷键 Ctrl+N。
- **打开**：点击文件菜单 → 打开，或使用快捷键 Ctrl+O，选择 Markdown 文件。
- **保存**：点击文件菜单 → 保存，或使用快捷键 Ctrl+S。
- **另存为**：点击文件菜单 → 另存为，或使用快捷键 Ctrl+Shift+S。

### 导出功能

- **导出为 Markdown**：点击文件菜单 → 导出 → 导出为 Markdown。
- **导出为 HTML**：点击文件菜单 → 导出 → 导出为 HTML。
- **导出为 PDF**：暂未实现。

### 主题切换

- **浅色主题**：点击视图菜单 → 主题 → 浅色主题。
- **深色主题**：点击视图菜单 → 主题 → 深色主题。

## 项目结构

```
FlowMark/
├── flowmark/             # 主包
│   ├── __init__.py       # 包初始化文件
│   ├── main.py           # 主入口文件
│   ├── editor/           # 编辑器模块
│   │   ├── __init__.py
│   │   └── rich_editor.py  # 富文本编辑器实现
│   ├── preview/          # 预览模块
│   │   ├── __init__.py
│   │   └── markdown_preview.py  # Markdown 预览实现
│   ├── ui/               # 界面模块
│   │   ├── __init__.py
│   │   └── main_window.py  # 主窗口实现
│   └── utils/            # 工具模块
│       ├── __init__.py
│       ├── file_handler.py  # 文件处理实现
│       └── markdown_converter.py  # Markdown 转换实现
├── requirements.txt      # 依赖包列表
├── setup.py              # 项目配置文件
└── run.py                # 启动脚本
```

## 依赖项

- PyQt6：用于创建 GUI 界面
- markdown：用于 Markdown 转 HTML
- pyperclip：用于剪贴板操作
- Pillow：用于图像处理

## 开发环境

- Python 3.8+
- 操作系统：Windows、macOS、Linux

## 贡献

欢迎贡献代码、报告问题或提出建议！

## 许可证

本项目采用 MIT 许可证。

## 联系方式

- GitHub：[https://github.com/Yangkunliang/FlowMark](https://github.com/Yangkunliang/FlowMark)
