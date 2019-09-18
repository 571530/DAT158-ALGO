Truls Martinsen, Heine Fjeldberg

## Problem 1
text "aaabaadaabaaa"

pattern "aabaaa"

| |a|a|a|b|a|a|d|a|a|b|a|a|a|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|1|a|a|b| | | | | | | | | | |  
|2| |a|a|b|a|a|a| | | | | | |
|3| | |a|a| | | | | | | | | |
|4| | | |a| | | | | | | | | |
|5| | | | |a|a|a| | | | | | |
|6| | | | | |a|a| | | | | | |
|7| | | | | | |a| | | | | | |
|8| | | | | | | |a|a|b|a|a|a|

## Problem 2
a)  
|    c  |a|b|
|-------|-|-|
|last(c)|5|2|


| |a|a|a|b|a|a|d|a|a|b|a|a|a|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|1|a|a|b|a|a|a| | | | | | | |  
|2| |a|a|b|a|a|a| | | | | | |  
|3| | | | | | | |a|a|b|a|a|a|  

b)

```python
def last(p, c):
    return p.rfind(c)

def boyer_moore_match(t, p):
    m = len(p)
    n = len(t)
    i = m - 1
    j = m - 1
    cmp = 0


    while i <= n -1:
        cmp += 1
        if t[i] == p[j]:
            if j == 0:
                return (i, cmp)
            else:
                i = i-1
                j = j-1
        else:
            i = i + m - min(j, 1 + last(p, t[i]))
            j = m - 1

    return (-1, cmp)

t = 'Årsaken til dette er gjennombrudd innen maskinlæring. Feltet består av en rekke teknikker som gjør datamaskiner i stand til å avdekke kompliserte mønstre og sammenhenger i store datasett. Maskinlæring har hatt mange viktige anvendelser opp gjennom årene, men har aldri vært så gjennomgripende innen teknologi og programvareutvikling som i dag'
t = t.lower()
p = 'kaffe'

i, cmp = boyer_moore_match(t, p)

print(cmp / len(t)) # 0.2485.. passer bra
```

## Problem 3

|j   |0|1|2|3|4|5|
|----|-|-|-|-|-|-|
|P[j]|a|a|b|a|a|a|
|f(j)|0|1|0|1|2|2|  

failure function

longest prefix must be suffix of P[1..j]

| j | P[1..J] | longest prefix | f(j) |
|---|---------|----------------|------|
| 0 |    -    |       -        |  0   |
| 1 |  a      |       a        |  1   |
| 2 |  ab     |       -        |  0   | 
| 3 |  aba    |       a        |  1   | 
| 4 |  abaa   |       aa       |  2   |
| 5 |  abaaa  |       aa       |  2   |



| |a|a|a|b|a|a|d|a|a|b|a|a|a|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|1|a|a|b|a|a|a| | | | | | | |  
|2| |a|a|b|a|a|a| | | | | | |
|3| | | | |a|a|b|a|a|a| | | |  
|4| | | | | | |a|a|b|a|a|a| |  
|5| | | | | | | |a|a|b|a|a|a|  

## Problem 4
text = "aaabbaaa"
suffixes

|suffixes|prefixes|both     |
|--------|--------|---------|
|a       |a       | a       |
|aa      |aa      | aa      |
|aaa     |aaa     | aaa     |
|aaab    |baaa    |         |
|aaabb   |bbaaa   |         |
|aaabba  |abbaaa  |         |
|aaabbaa |aabbaaa |         |
|aaabbaaa|aaabbaaa| aaabbaaa|

4 prefixes are also suffixes


## Problem 5
!["Standard trie"](./trie.png)

## Problem 6
!["Compressed trie"](./compressed_trie.png)

## Problem 7
text = "dogs do not spot hot pots or cats"

|c|n|
|-|-|
|a|1|
|c|1|
|g|1|
|h|1|
|n|1|
|r|1|
|p|2|
|d|2|
|s|4|
|t|5|
|o|7|
| |7|

!["huffman tre"](./huffman.png)


## Problem 8


| |  |  |b|a|b|b|a|b|a|b|
|-|--|--|-|-|-|-|-|-|-|-|
| |  |-1|0|1|2|3|4|5|6|7|
| |-1| 0|0|0|0|0|0|0|0|0|
|b| 0| 0|1|1|1|1|1|1|1|1|
|b| 1| 0|1|1|2|2|2|2|2|2|
|a| 2| 0|1|2|2|2|3|3|3|3|
|b| 3| 0|1|2|3|3|3|4|4|4|
|b| 4| 0|1|2|3|4|4|4|4|5|
|a| 5| 0|1|2|3|4|5|5|5|5|
|a| 6| 0|1|2|3|4|5|5|6|6|
|a| 7| 0|1|2|3|4|5|5|6|6|
|b| 8| 0|1|2|3|4|5|6|6|7|

Longest common subsequence is 7 characters long

## Problem 9
a, b and c
```python
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
```

after 37 characters the recursive implementation started taking over a second..
