a=[]
b=[]
for i in range(3):
    a.append([])
    b.append([])
    for j in range(3):
        a[i].append("_")
        b[i].append("_")
name1=input("Enter player1 name: ")
name2=input("Enter player2 name: ")
i=0
def matrix():
    for i in range(3):
        for j in range(3):
            print(b[i][j],end=" ")
        print(" ")
while(i<9):
    if(i%2==0):
        print("Player1",name1,"your mark(x): ")
        c=int(input("Enter your move(1 to 9)"))
        if(c==1):
            if(b[0][0]!="X" and b[0][0]!="O"):
                b[0][0]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==2):
            if(b[0][1]!="X" and b[0][1]!="O"):
                b[0][1]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==3):
            if(b[0][2]!="X" and b[0][2]!="O"):
                b[0][2]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==4):
            if(b[1][0]!="X" and b[1][0]!="O"):
                b[1][0]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==5):
            if(b[1][1]!="X" and b[1][1]!="O"):
                b[1][1]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==6):
            if(b[1][2]!="X" and b[1][2]!="O"):
                b[1][2]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==7):
            if(b[2][0]!="X" and b[2][0]!="O"):
                b[2][0]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==8):
            if(b[2][1]!="X" and b[2][1]!="O"):
                b[2][1]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c==9):
            if(b[2][2]!="X" and b[2][2]!="O"):
                b[2][2]="X"
            else:
                print("Already entered in this place")
                i-=1
        elif(c<0 and c>9):
            print("enter numbers between 1 to 9 only")
        matrix()
        i+=1 
    elif(i%2!=0):
        print("Player2",name2,"your mark(O): ")
        c=int(input("Enter your move(1 to 9)"))
        if(c>=1 and c<=9):
            if(c==1):
                if(b[0][0]!="X" and b[0][0]!="O"):
                    b[0][0]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==2):
                if(b[0][1]!="X" and b[0][1]!="O"):
                    b[0][1]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==3):
                if(b[0][2]!="X" and b[0][2]!="O"):
                    b[0][2]="O"   
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==4):
                if(b[1][0]!="X" and b[1][0]!="O"):
                    b[1][0]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==5):
                if(b[1][1]!="X" and b[1][1]!="O"):
                    b[1][1]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==6):
                if(b[1][2]!="X" and b[1][2]!="O"):
                    b[1][2]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==7):
                if(b[2][0]!="X" and b[2][0]!="O"):
                    b[2][0]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==8):
                if(b[2][1]!="X" and b[2][1]!="O"):
                    b[2][1]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c==9):
                if(b[2][2]!="X" and b[2][2]!="O"):
                    b[2][2]="O"
                else:
                    print("Already entered in this place")
                    i-=1
            elif(c<0 and c>9):
                print("enter numbers between 1 to 9 only")
        else:
            print("invalid input")
        matrix()
        i+=1
    if(b[0][0]=="X"and b[0][1]=="X"and b[0][2]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[1][0]=="X"and b[1][1]=="X"and b[1][2]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[2][0]=="X"and b[2][1]=="X"and b[2][2]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[0][0]=="X"and b[1][0]=="X"and b[2][0]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[0][1]=="X"and b[1][1]=="X"and b[2][1]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[0][2]=="X"and b[1][2]=="X"and b[2][2]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[0][0]=="X"and b[1][1]=="X"and b[2][2]=="X"):
        print(name1,"Player1 is Winner")
        break
    elif(b[0][2]=="X"and b[1][1]=="X"and b[2][0]=="X"):
        print(name1,"Player1 is Winner")
        break

    if(b[0][0]=="O"and b[0][1]=="O"and b[0][2]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[1][0]=="O"and b[1][1]=="O"and b[1][2]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[2][0]=="O"and b[2][1]=="O"and b[2][2]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[0][0]=="O"and b[1][0]=="O"and b[2][0]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[0][1]=="O"and b[1][1]=="O"and b[2][1]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[0][2]=="O"and b[1][2]=="O"and b[2][2]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[0][0]=="O"and b[1][1]=="O"and b[2][2]=="O"):
        print(name2,"Player2 is Winner")
        break
    elif(b[0][2]=="O"and b[1][1]=="O"and b[2][0]=="O"):
        print(name2,"Player2 is Winner")
        break
    if(i==9):
        print("Game became draw")


    
    
