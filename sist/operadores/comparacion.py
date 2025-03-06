def comparar (a, b):
    if a > b:
        return 'es mayor'
    elif a < b:
        return  'es menor '
    elif a >= b:
        return 'mayor o igual que'
    elif a <= b:
        return 'menor o igual que'
    elif a != b:
        return 'diferente de'
    else:
        return  'igual '
    