# logic simplest recursion
def find_xmas(xword, shape, row, col, dir):
    if shape == '':
        return True
    
    # update position
    if 'u' in dir:
        row -= 1
    if 'l' in dir:
        col -= 1
    if 'r' in dir:
        col += 1
    if 'd' in dir:
        row += 1
    # check new position
    # print(xword[row][col], row, col, shape[0], dir)
    if xword[row][col] == shape[0]:
        return find_xmas(xword, shape[1:], row, col, dir)
    else:
        return False
    
        
        
# set up
xword = open('day4.txt', "r")
lines = xword.readlines()
for i in range(len(lines)-1):
    lines[i] = lines[i][0:-1]
# print(lines)
count = 0
dir = ['ul','u','ur','r','dr','d','dl','l']

# loop through xword
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            
            for d in dir:
                if 'u' in d and i-3 < 0:
                    continue
                elif 'l' in d and j-3 < 0:
                    continue
                elif 'r' in d and j+3 > len(lines[i])-1:
                    continue
                elif 'd' in d and i+3 > len(lines)-1:
                    continue
                # print('valid start', i, j, d)
                if(find_xmas(lines, 'MAS', i, j, d)):
                    # print(i,j,d)
                    count+=1
        
print(count)