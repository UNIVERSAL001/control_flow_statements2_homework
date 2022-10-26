def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n%10
    n//=10
    x2=n%10
    n//=10
    x3=n%10
    n//=10
    x4=n%10
    n//=10
    x5=n%10
    m = x1
    k=0
    if m <x1:
        m=x1
        k=0
    if m <x2:
        m=x2
        k=1
    if m <x3:
        m=x3
        k=2
    if m <x4:
        m=x4
        k=3
    if m <x5:
        m=x5
        k=4
    return k
print(main(12345))