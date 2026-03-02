import os
import re
import sys

def tokenize(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    words = re.findall(r'\b\w+\b', content)
    valid_words = {'just', 'monika'}
    tokens = []

    for word in words:
        if word.lower() not in valid_words:
            os.remove(file_path)
            print("Just Monika")
            sys.exit(0)
        tokens.append(word.lower())

    if len(tokens) % 3 != 0:
        return tokens[:-(len(tokens) % 3)]
    return tokens

def get_commands(tokens):
    commands = []
    mapping = {
        ('just', 'just', 'just'): '>',
        ('just', 'just', 'monika'): '<',
        ('just', 'monika', 'just'): '+',
        ('just', 'monika', 'monika'): '-',
        ('monika', 'just', 'just'): '.',
        ('monika', 'just', 'monika'): ',',
        ('monika', 'monika', 'just'): '[',
        ('monika', 'monika', 'monika'): ']'
    }

    for i in range(0, len(tokens), 3):
        triple = tuple(tokens[i:i+3])
        if triple in mapping:
            commands.append(mapping[triple])
    
    return commands
