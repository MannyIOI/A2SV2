def bonAppetit(bill, k, b):
    anna_exclusion = bill[k]
    total = 0
    for i in bill:
        total = total + i
    
    shared_cost = (total - anna_exclusion) // 2
    if b > shared_cost:
        return b - shared_cost
    
    return 'Bon Appetit'