import icecream
import string

def punctuation_remover(input): #denna funktionen tar en sträng som input och returnerar samma sträng fast med alla skiljetecken bortagna
    translator = str.maketrans('', '', string.punctuation) #denna raden skapar ett translate table där man ersätter tomma spaces med tomma spaces och tar bort alla skiljetecken. string.punctuation är bara en lista med alla skiljetecken som jag fick från packetet string
    return input.translate(translator)

def text_stats(input):
    word_count = 0
    word_freq = {}
    input_file = open(input, 'r')

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
    
    common_words = list(word_freq.items())
    common_words = common_words.sort()
    
    output = {'word count' : word_count, 'unique word count' : unique_word_count, 'word frequency' : word_freq}
    
    return output
    
    
stats = text_stats('input.txt')

print(stats)