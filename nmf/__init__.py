import numpy as np

def improve(H, C, D):
    '''
    Improve the nonnegative approximation H ~ CD

    The user is responsible for initializing C and D with nonnegative entries.
    Because this is a multiplicative algorithm, any sparsity in C and D is
    preserved.

    '''
    # D update
    D = D * C.T.dot(H) / C.T.dot(C).dot(H)

    # C update
    C = C * H.dot(D.T) / C.dot(D).dot(D.T)

    return C, D

