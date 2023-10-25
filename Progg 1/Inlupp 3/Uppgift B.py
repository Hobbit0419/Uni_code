import icecream
import string
from pathlib import Path
import keyword
import re

def program_stats(input):
    word_freq = {}
    THIS_FOLDER = Path(__file__).parent.resolve()
    input_file = open(THIS_FOLDER / input, 'r', encoding = 'utf-8')
    line_number = 1

    for line in input_file:
        print(f'{line_number} {line}')
        line = re.sub(r'#.*$', '', line)
        words = re.findall(r'[a-zA-ZåäöÅÄÖ]+', line)
        for word in words:
            if word in word_freq and not keyword.iskeyword(word):
                word_freq[word].append(line_number)
            elif not keyword.iskeyword(word):              
                word_freq[word] = [line_number]
        line_number += 1
    print('\n Referenslista:')
    for key in word_freq:
        print(f'{key} {word_freq[key]}')
        
   
    
program_stats('bokstavsfrekvens.py')

