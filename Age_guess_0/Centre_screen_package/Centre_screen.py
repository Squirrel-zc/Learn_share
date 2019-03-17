def Centre_screen(true,guesslist):

    list_x=[i-true for i in guesslist]

    new_guesslist=[]

    l=[]

    h=[]

    for n in list_x:
        if n<0:
            l.append(n)

        if n>0:
            h.append(n)

    m=max(l)
    new_guesslist.append(m+true)

    s=min(h)
    new_guesslist.append(s+true)

    print(new_guesslist[0],'~',new_guesslist[1])
