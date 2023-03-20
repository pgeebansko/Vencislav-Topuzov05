next = True
b = list()
while next == True:
    next = input('Da se vuvede li chislo da ili ne')
    if next == 'OK':
        a = int(input('Vuvedete chislo'))
        b.append(a)
    else:
        next = False

    print(b)