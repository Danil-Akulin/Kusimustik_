from random import shuffle

print('Опрос расчитан на двух людей')
print('Опрос на тему Экология')
b=[]
qq=[]
gh=[]
for one in range(0, 1):
    a=input('Ввидите имя человека ')
    b.append(a)


#def voprosi():
 #   for i in range(1):
  #      for l in range(1, 16):
 #           gh.append(l)
 #       shuffle(gh)
 #   return gh

    mas4 = [0]
    mas5 = []
    fail = open("voprosi.txt", "r", encoding='UTF-8')
    mas1 = []
    mas2 = []
    for line in fail:
        n = line.find(",")
        mas1.append(line[0:n].strip())
        mas2.append(str(line[n+1:len(line)].strip()))
    fail.close()
    print(mas1)
    print(mas2)

    del mas1[1::2]
    del mas2[1::2]

    print(mas1)
    print(mas2)
    shuffle(mas1)
    del mas1[6:16]
    print(mas1)
    if mas1:
        print(mas1[0])
        a=input('да/нет ')
        if a!='да':
            print('неправильно)')
        else:
            print('правильно')
            mas4[0]+=1

    if mas1:
        print(mas1[1])
        a=input('да/нет ')
        if a!='да':
            print('неправильно(')
        else:
            print('правильно)')
            mas4[0]+=1

    if mas1:
        print(mas1[2])
        a=input('да/нет ')
        if a!='да':
            print('правильно)')
            mas4[0]+=1
        else:
            print('неправильно(')

    if mas1:
        print(mas1[3])
        a=input('да/нет ')
        if a!='да':
            print('неправильно)')
        else:
            print('правильно(')
            mas4[0]+=1

    if mas1:
        print(mas1[4])
        a=input('да/нет ')
        if a!='да':
            print('правильно)')
            mas4[0]+=1
        else:
            print('неправильно(')
    print('Поздравляю дорогой', b, 'вы ответили правильно на', mas4[0], 'вопроса)')
    print(mas4)
    if mas4[0] >= int('3'):
        print('вы прошли')

        fail = open("oiged.txt", "a", encoding='UTF-8')
        fail.write('Прошёл\n')
        fail.write(b[0])
        fail.close()

    if mas4[0] <= int('2'):
        print('вы не прошли')

        fail = open("valed.txt", "a", encoding='UTF-8')
        fail.write('не Прошёл\n')
        fail.write(b[0])
        fail.close()

for one in range(0, 1):
    q=input('Ввидите имя человека ')
    qq.append(q)


    mas4 = [0]
    mas5 = []
    fail = open("voprosi.txt", "r", encoding='UTF-8')
    mas1 = []
    mas2 = []
    for line in fail:
        n = line.find(",")
        mas1.append(line[0:n].strip())
        mas2.append(str(line[n+1:len(line)].strip()))
    fail.close()
    print(mas1)
    print(mas2)

    del mas1[1::2]
    del mas2[1::2]

    print(mas1)
    print(mas2)
    shuffle(mas1)
    del mas1[6:16]
    print(mas1)
    if mas1:
        print(mas1[0])
        q=input('да/нет ')
        if q!='да':
            print('неправильно)')
        else:
            print('правильно')
            mas4[0]+=1

    if mas1:
        print(mas1[1])
        q=input('да/нет ')
        if q!='да':
            print('неправильно(')
        else:
            print('правильно)')
            mas4[0]+=1

    if mas1:
        print(mas1[2])
        q=input('да/нет ')
        if q!='да':
            print('правильно)')
            mas4[0]+=1
        else:
            print('неправильно(')

    if mas1:
        print(mas1[3])
        q=input('да/нет ')
        if q!='да':
            print('неправильно)')
        else:
            print('правильно(')
            mas4[0]+=1

    if mas1:
        print(mas1[4])
        q=input('да/нет ')
        if q!='да':
            print('правильно)')
            mas4[0]+=1
        else:
            print('неправильно(')
    print('Поздравляю дорогой', qq, 'вы ответили правильно на', mas4[0], 'вопроса)')
    print(mas4)
    if mas4[0] >= int('3'):
        print('вы прошли')

        fail = open("oiged.txt", "a", encoding='UTF-8')
        fail.write('Прошёл\n')
        fail.write(qq[0])
        fail.close()

    if mas4[0] <= int('2'):
        print('вы не прошли')

        fail = open("valed.txt", "a", encoding='UTF-8')
        fail.write('не Прошёл\n')
        fail.write(qq[0])
        fail.close()