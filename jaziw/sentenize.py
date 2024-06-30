from typing import List
import re

from .substring import Substring


def sentenize(text: str) -> List[Substring]:
    sentence_endings = re.compile(r'([.?!])\s+')
    sentences = []
    start = 0
    for match in sentence_endings.finditer(text):
        end = match.end() - 1
        sentences.append(Substring(start, end, text[start:end]))
        start = match.end()
    if start < len(text):
        sentences.append(Substring(start, len(text), text[start:]))
    return sentences
