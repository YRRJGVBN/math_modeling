def morphy(word):
    if len(word) != 5:
        return 0
    else:
        return 1

def worgle(word, Tword):
    zn = []
    w = list(word)
    Tw = list(Tword)

    for i in w:
        if i in Tw:
            zn.append('$')
        else:
            zn.append('X')

    for i in range(5):
        if w[i] == Tw[i]:
            zn[i] = '0'
    r = ''.join(zn)
    print(word)
    print(r)

m = 0
Tword = 'барак'

while 1:
    word = input()
    if morphy(word):
        worgle(word, Tword)
        m += 1
    else:
        print('Вводите только слова из 5 букв')

    if m == 6:
        print(f'Вы проиграли! Загаданное слово: {Tword}')
        break
    
    if word == Tword and m != 6:
        print(f'Вы отгадали слово {Tword}')
        m = 0
        break