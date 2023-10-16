import icecream
import string
from pathlib import Path

def punctuation_remover(input): #denna funktionen tar en sträng som input och returnerar samma sträng fast med alla skiljetecken bortagna
    translator = str.maketrans('', '', string.punctuation) #denna raden skapar ett translate table där man ersätter tomma spaces med tomma spaces och tar bort alla skiljetecken. string.punctuation är bara en lista med alla skiljetecken som jag fick från packetet string
    return input.translate(translator)

def text_stats(input, nr_common_words, nr_uncommon_words):
    word_count = 0
    word_freq = {}
    THIS_FOLDER = Path(__file__).parent.resolve()
    input_file = open(THIS_FOLDER / input, 'r')

    for line in input_file:
        line = punctuation_remover(line)
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
    
    
stats = text_stats('cooltext.txt', 5, 5)

print(stats)