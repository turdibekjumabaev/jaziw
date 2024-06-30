from typing import List
import re

from .substring import Substring


def tokenize(text: str) -> List[Substring]:
    token_pattern = re.compile(r'\b[\wÁáǴǵÚúŃńÍıÓó-]+\b|[.?!]')
    matches = token_pattern.finditer(text)
    tokens = [Substring(match.start(), match.end(), match.group()) for match in matches]
    return tokens
