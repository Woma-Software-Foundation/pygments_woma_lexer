# A Pygments Lexer for the Woma Programming Language
[![PyPI](https://img.shields.io/pypi/v/pygments-woma-lexer?style=for-the-badge)](https://pypi.org/project/pygments-woma-lexer/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pygments-woma-lexer?style=for-the-badge)](https://pypi.org/project/pygments-woma-lexer/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/pygments-woma-lexer?style=for-the-badge)](https://pypi.org/project/pygments-woma-lexer/)<p align="right">![logo](https://raw.githubusercontent.com/rjdbcm/Aspidites/main/docs/_static/aspidites_logo_45_45.png)</p>
----------------------------------------------------
# How to Use
Just add the following lines to your docs/conf.py
```python
from pygments_woma_lexer import WomaLexer
from sphinx.highlighting import lexers
lexers.update(woma=WomaLexer())
```
