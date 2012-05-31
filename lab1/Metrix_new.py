M = [1, 2, 3, 4, 5]
##################################
M[0] = [1, 1, 2, 2, 2]
M[1] = [1, 2, 2, 3, 3]
M[2] = [1, 2, 2, 3, 3]
M[3] = [2, 2, 6, 6, 6]
M[4] = [2, 2, 7, 7, 8]
E = 1
##################################
for inn in M:
    print inn
print 'Element =', E

def bool_EL(M, E):
    bool_el = iE = jE = -1
    i_0 = temp = 0
    i_n = len(M) - 1
    N = i_n + 1
    # # # # # # # # # # # # # # # # # # # #
    # 1 and N - element
    if (E < M[0][0]) or (E > M[i_n][i_n]):
        bool_el = 0
    elif (E == M[0][0]):
        bool_el = 1
        iE = jE = 0
    elif (E == M[i_n][i_n]):
        bool_el = 1
        iE = jE = i_n
        # # # # # # # # # # # # # # # # # # # #
    # diagonal
    i_m = (i_n + i_0)/2
    while (bool_el == -1) and (i_m > i_0):
        if (M[i_m][i_m] == E):
            iE = jE = i_m
            bool_el = 1
        elif  M[i_m][i_m] < E:
            i_0 = i_m
        else:
            i_n = i_m
        i_m = (i_n + i_0)/2
        # # # # # # # # # # # # # # # # # # # #
    # Not diagonal
    if (bool_el == -1):
    # 6oo-9oo
        j = i_n - 1
        i = i_n
        while (j >= 0) and (i < N) and (bool_el == -1):
            if M[i][j] == E:
                iE = i
                jE = j
                bool_el = 1
            elif  M[i][j] > E:
                j = j - 1
            else:
                i = i + 1
    #12oo-15oo
        i = i_n - 1
        j = i_n
        while (i >= 0) and (j < N) and (bool_el == -1):
            if M[i][j] == E:
                iE = i
                jE = j
                bool_el = 1
            elif  M[i][j] > E:
                i = i-1
            else:
                j = j + 1
    if (bool_el == -1):
        bool_el = 0

    return bool_el, iE, jE
############################################
def bool_EL_min_IND(M, E):
    b_el_2 = iE = jE = -1
    b_fun_el = bool_EL(M, E)
    b_el = b_fun_el[0]
    ind_I = b_fun_el[1]
    ind_J = b_fun_el[2]
    if (b_el == 1) and (ind_I == ind_J):
        while (M[ind_I-1][ind_I-1] == E):
            ind_I = ind_J = ind_I - 1
    elif (ind_I > ind_J):
        i_n = ind_I
        i_0 = 0
        i_m = (i_n + i_0)/2
        while (i_m > i_0):
            if M[i_m][i_m] < E:
                i_0 = i_m
            else:
                i_n = i_m
            i_m = (i_n + i_0)/2
        N = len(M)
        i = i_n - 1
        j = i_n
        while (i >= 0) and (j < N) and (b_el_2 == -1):
            if M[i][j] == E:
                iE = i
                jE = j
                b_el_2 = 1
            elif  M[i][j] > E:
                i = i - 1
            else:
                j = j + 1
    if (b_el_2 == 1):
        if (jE < ind_I) or ((jE == ind_I) and (iE > ind_J)):
            ind_I = iE
            ind_J = jE
    return ind_I, ind_J

############################################
def all_ELEMENT(M, E):
    tmp = bool_EL_min_IND(M, E)
    nnI = nI = tmp[0]
    nnJ = nJ = tmp[1]
    element_M = []
    # if element exist
    if (nI > -1):
        N = len(M)
        E = M[nI][nJ]
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


print 'bool_EL =', bool_EL(M,E)
print 'min index =', bool_EL_min_IND(M, E)
print 'all_EL =',all_ELEMENT(M, E)
#print be, iE, jE

