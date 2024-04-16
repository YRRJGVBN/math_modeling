def worgle(word, Tword):
    zn = []
    w = list(word)
    Tw = list(Tword)

    if len(w) != 5:
        print('Вводите только слова из 5 букв')
        return 0
    else:
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
        return 1

m = 0
Tword = 'барак'

for i in range(6):
    word = input()
    worgle(word, Tword)
    m += 1

    if m == 6:
        print(f'Вы проиграли! Загаданное слово: {Tword}')
        break
    
    if word == Tword and m != 6:
        print(f'Вы отгадали слово {Tword}')
        m = 0
        break