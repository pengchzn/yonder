import numpy as np
import scipy.sparse.linalg as sp
from numpy.linalg import inv


def popcorn(X, Xsd, p, MaxIter=1e5):
    X = np.mat(X)
    Xsd = np.mat(Xsd)
    m = X.shape[0]
    n = X.shape[1]
    if p > min(m, n):
        exit("popcorn:err1 - Invalid rank for MLPCA decomposition")
    ml = Xsd.shape[0]
    nl = Xsd.shape[1]
    if m != ml or n != nl:
        exit("popcorn:err2 - Dimensions of data and standard deviations do not matchn")
    if bool(np.any(Xsd == 0)):
        exit("popcorn:err3 - Zero value(s) for standard deviations")
    ConvLim = 1e-10
    MaxIter = MaxIter
    VarMult = 1000
    VarX = np.multiply(Xsd, Xsd)
    VarX[np.isnan(VarX)] == VarX.max() * VarMult
    U, S, V = sp.svds(X, k=p)
    Count = 0
    Sold = 0
    ErrFlag = -1
    while (ErrFlag < 0):
        Count = Count + 1
        Sobj = 0
        MLX = np.mat(np.zeros((X.shape[0], X.shape[1])))
        for j in range(0, n):
            Q = np.diagflat(1 / VarX[:, j])
            FInter = inv(U.T @ Q @ U)
            MLX[:, j] = U @ (FInter @ (U.T @ (Q @ X[:, j])))
            Dx = np.mat(X[:, j] - MLX[:, j])
            Sobj = Sobj + Dx.T @ Q @ Dx
        if Count % 2 == 1:
            ConvCalc = np.abs(Sold - Sobj) / Sobj
            if ConvCalc < ConvLim:
                ErrFlag = 0
            if Count > MaxIter:
                ErrFlag = 1
                exit("popcorn:err4 - Maximum iterations exceeded")
        if ErrFlag < 0:
            Sold = Sobj
            U, S, V = sp.svds(MLX, k=p)
            V = V.T
            X = X.T
            VarX = VarX.T
            n = X.shape[1]
            U = V
    U, S, V = sp.svds(MLX, k=p)
    S = np.mat(np.diag(S))
    V = V.T
    return U, S, V
