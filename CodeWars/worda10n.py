import re

def abbreviate(text):
    def replace_word(match):
        word = match.group(0)
        if len(word) >= 4:
            # Primer carácter + número de caracteres intermedios + último carácter
            return f"{word[0]}{len(word) - 2}{word[-1]}"
        return word

    # re.sub busca todas las palabras compuestas puramente por letras
    return re.sub(r'[a-zA-Z]+', replace_word, text)