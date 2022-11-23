def substitution_text(self, name, value) -> str:
    return f'.. |{name}| replace {value}'
