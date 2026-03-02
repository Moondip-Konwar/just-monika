import os
import sys
import random

def get_random_case(s):
    return "".join(random.choice([c.upper(), c.lower()]) for c in s)

def tokenize(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    raw_words = [w.strip() for w in content.split(',') if w.strip()]
    
    valid_bases = {'just', 'monika'}
    commands = []

    # Mapping swapped to prioritize Monika for common BF operations
    mapping = {
        # Monika variations (Most common BF commands)
        'MONIKA': '+',
        'monika': '-',
        'Monika': '>',
        'mOnIkA': '<',
        # Just variations (Less common BF commands)
        'JUST': '.',
        'just': '[',
        'Just': ']',
        'jUsT': ','
    }

    for word in raw_words:
        if word.lower() not in valid_bases:
            os.remove(file_path)
            while True:
                print(f"{get_random_case('Just')} {get_random_case('Monika')}")
        
        if word in mapping:
            commands.append(mapping[word])

    return commands
