import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

    if not (isinstance(family, list) or isinstance(start, int) or isinstance(end, int)):
        raise TypeError("argument type error")
    for elem in family:
        if not isinstance(family, list):
            raise TypeError("argument type error")
        for elem_in in elem:
            if not (isinstance(elem_in, float) or isinstance(elem_in, int)):
                print(type(elem_in))
                raise TypeError("argument type error")
        
    len_co = [len(row) for row in family]
    if not all(length == len_co[0] for length in len_co):
        print("column size wrong")
        exit(1)
    np_family = np.array(family)
    print("My shape is :", np_family.shape)
    start = abs(start)
    end = abs(end)
    print("My new shapes is : ({start}, {end})".format(start=start, end=end))
    return np_family[start:, :end]