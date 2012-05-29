M = [1, 1, 2, 4],[2, 2, 2, 5],[2, 2, 3, 6],[2, 5, 6, 7]
E = 2
print M
print E
############################################
def bool_ELEMENT(M, E):
    i = bb = be = 0
    iE = jE = -1
    N = len(M)
    nE = 0
    i  = 0
    while (bb == 0):
        if M[i][i] == E:
            iE = jE = i
            be = 1
        elif  M[i][i] < E:
            i = i + 1
        else:
            nE = i
            bb = 1
        if (i == N-1) or (be ==1):
            bb = 1
# # # # # # # # # # # # # # # # # # # #
# Not diagonal
    print nE
    if nE > 0:
# 6oo-9oo
        j = nE - 1
        i = nE
        while (j >= 0) and (i < N) and (be == 0):
            if M[i][j] == E:
                iE = i
                jE = j
                be = 1
            elif  M[i][j] > E:
                j = j-1
            else:
                i = i + 1
#12oo-15oo
        be1 = 0
        i = nE - 1
        j = nE
        while (i >= 0) and (j < N) and (be1 == 0):
            if M[i][j] == E:
                iE1 = i
                jE1 = j
                be1 = 1
            elif  M[i][j] > E:
                i = i-1
            else:
                j = j + 1
# min index element
        if be == be1 == 1:
            if (jE1 < iE) or ((jE1 == iE) and (iE1>jE)):
                iE = iE1
                jE = jE1
        if (be == 0) and (be1 == 1):
            iE = iE1
            jE = jE1
    return be, iE, jE
############################################
def all_ELEMENT(M, nI, nJ):
    nnI = nI
    nnJ = nJ
    N = len(M)
    E = M[nI][nJ]
    element_M = []
### 6oo-9oo
    while (nI < N) and (nJ >= 0):
        i = nI
        if M[i][nJ] < E:
            nI = nI + 1
        elif M[i][nJ] > E:
            nJ = nJ - 1
        else:
            while (i < N) and (M[i][nJ] == E):
                element_M.append([i,nJ])
                i = i + 1
            nJ = nJ - 1
### 12oo-15oo
    nI = nnJ
    nJ = nnI
    while (nJ < N) and (nI >= 0):
        j = nJ
        if M[nI][j] < E:
            nJ = nJ + 1
        elif M[nI][j] > E:
            nI = nI - 1
        else:
            while (j < N) and (M[nI][j] == E):
                element_M.append([nI, j])
                j = j + 1
            nI = nI - 1
### diagonal
    if (nnI == nnJ):
        element_M.pop(0)
        nIJ = nnI + 1
        while (nIJ < N) and (M[nIJ][nIJ] == E):
            element_M.append([nIJ, nIJ])
            i = j = nIJ + 1
            while (i < N) and (M[i][nIJ] == E):
                element_M.append([i, nIJ])
                i = i + 1
            while (nIJ < N) and (M[nIJ][j] == E):
                element_M.append([nIJ, j])
                j = j + 1
            nIJ = nIJ +1
    return element_M

tmp = bool_ELEMENT(M, E)
print tmp

tmp1 = all_ELEMENT(M, tmp[1], tmp[2])
print tmp1
#print be, iE, jE
