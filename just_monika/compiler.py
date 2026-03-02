def bf_to_monika(bf_code):
    mapping = {
        '+': 'MONIKA',
        '-': 'monika',
        '>': 'Monika',
        '<': 'mOnIkA',
        '.': 'JUST',
        ',': 'jUsT',
        '[': 'just',
        ']': 'Just'
    }
    return ", ".join(mapping[c] for c in bf_code if c in mapping)

def monika_to_bf(monika_code):
    mapping = {
        'MONIKA': '+',
        'monika': '-',
        'Monika': '>',
        'mOnIkA': '<',
        'JUST': '.',
        'jUsT': ',',
        'just': '[',
        'Just': ']'
    }
    words = [w.strip() for w in monika_code.split(',') if w.strip()]
    return "".join(mapping.get(w, '') for w in words)
