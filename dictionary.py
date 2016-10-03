import re

def reading ():
    s = ''
    f = open ('frogs.html', 'r', encoding='utf-8')
    a = f.read ()
    f.close ()
    return a

def italics(a):
    dict_it = {}
    regex = '<i>(?:<.*?>)?(.*?)(?:<.*?>)?</i>'
    res = re.findall(regex, a)
    n = 1
    for r in res:
        dict_it[r] = n
        n += 1
    return dict_it

def print_dict(dict_it):
    f = open('dictionary.txt', 'w', encoding = 'utf-8')
    for word in dict_it:
        f.write(word+' '+str(dict_it[word])+'\n')
    f.close()

def zap(s):
    f = open ('frogs.txt', 'w', encoding='utf-8')
    f.write (s)
    f.close ()

def main ():
    a = reading ()
    dict_it = italics(a)
    print_dict(dict_it)
    
if __name__ == '__main__' :
    main ()    
