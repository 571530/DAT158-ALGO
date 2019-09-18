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