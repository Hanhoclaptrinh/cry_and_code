def getTotalX(a, b):
    # tim boi chung nho nhat cua mang a
    lcm_a = reduce(lambda x, y: (x * y) // math.gcd(x, y), a)
    
    # tim uoc chung lon nhat cua mang b
    gcd_b = reduce(math.gcd, b)
    
    count = 0
    
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
        
    return count