import re

#работа с html-файлом
f = open ('adygheint.html', 'r', encoding='utf-8')
adyghenews = f.read ()
f.close ()

#поиск текста в коде стр, обработка
regex = '<p>(.*?)</p>'
result = re.findall(regex, adyghenews)

for word in result:
    word = word.lower()
    wordform = word.split()
    for word1 in wordform:
        word1 = word1.strip(' ,.?')

a = set(wordform)

#работа с txt-файлом
f1 = open ('adyghe-unparsed-words.txt', 'r', encoding = 'utf-8')
adyg_wordform = f1.read ()
f1.close ()

for word in adyg_wordform:
    wordform = word.split('\n')

b = set (adyg_wordform)

#поиск встречающихся словоформ
s = a & b

file = open('wordlist', 'w')
file.write(sorted(s))
file.close()
