class PohonBiner:
    def __init__(self, A, L, R):
        self.A = A
        self.L = L
        self.R = R

def MakePB (A,L,R):
    return PohonBiner(A,L,R)

def Akar(P):
    return P.A

def Left(P):
    return P.L

def Right(P):
    return P.R

def IsTreeEmpty(P):
    if (P==None):
        return True
    else:
        return False

def IsOneElement(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))):
        return True
    else:
        return False

def IsUnerRight(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

def IsUnerLeft(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))):
        return True
    else:
        return False

def IsBiner(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

def NbElmtPB(P):
    if (IsOneElement(P)):
        return 1
    else:
        if(IsBiner(P)):
            return NbElmtPB(Left(P)) + 1 + NbElmtPB(Right(P))
        elif (IsUnerLeft(P)):
            return NbElmtPB(Left(P)) +1
        elif (IsUnerRight(P)):
            return 1 + NbElmtPB(Right(P))

def NbDaunPB(P):
    if (IsOneElement(P)):
        return 1
    else:
        if (IsBiner(P)):
            return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
        elif (IsUnerLeft(P)):
            return NbDaunPB(Left(P))
        elif(IsUnerRight(P)):
            return NbDaunPB(Right(P))

def RepPrefixPB(P):
    if (IsOneElement(P)):
        return [Akar(P)]
    else:
        if (IsBiner(P)):
            return [Akar(P)] + [RepPrefixPB(Left(P))] + [RepPrefixPB(Right(P))]
        elif (IsUnerLeft(P)):
            return [Akar(P)] + [RepPrefixPB(Left(P))]
        elif (IsUnerRight(P)):
            return [Akar(P)] + [RepPrefixPB(Right(P))]


def search (a,P):
    if (Akar(P) == a):
        return True
    elif (IsTreeEmpty(P)):
        return False
    else:
        if (IsOneElement(P)):
            if (Akar(P) == a):
                return True
            else:
                return False
        else:
            if (Akar(P) < a):
                return search(a,Right(P))
            else:
                return search(a,Left(P))
