##n='ocean'
##m='academy'
##if n=='Ocean':
##    print(n)
##elif m=='academy':
##    print(m)
##else:
##    print(n+m)
##
##n=6
##m=0
##for i in range(20):
##    m+=1
##    if i ==n:
##        print("stop",m)
##        break
##    else:
##        continue
##    print("It goes on")
##i = 1
##while True:
##    if i%2 == 0:
##        break
##    print(i)
##    i += 2
##x = 10
##y = 50
##if (x ** 2 == 100 and y < 100):
##     print(x, y)
##print(3*1**3)
##
##if (9 < 0) and (0 < -9):
##    print("hello")
##elif (9 > 0) or False:
##    print("good")
##else:
##    print("bad")


n=6
m=3
count=0
for i in range(1,10000,2):
    if count == 6:
        n=count+i
        count+=m
    else:
        print(count)
        break
