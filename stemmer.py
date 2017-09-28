import re

rule1 = r'pen([cdjz])(.*)'

def stemmer(word, pattern):
    ganti = ''
    matched = re.match(rule1, word)
    if matched:
        return matched.group(1) + matched.group(2)
    return word

words = ['dimakan', 'dibuat', 'dirasakan', 'penodong', 'pendahulu', 'penjarah', 'pencuri', 'penziarah']

for word in words:
    print(stemmer(word, rule1))