import os
import sys

def parse_file(directory):
    #f = f.open(directory, 'rU')
    #line = f.readline()
    #f.close()
    with open('./test.txt','w') as f:
        writeTo = "blahblah"
        f.write(writeTo)
        
    test = f.closed
    #with open(directory, 'rU') as f:
        #line = f.readline()
        #line = f.readline()
        #f.seek(0)
        #line = f.readline()
    #test = f.closed
    #print(line)
def write_file():
    with open('./test.txt', 'w') as f:
        writeTo = 'blahblah'
        f.write(writeTo)
    test = f.closed

if __name__ == '__main__':
    directory = './cornell_movie_dialogs_corpus/cornell movie-dialogs corpus/movie_lines.txt'
    #parse_file(directory)
    write_file() #works