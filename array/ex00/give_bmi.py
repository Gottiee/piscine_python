import numpy as np

def error():
    print("give_bmi: List value error")
    exit(1)

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        error()

    for i, h in enumerate(height):
        if not isinstance(h, int) and not isinstance(h, float):
            error()
        
    for i, w in enumerate(weight):
        if not isinstance(w, int) and not isinstance(w, float):
            error()

    wei = np.array(weight) 
    hei = np.array(height)
    return list(wei / (hei * hei))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    l = np.array(bmi)
    return list(limit < l)
