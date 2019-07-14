import zlib
import json
import re
from nltk.corpus import stopwords
import nltk



def collect_words():
    stopwords_list = stopwords.words('english')
    #movie_path = './text_separated/movie_lines/m{number}_all_lines.txt'.format(number=i)
    words_tally = {}
    bigrams_tally= {}
    #regex = r"[a-z]+['][a-z]+|[a-z]+"
    i=0
    while True:
        try:
            with open('./text_separated/movie_lines/m{number}_all_lines.txt'.format(number=0), 'r') as f:
                while True:
                    line = f.readline().lower()
                    #line = line.lower().split()
                    if line == '':
                        i+=1
                        break
                    #reg_groups = re.findall(regex,line)
                    tokens = nltk.word_tokenize(line)
                    bigram_groups = [nltk.bigrams(tokens)]
                    for word in tokens:
                        if word in words_tally:
                            words_tally[word] += 1
                        elif word in stopwords_list:
                            continue
                        else:
                            words_tally[word] = 1
                    for bigram in bigram_groups:
                        if bigram in bigrams_tally:
                            bigrams_tally[bigram] += 1
                        else:
                            bigrams_tally[bigram] = 1
            #if i>616:
                break
        except FileNotFoundError:
            break
    analyze_dict(words_tally, bigrams_tally)
    #generate_json(words_tally, path='./text_separated/data/movies_word_tally.json')

def analyze_dict(words_dict={}, bigrams_dict={}):
    words_list = sorted(words_dict.items(), key=lambda x: x[1],reverse=True)
    bigrams_list = sorted(bigrams_dict.items(), key=lambda x: x[1],reverse=True)
    num_nonstop = len(words_list) #list of unique nonstopwords
    top_hundred_words = [x for x in words_list[0:100]] #list of top 100 occurring words
    top_fifty_bigrams = [x for x in bigrams_list[0:100]]
    
    return

def generate_json(words_dict, path=''):
    with open(path, 'w') as g:
        json.dump(words_dict,g)

if __name__ == '__main__':
    collect_words()