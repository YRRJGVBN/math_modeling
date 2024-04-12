def worgle(word, Tword):
    zn = []
    w = list(word)
    Tw = list(Tword)
    
    for i in w:
        if i in Tw:
            zn.append('#')
        else:
            zn.append('x')

    for i in range(5):
        if w[i] == Tw[i]:
            zn[i] == '0'

    print(zn)


word = 'табак'
Tword = 'барак'
worgle(word, Tword)