def fillTheField(field):
    size = int(input('Enter  the size of a field: '))
    for i in range(size):
        field.append(['*'] * size)


def showField(field):
    size = len(field)
    cape = '  '
    for i in range(size):
        cape +=str(i) + ' '
    print(cape)
    for i in range(size):
        str1 = ''
        for j in range(size):
            str1 +=field[i][j] + ' '
        print( i ,str1,' \n')
        
def isWin(field,c,mark ):
    directions = {0 : [], 1: [], 2:[], 3:[], 4:[], 5:[]} #clockwise  4 and 5 are diagonals

    for i in range(1,3):
        if(c[1]-i>=0 and field[c[0]][c[1]-i]==mark):
            directions[3].append([c[0],c[1]-i])
        if(c[0]+i<len(field) and field[c[0]+i][c[1]]==mark):
            directions[2].append([c[0]+i,c[1]])
        if(c[1]+i<len(field) and field[c[0]][c[1]+i]==mark):
            directions[1].append([c[0],c[1]+i])
        if(c[0]-i>=0 and field[c[0]-i][c[1]]==mark):
            directions[0].append([c[0]-i,c[1]])  
             
        if(c[0]-i>=0 and c[1]-i>=0 and field[c[0]-i][c[1]-i]==mark):
            directions[4].append([c[0]-i,c[1]-i])  
        if(c[0]+i< len(field) and c[1]+i<len(field) and field[c[0]+i][c[1]+i]==mark):
            directions[4].append([c[0]+i,c[1]+i])
        
        if(c[0]-i>=0 and c[1]+i<len(field) and field[c[0]-i][c[1]+i]==mark):
            directions[5].append([c[0]-i,c[1]+i])  
        if(c[0]+i< len(field) and c[1]-i>=0 and field[c[0]+i][c[1]-i]==mark):
            directions[5].append([c[0]+i,c[1]-i])
    for i in directions:
        if len(directions[i]) == 2:
            print(directions[i])
            return True

    return False

def startgame(field):
    isNoWinner = True
    numTurn = 1
    coords = ''
    while(isNoWinner):
        coords = input('Enter coordinates, using space: ')
        mark = 'x'
        if(numTurn%2==0):
            mark = 'o'
        
        inputCoords = coords.split(' ')
        actualCoords = [int(inputCoords[0]),int(inputCoords[1])]
        
        field[actualCoords[0]][actualCoords[1]] = mark
        isNoWinner = not isWin(field,actualCoords,mark)
        showField(field)
        if(not isNoWinner):
            print('Player',mark,'won on turn', numTurn)
            break
        
        numTurn+=1


def main():
    field = [] 
    fillTheField(field)
    showField(field)
    startgame(field)
    
main()