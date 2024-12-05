# logic simplest recursion
def find_xmas(xword, row, col):
    parts = 0
    # update position
    if 'M' == xword[row-1][col-1]:
        if 'S' == xword[row+1][col+1]:
            parts+=1
    elif 'S' == xword[row-1][col-1]:
        if 'M' == xword[row+1][col+1]:
            parts += 1
    if 'M' == xword[row-1][col+1]:
        if 'S' == xword[row+1][col-1]:
            parts+=1
    elif 'S' == xword[row-1][col+1]:
        if 'M' == xword[row+1][col-1]:
            parts+=1
    print(parts)
    if parts == 2:
        return True
    else:
        return False
    
        
        
    
# set up
xword = open('day4.txt', "r")
lines = xword.readlines()
for i in range(len(lines)-1):
    lines[i] = lines[i][0:-1]
# print(lines)
count = 0

# loop through xword
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'A':
            
            
                if i-1 < 0:
                    continue
                if j-1 < 0:
                    continue
                if j+1 > len(lines[i])-1:
                    continue
                if i+1 > len(lines)-1:
                    continue
                
                print('valid start', i, j)
                if(find_xmas(lines, i, j)):
                    print(i,j)
                    count+=1
        
print(count)