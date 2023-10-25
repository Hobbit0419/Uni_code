<<<<<<< HEAD
import string
from pathlib import Path

def text_stats(input, nr_common_words, nr_uncommon_words):
    word_count = 0
    word_freq = {}
    THIS_FOLDER = Path(__file__).parent.resolve()
    input_file = open(THIS_FOLDER / input, 'r')

    for line in input_file:
        words = line.split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:              
                word_freq[word] = 1
            word_count += 1
    
    unique_word_count = len(word_freq.keys())
    
    words = list(word_freq.items())
    words.sort(key=lambda a: a[1], reverse=True)
    common_words = words[:nr_common_words]
    uncommon_words = words[len(words) - 1 - nr_uncommon_words:]
    
    output = {'word count' : word_count, 'unique word count' : unique_word_count, 'word frequency' : word_freq, 'most common words' : common_words, 'least common words' : uncommon_words}
    
    return output

def input_printer(input_file):
    place = 'holder'
=======
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

>>>>>>> 9e793a96f671cad7af41ad8ce0c897c63a6e8fdf
