from setuptools import setup, find_packages

setup(
    name="FlowMark",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6",
        "markdown",
        "pyperclip",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "flowmark=flowmark.main:main"
        ]
    }
)
