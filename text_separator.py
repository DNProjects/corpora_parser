import os
import sys
import re

def separate_lines(directory, type=''):
    with open(directory, 'r') as f:
        i = 0
        while True:
            lineToWrite = f.readline()
            with open('./{folder}/m{number}.txt'.format(folder=type,number=i), 'w') as g:
                while True:
                    if 'm{number}'.format(number=i) in lineToWrite:
                        g.write(lineToWrite)
                        lineToWrite = f.readline()
                    else:
                        i += 1
                        break
            if lineToWrite == '':
                break

def create_corpus(corpus=''):
    #case_switch = {
        #'cornell': '\D[\d]+ \W+ \w+ \W+'
        #''
    #}
    regex = ''
    if corpus is 'cornell':
        regex = r'(\+\+\+\$\+\+\+) ' #a string with a 'r' prefix is a raw string and treats backslashes as literal characters
    pattern = re.compile(regex)
    i = 0
    #with open('./text_separated/separated_lines/m617.txt', 'r') as test:
        #read = test.readline()
    try:
        while True:
            #open(./blah/m{number}.txt'.format(number=i), 'r')
            with open('./text_separated/separated_lines/m{number}.txt'.format(number=i), 'r') as f:
                with open('./text_separated/movie_lines/m{number}_all_lines.txt'.format(number=i), 'w') as g:
                    while True:
                        line = f.readline()
                        split_line = re.split(regex,line)
                        lineToWrite = split_line[len(split_line)-1]
                        g.write(lineToWrite)
                        if line == '':
                            i += 1
                            break
            if i>616:
                break
    except FileNotFoundError:
        return

def evalFormat():
    i=0
    try:
        while True:
            with open('./text_separated/movie_lines/m{number}.txt'.format(number=i), 'r') as f:
                line = f.readline()
                if '+++$+++' in line:
                    return False
                if line == '':
                    i += 1
                    break
            if i>616:
                break
        return True
    except FileNotFoundError:
        return True
if __name__ == '__main__':
    movie_lines = './cornell_movie_dialogs_corpus/cornell movie-dialogs corpus/movie_lines.txt'
    movie_conversations = './cornell_movie_dialogs_corpus/cornell movie-dialogs corpus/movie_conversations.txt'
    text_separated = './text_separated'
    #separate_lines(movie_lines, type='separated_lines')
    #separate_lines(movie_conversations, type='separated_conversation')
    create_corpus('cornell')
    test = evalFormat()
    #print(test)
