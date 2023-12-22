def validing(list):
        for elementp in range(9):
            for element in range(elementp+1,9):
                if list[element] == list[elementp]:
                    return False
                    
        return True        
# **********************************************************************************************************************************************************************************
def inputingCol(col):
    while col != "1" and col != "2" and col != "3" and col != "4" and col != "5" and col != "6" and col != "7" and col != "8" and col != "9" :
        print("le nombre incorect")
        col=(input(f"entrer le numero de colon: "))
    return col
def inputingNum(num):
    while num != "1" and num != "2" and num != "3" and num != "4" and num != "5" and num != "6" and num != "7" and num != "8" and num != "9" :
        print("le nombre incorect")
        num=(input(f"entrer le nombre: "))
    return num    
# **********************************************************************************************************************************************************************************

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

# **********************************************************************************************************************************************************************************

                                        ########## 
                                ########## Main ##########  
                                        ########## 
list1=[ 
        ["4","3","5","2","6","9","7","8","1"],
        ["6","8","2","5","7","1","4","9","3"],
        ["1","9","7","8","3","4","5","6","2"],
        ["8","2","6","1","9","5","3","4","7"],
        ["3","7","4","6","8","2","9","1","5"],
        ["9","5","1","7","4","3","6","2","8"],
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
# **********************************************************************************************************************************************************************************
while lign!="stop": 
    conteur=0

    conteur1=0

    conteur2=0

    rowFalse=""

    colFalse=""

    blocFalse=""
    
    forming()
    
    lign=(input("entrer le numero de ligne ou entrer 'stop' pour stop ou entrer 'exit' pour exit: "))
    while lign!="exit" and lign!="stop" and lign != "1" and lign != "2" and lign != "3" and lign != "4" and lign != "5" and lign != "6" and lign != "7" and lign != "8" and lign != "9":
        print("le nombre incorect")
        lign=(input("entrer le numero de ligne ou entrer 'stop' pour stop: "))

    if lign=="exit":
         exit()
    if lign=="stop":
        listRow=[]
        for i in range(9):
                listRow=list1[i]
                if validing(listRow):
                    conteur+=1
                else:
                    rowFalse+= str(i+1)+" ,"
        if conteur == 9:
                print(f"***** row true*****")
        else:
            print(f"***** row false in row {rowFalse}*****")

        # **********************************************************************************************************************************************************************************

        listColonprincipale=[]
        for elementColonPrincipale in range(9):
            listColon=[]
            for elementColonScondaire in range(9):
                listColon.append(list1[elementColonScondaire][elementColonPrincipale])
            listColonprincipale.append(listColon)

        # **********************************************************************************************************************************************************************************

        for i in range(9):
            listColon=listColonprincipale[i]
            if validing(listColon):
                conteur1+=1
            else:
                colFalse+= str(i+1)+" ,"
        if conteur1 == 9:
                print(f"***** col true*****")
        else:
            print(f"***** col false in col {colFalse}*****")

        # **********************************************************************************************************************************************************************************

        listBlocPrincipale=[]
        for i in range(0,9,3):
            for y in range(0,9,3):
                    listBloc=[]
                    for j in range(i,i+3):
                        for x in range(y,y+3):
                            listBloc.append(list1[j][x]) 
                    listBlocPrincipale.append(listBloc)

        # **********************************************************************************************************************************************************************************

        for i in range(9):
            listBloc=listBlocPrincipale[i]
            if validing(listBloc):
                conteur2+=1
            else:
                blocFalse+= str(i+1)+" ,"
        if conteur2 == 9:
                print(f"***** bloc true*****")
        else:
            print(f"***** bloc false in bloc {blocFalse}*****")
        lign = ""
        continue

    col=(input("entrer le numero de colon: "))  
    col=inputingCol(col)  

    num=(input("entrer le nombre: "))
    num=inputingNum(num)

    lign = int(lign)
    col = int(col)
    num = int(num)

    list1[lign-1][col-1]=str(num)




