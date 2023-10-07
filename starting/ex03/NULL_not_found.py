def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing: None", type(object))
        return 0
    elif isinstance(object, int):
        if object == 0:
            print("Zero: 0", type(object))
            return 0
    elif isinstance(object, str):
        if len(object) == 0: 
            print("Empty:", type(object))
            return 0
    elif isinstance(object, float):
        if object != float("NaN"):
            print("Cheese: nan", type(object))
            return 0
    elif isinstance(object, bool):
        if object == False:
            print("Fake: False", type(object))
            return 0
    print("Type not Found")
    return 1