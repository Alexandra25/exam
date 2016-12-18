import re
import os

def processing():
    f = open('zamok.txt', 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def search(text):
    res = re.findall('[А-ЯЁ]\. [А-ЯЁ][а-яё]+', text)
    for name in res:
        print(name)
    print('\n')

def names(text):
    regex = ['[А-ЯЁ]\. [А-ЯЁ]\. [А-ЯЁ][а-яё]+', '[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ (?:[А-ЯЁ][а-яё]+)?']
    for reg in regex:
        res = re.findall(reg, text)
        for r in res:
            print(r)

def files(text):
    d = {}
    names = []
    regex = ['([А-ЯЁ][^\.\\n]*?([А-ЯЁ]\. [А-ЯЁ]\. ([А-ЯЁ][а-яё]+))[^\.\\n]*?\.)', '([А-ЯЁ][^\.\\n]*?([А-ЯЁ][а-яё]+ ([А-ЯЁ][а-яё]+))[^\.\\n]*?\.)']
    for reg in regex:
        res = re.findall(reg, text)
        for r in res:
            if r[2] in d:
                d[r[2]].append(r[0])
            else:
                d[r[2]] = [(r[0])]
            if r[2] not in names:
                names.append(r[2])
                diract = 'C:\\' + r[2]
                os.mkdir(diract)
                diract = diract + '\\' + r[1] + '.txt'
                f = open(diract, 'a', encoding = 'utf-8')
                for sent in d[r[2]]:
                    f.write(sent)
                    f.write('\n')
                f.close()
            else:
                diract = 'C:\\' + r[2] + '\\' + r[1] + '.txt'
                f = open(diract, 'a', encoding = 'utf-8')
                for sent in d[r[2]]:
                    f.write(sent)
                    f.write('\n')
                f.close()

def main():
    text = processing()
    search(text)
    names(text)
    files(text)

if __name__ == '__main__':
    main()
