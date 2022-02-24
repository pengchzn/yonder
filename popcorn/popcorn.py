import numpy as np
import scipy.sparse.linalg as sp
from numpy.linalg import inv


def popcorn(X, Xsd, p, MaxIter=1e5):
    X = np.mat(X)
    Xsd = np.mat(Xsd) # Convert the formation of imput data
    m = X.shape[0] # Numbers of lines in X
    n = X.shape[1] # Numbers of columns in X
    if p > min(m, n):
        exit("popcorn:err1 - Invalid rank for MLPCA decomposition")
    ml = Xsd.shape[0] # Numbers of lines in Xsd
    nl = Xsd.shape[1] # Numbers of columns in Xsd
    if m != ml or n != nl:
        exit("popcorn:err2 - Dimensions of data and standard deviations do not matchn")
    if bool(np.any(Xsd == 0)):
        exit("popcorn:err3 - Zero value(s) for standard deviations")

# Initialization
    ConvLim = 1e-10 # Convergence Limit
    MaxIter = MaxIter # Maximum no. of iterations
    VarMult = 1000 # Multiplier for missing data
    VarX = np.multiply(Xsd, Xsd) # Convert sd's to variance
    VarX[np.isnan(VarX)] == VarX.max() * VarMult # Give missing values large variance
    U, S, V = sp.svds(X, k=p) # Generate initial estimates assuming homoeostatic errors
    Count = 0 # Loop counter
    Sold = 0 # Hold last value of objective function
    ErrFlag = -1 # Loop flag
    while (ErrFlag < 0):
        Count = Count + 1
        # Evaluate objective function
        Sobj = 0 # Initialize the sum
        MLX = np.mat(np.zeros((X.shape[0], X.shape[1])))
        for j in range(0, n):
            Q = np.diagflat(1 / VarX[:, j]) # Inverse of error covariance matrix
            FInter = inv(U.T @ Q @ U) # Intermediate calculation
            MLX[:, j] = U @ (FInter @ (U.T @ (Q @ X[:, j]))) # Max.Lik estimates
            Dx = np.mat(X[:, j] - MLX[:, j]) # Residual vector
            Sobj = Sobj + Dx.T @ Q @ Dx # Update objective function
        if Count % 2 == 1: # Check on odd iterations ONLY
            ConvCalc = np.abs(Sold - Sobj) / Sobj # Convergence criterion
            if ConvCalc < ConvLim:
                ErrFlag = 0
            if Count > MaxIter: # Maximum Iterations
                ErrFlag = 1
                exit("popcorn:err4 - Maximum iterations exceeded")
        if ErrFlag < 0:
            Sold = Sobj # Save most recent objective function
            U, S, V = sp.svds(MLX, k=p)
            V = V.T
            X = X.T # Flip matrix
            VarX = VarX.T # Flip the varience
            n = X.shape[1] # Adjust the no. of columns
            U = V # Becomes U in for transpose

    U, S, V = sp.svds(MLX, k=p)
    S = np.mat(np.diag(S))
    V = V.T
    return U, S, V
