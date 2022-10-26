def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    ma = a
    mi = a
    if ma<b:
        ma=b
    if ma<c:
        ma=c
    if mi>b:
        mi=b
    if mi<c:
        mi=c
    
    return a+b+c-mi-ma