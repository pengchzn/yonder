import numpy as np
from numpy.linalg import inv
import scipy.sparse.linalg as sp


def MLPCA(X, Xsd, MaxIter=1e5):
    epsilon = 1e-10
    MaxIter = MaxIter
    n = X.shape[1]
    p = n - 1
    VarX = np.multiply(Xsd, Xsd)
    U, S, V = sp.svds(X,k=p)
    i = 0
    Sold = 0
    k = -1
    while (k < 0):
        i = i + 1
        Sobj = 0
        LX = np.mat(np.zeros((X.shape[0], X.shape[1])))
        for j in range(0, n):
            Q = np.diagflat(1 / VarX[:, j])
            F = inv(U.T @ Q @ U)
            LX[:, j] = U @ (F @ (U.T @ (Q @ X[:, j])))
            Dx = np.mat(X[:, j] - LX[:, j])
            Sobj = Sobj + Dx.T @ Q @ Dx
        if i % 2 == 1:
            ConvCalc = np.abs(Sold - Sobj) / Sobj
            if ConvCalc < epsilon:
                k = 0
            if i > MaxIter:
                k = 1
                exit("MaxIter exceeded")
        if k < 0:
            Sold = Sobj
            U, S, V = sp.svds(LX,k=p)
            V = V.T
            X = X.T
            VarX = VarX.T
            n = X.shape[1]
            U = V
    U, S, V = sp.svds(LX,k=p)
    S = np.mat(np.diag(S))
    V = V.T
    return U @ S @ V.T