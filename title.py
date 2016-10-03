#взять код страницы из вики, извлечь заголовок, взять адрес картинки
#извлечь все слова, написанные курсивом, поместить в словарь,
#где ключ - слово, а значение - номер среди всех слов, написанных курсивом,
#результат записать в файл

import re

def reading ():
    s = ''
    f = open ('frogs.html', 'r', encoding='utf-8')
    a = f.read ()
    f.close ()
    return a

def zap(s):
    f = open ('frogs.txt', 'w', encoding='utf-8')
    f.write (s)
    f.close ()

def poisk(a):
    if '>Лягушки — Википедия<' in a:
        m = a.find('>Лягушки — Википедия<')
        regex = 'class="firstHeading" lang="ru">(.*?)</h1'
        res = re.search(regex, a)
        if res:
            s = res.group (1)
            zap (s)

def main ():
    a = reading ()
    poisk(a)

    
if __name__ == '__main__' :
    main ()    
