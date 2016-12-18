Шаблоны

#открытие текста
def reading ():
    f = open ('something.txt', 'r', encoding='utf-8')
    text = f.read ()
    f.close ()
    return text

#запись в новый текстовый файл
def pechat (new):
    f = open ('something.txt','w',encoding='utf-8')
    f.write (new)
    f.close ()

#концовка
if __name__ == '__main__' :
    main ()

#обработка текста
 text = text.lower()
 txt = text.split()
 for word in txt:
     word = word.strip(' ,.?')
