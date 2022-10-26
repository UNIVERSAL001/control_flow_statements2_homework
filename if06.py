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
    m = 0
    if m <x1:
        m=1
    if m <x2:
        m=2
    if m <x3:
        m=3
    if m <x4:
        m=4
    if m <x5:
        m=5
    return m