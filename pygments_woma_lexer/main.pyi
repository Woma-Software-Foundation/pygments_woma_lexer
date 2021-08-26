from pygments.lexer import RegexLexer
from typing import Any

class WomaLexer(RegexLexer):
    name: str
    mimetype: str
    def __init__(self, startinline: bool = ...) -> None: ...
    def innerstring_rules(ttype) -> None: ...
    def fstring_rules(ttype) -> None: ...
    tokens: Any
