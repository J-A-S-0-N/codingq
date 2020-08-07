def backward_string(st):
    lstr = list(st)
    lstrbu = list(st)
    a = 0
    c = 2
    lstr[a] = lstr[c]
    lstrbu[c] = lstrbu[a]
    print(lstr)




backward_string('val')# == 'lav'
