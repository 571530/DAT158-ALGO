import time

def lcs_recursive(s1, s2, x = None, y = None):
    if x == None or y == None:
        return lcs_recursive(s1, s2, len(s1) - 1, len(s2) - 1)

    if x == -1 or y == -1:
        return 0
    elif s1[x] == s2[y]:
        return 1 + lcs_recursive(s1, s2, x - 1, y - 1)
    else:
        return max(lcs_recursive(s1, s2, x-1, y), lcs_recursive(s1, s2, x, y-1))

def lcs_dynamic(s1, s2):
    n = len(s1)
    m = len(s2)

    L = [[0]*(m + 1) for i in range(n + 1)] 

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
                
    return L[n][m]

t1 = 'babbababbabbababbabbababbabbababbaabb'
t2 = 'bbabbaaabbbabbaaabbbabbaaabbbabbababa'

before = time.time()
res = lcs_recursive(t1, t2)
after = time.time()
print('{} s with recursive'.format(after-before)) # 3.7 s

before = time.time()
print(lcs_dynamic(t1, t2))
after = time.time()
print('{} s with dynamic'.format(after-before)) # 0.001 s


print(len(t1)) # 37
print(len(t2)) # 37