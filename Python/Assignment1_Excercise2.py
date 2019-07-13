# Importing numpy library.
import numpy as np

# Defining match function.
# 's1' is first string.
# 's2' is second string.
def match(s1,s2):
    if((len(s1) == 0) or (len(s2) == 0)):
        return False
    matrix = np.zeros((len(s1)+1 ,len(s2)+1), dtype=bool)
    matrix[0][0] = True
    
    for i in range(0,len(s2)):
        if ((s2[i] == '*') and matrix[0][i-1]):
            matrix[0][i+1]= True
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if((s2[j] == '.') or (s2[j] == s1[i])):
                matrix[i+1][j+1] = matrix[i][j]
            elif (s2[j] == '*'):
                if ((s2[j-1] != s1[i]) and s2[j-1] != '.'):
                    matrix[i+1][j+1] = matrix[i+1][j-1]
                else:
                    matrix[i+1][j+1] = matrix[i+1][j-1] or matrix[i+1][j] or matrix[i][j+1]
    
    return matrix[len(s1)][len(s2)]            
    

# Calling Function with parameters.    
match("aab", "c*a*b")
# Output is : True
