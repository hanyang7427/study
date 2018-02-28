# encoding = utf-8

import os
import sys
import numpy as np
def main(argc, argv, envp):
    # dim -> dimensionality 维度
    one_dim = np.arange(1,5)
    print(one_dim)
    print(type(one_dim))
    print(one_dim.dtype)
    print(one_dim.shape)

    two_dim = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]], dtype=float)
    print(two_dim)
    print(type(two_dim))
    print(two_dim.dtype)
    print(two_dim.shape)
    '''
    three_dim = np.array([
        [
            np.arange(1, 5),
            np.arange(5, 9),
            np.arange(9, 13),
        ],
        [
            np.arange(13, 17),
            np.arange(17, 21),
            np.arange(21, 25),
        ],
    ])
    '''
    three_dim = np.arange(1, 25).reshape(2,3,4).astype(float)
    print(three_dim)
    print(type(three_dim))
    print(three_dim.dtype)
    print(three_dim.shape)
    print(three_dim[1, 0, 0])
    for i in range(three_dim.shape[0]):
        for j in range(three_dim.shape[1]):
            for k in range(three_dim.shape[2]):
                print('{:4}'.format(three_dim[i, j, k]),end=' ')
            print()
        print()
    return 0
if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))