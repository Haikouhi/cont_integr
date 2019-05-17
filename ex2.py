def exercice_2(x, a, b):
    """
    Ecrire une fonction qui renvoie :
        -255 si x<a
        x si a<x<b
        255 si x>b
    (A faire en TDD)

    """

    if a > b:
        raise ValueError
    if x < a:
        return -255
    elif x > b:
        return 255
    else:
        return x

