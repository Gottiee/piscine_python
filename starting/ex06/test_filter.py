from ft_filter import ft_filter

def even (number) -> bool:
    if number %2 == 0:
        return True
    return False
    
def even_dict(item):
    key, value = item  # Décompose le tuple en clé et valeur
    return key % 2 == 0

def main():
    ft_list = [1 ,2 ,3 ,4 ,5 ,6]
    ft_tuple = (1 ,2 ,3 ,4 ,5 ,6)
    ft_set = {1, 2, 3, 4, 5 ,5, 6}
    ft_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6:6}

    print("List", ft_list)
    print("filter list", list(filter(even, ft_list)))
    print("ft_filter list", list(ft_filter(even, ft_list)))

    print("\nTuple", ft_tuple)
    print("filter tuple", tuple(filter(even, ft_tuple)))
    print("ft_filter tuple", tuple(ft_filter(even, ft_tuple)))

    print("\nSet", ft_set)
    print("filter set", set(filter(even, ft_set)))
    print("ft_filter set", set(ft_filter(even, ft_set)))

    print("\nDict", ft_dict)
    print("filter dict", dict(filter(even_dict, ft_dict.items())))
    print("ft_filter dict", dict(ft_filter(even_dict, ft_dict.items())))




if __name__ == "__main__":
    main()