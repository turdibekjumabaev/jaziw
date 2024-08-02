
def normalize(text: str) -> str:
    lines = text.splitlines()
    stripped_lines = [line.strip() for line in lines if
                      line.strip()]
    cleaned_text = ' '.join(stripped_lines)
    return cleaned_text
