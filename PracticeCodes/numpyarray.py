import numpy as np

def main():
    pointer = 2
    ndarray = np.array (
                    [
                       [ [111, 112, 113, 114 ], [121, 122, 123, 124] , [131, 132, 133, 134] ],
                       [ [211, 212, 213, 214], [221, 222, 223, 224], [231, 232, 233, 234] ],
                       [ [311, 312, 313, 314], [321, 322, 323, 324], [331, 332, 333, 334] ],
                       [  [411, 412, 413, 414], [421, 422, 423, 424], [431, 432, 433, 434] ]
                    ]
                   )
    print(ndarray[0])
    return ndarray

#if __name__ == "__main__":
main()
print("abc")