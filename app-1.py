from lazy_streams import stream

# https://github.com/brettschneider/python_lazy_streams/blob/master/README.md

# a. inspirowane strumieniami z Java

# b. sa lazy evaluated

# c. nie zmieniaja sekwencji na ktorej dzialaja

# d. wprowadzaja dwie kategorie operacji: terminal operations oraz non-terminal operations
#    terminal operations powoduje wykonanie operacji na strumieniu i zwracaja wynik
#    non-terminal operations zwracaja LazyStream ktory mozna przetwarzac dalej

numbers = range(1, 10)
s1 = stream(numbers)

res1 = s1.reverse().filter(lambda x: x % 2 == 0).map(lambda x: x ** 2).last_or_else(-1)
print(res1)

# wykaz operacji terminalnych
s2 = stream(numbers)
res2 = s2.filter(lambda x: x > 2).to_string()
print(res2)

res3 = s2.filter(lambda x: x > 2).to_string('...')  # wypisanie z oddzieleniem za pomoca separatora
print(res3)

res4 = s2.filter(lambda x: x > 2).first_or_else(-1)
print(res4)

res5 = s2.filter(lambda x: x > 2).reduce(lambda x, y: min(x, y))
print(res5)

res6 = s2.filter(lambda x: x > 2).min()
print(res6)

res7 = s2.filter(lambda x: x > 2).max()
print(res7)

res8 = s2.filter(lambda x: x > 2).size()
print(res8)

res9 = s2.filter(lambda x: x > 2).to_list()
print(res9)

# wykaz operacji nieterminalnych

# pobiera 2 pierwsze elementy
res10 = s2.filter(lambda x: x > 2).take(2).to_list()
print(res10)

# splaszcza elementy z list zagniezdzonych do jednej listy
l1 = [1, 2, 3, [4, 5, 6, 7, [8, 9]]]
res11 = stream(l1).flatten().to_list()
print(res11)

# sortowanie + for_each
print('SORTED')
stream(range(100, 120)).filter(lambda x: x > 2).sort(key=lambda x: x % 10, reverse=True).for_each(lambda x: print(x))

