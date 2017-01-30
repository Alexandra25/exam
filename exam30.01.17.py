import re
import os

#файлы с субтитрами
def reading ():
    a = ''
    files = os.listdir()
    for file in files:
        if file.startswith('Sherlock'):
            f = open (file, 'r', encoding='utf-8')
            t = f.read ()
            a += t
            f.close ()
    return a

#файлы с пересказом
def reading_plot():
    f = open ('plot.txt', 'r', encoding='utf-8')
    plot = f.read ()
    f.close ()
    words = plot.split()
    for i,word in enumerate(words):
        words[i] = word.strip(',.?!\'":;()«»—')
    return words

#все размеченные слова в words.txt

#поиск имен и фамилий
def mystemn():
    os.system('mystem.exe subs.txt words.txt -in')
    f = open ('words.txt', 'r', encoding='utf-8') 
    w = f.readlines ()
    f.close ()
    names = []
    for word in w:
        if ',имя,' in word or ',фам,' in word:
            regex = '(.*?){'
            name = re.search(regex, word)
            names.append(name.group(1))
    return names

#отсортированный результат
def print_names (n):
    n = list(n)
    for i,name in enumerate(n):
        n[i] = name.lower()
    n.sort()
    for name in n:
        print(name)

def zap(s):
    f = open ('subs.txt', 'w', encoding='utf-8')
    f.write (s)
    f.close ()

def main():
    subs = reading ()
    zap(subs)
    names = mystemn ()
    names = set(names)
    words_plot = reading_plot ()
    words_plot = set(words_plot)
    names_texts = names & words_plot
    print_names(names_texts)
    
if __name__ == '__main__' :
    main ()

