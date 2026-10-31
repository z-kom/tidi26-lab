def two_pointers(a, b):
    """
    Два указателя
    Время: O(M+N)
    Память: O(1)
    """
    i = 0
    j = 0
    
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return True
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
            
    return False


def binary_search(a, b):
    """
    Бинарный поиск
    Время: O(M * log N)
    Память: O(1)
    """
    if len(a) > len(b):
        a, b = b, a
    
    for x in a:
        l = 0
        r = len(b)
        
        while l < r:
            m = (l + r) // 2
            if b[m] < x:
                l = m + 1
            else:
                r = m
        
        if l < len(b) and b[l] == x:
            return True
        
    return False


def exponential_search(a, b):
    """
    Экспоненциальный поиск
    Время: O(M*log(2N/M))
    Память: O(1)
    """
    if len(a) > len(b):
        a, b = b, a
        
    n = len(b)
    q = 0
    
    for x in a:
        if q >= n:
            return False
        if b[q] == x:
            return True
        if b[q] > x:
            continue
        
        step = 1
        
        while q + step < n and b[q + step] < x:
            step *= 2
            
        l = q + step // 2
        r = min(n, q + step)
        
        while l < r:
            m = (l + r) // 2
            if b[m] < x:
                l = m + 1
            else:
                r = m
                
        if l < n and b[l] == x:
            return True
        q = l
        
    return False


def double_binary_search(a, b):
    """
    Двойной бинарный
    Время: O(M*log(2N/M))
    Память: O(log M)
    """
    if len(a) > len(b):
        a, b = b, a

    def rec(l1, r1, l2, r2):
        if l1 >= r1 or l2 >= r2:
            return False
        if a[l1] > b[r2 - 1] or a[r1 - 1] < b[l2]:
            return False
        
        m1 = (l1 + r1) // 2
        l = l2
        r = r2
        
        while l < r:
            m2 = (l + r) // 2
            if b[m2] < a[m1]:
                l = m2 + 1
            else:
                r = m2
                
        if l < r2 and b[l] == a[m1]:
            return True
        return rec(l1, m1, l2, l) or rec(m1 + 1, r1, l, r2)

    return rec(0, len(a), 0, len(b))
