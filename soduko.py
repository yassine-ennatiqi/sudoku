def validing(list):
        for elementp in range(9):
            for element in range(elementp+1,9):
                if list[element] == list[elementp]:
                    return False
                    
        return True        
def coping(lisst1,lisst2,falsing,cont):
    for i in range(9):
        lisst2=lisst1[i]
        if validing(lisst2):
            cont+=1
        else:
            falsing+= str(i+1)+" ,"

    if cont == 9:
        print(f"***** row true*****")
    else:
        print(f"***** row false in row {falsing}*****")

def inputing(entrer):
    while entrer != "1" and entrer != "2" and entrer != "3" and entrer != "4" and entrer != "5" and entrer != "6" and entrer != "7" and entrer != "8" and entrer != "9" :
        print("le nombre incorect")
        entrer=(input("entrer le numero de entreron: "))
    return entrer    


def forming():
    for i in range(9):
        if i in [0,3,6,9]:
            print("+-----------------------+")
        for j in range(9):
            if j in [0,3,6,9]:
                print("|" , end=" ")
            print( list1[i][j],end=" ")
            if j in [8] :
                print("|" , end=" ")
        print()
        if i in [8]:
            print("+-----------------------+")
                                        ########## 
                                ########## Main ##########  
                                        ########## 
list1=[ 
        ["4","3","5","2","6","9","7","8","1"],
        ["6","8","2","5","7","1","4","9","3"],
        ["1","9","7","8","3","4","5","6","2"],
        ["8","2","6","1","9","5","3","4","7"],
        ["3","7","4","6","8","2","9","1","5"],
        ["9","5","1","7","4","1","6","2","8"],
        ["5","1","9","3","2","6","8","7","4"],
        ["2","4","8","9","5","7","1","3","6"],
        ["7","6","3","4","1","8","2","5","9"],
       ]

conteur=0

conteur1=0

conteur2=0

rowFalse=""

colFalse=""

blocFalse=""

# list1=[]
# for x in range(10):
#     list2=[]
#     for y in range(9):
#         list2.append('-')
#     list1.append(list2)

lign=str(input(r"entrer 'start' pour start: "))

while lign!="start" :
    if lign == "stop":
        exit()
    lign=str(input(r"entrer 'start' pour start or 'stop' pou stoper: "))

while lign!="stop": 
    forming()
    
    lign=(input("entrer le numero de ligne ou entrer 'stop' pour stop: "))
    while lign!="stop" and lign != "1" and lign != "2" and lign != "3" and lign != "4" and lign != "5" and lign != "6" and lign != "7" and lign != "8" and lign != "9":
        print("le nombre incorect")
        lign=(input("entrer le numero de ligne ou entrer 'stop' pour stop: "))

    if lign=="stop":
        break

    col=(input("entrer le numero de colon: "))  
    col=inputing(col)  

    num=(input("entrer le nombre: "))
    inputing(num)

    lign = int(lign)
    col = int(col)
    num = int(num)

    list1[lign-1][col-1]=str(num)
list11=[]
coping(list1,list11,rowFalse,conteur)

listColonprincipale=[]
for elementColonPrincipale in range(9):
    listColon=[]
    for elementColonScondaire in range(9):
        a=list1[elementColonScondaire][elementColonPrincipale]
        listColon.append(a)
    listColonprincipale.append(listColon)

coping(listColonprincipale,listColon,colFalse,conteur1)


list100=[]
for i in range(0,9,3):
    for y in range(0,9,3):
            list200=[]
            for j in range(i,i+3):
                for x in range(y,y+3):
                    list200.append(list1[j][x]) 
            list100.append(list200)

coping(list100,list200,blocFalse,conteur2)




