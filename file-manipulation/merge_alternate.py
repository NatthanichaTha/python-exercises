def merge(S1, S2):
    SS = ""
    
    for i in range(min(len(S1), len(S2))):
        SS += S1[i] + S2[i]
    
    for j in range(i+1, len(S1)):
        SS += S1[j]
    
    for j in range(i+1, len(S2)):
        SS += S2[j]
    
    return SS

print(merge("Hello", "Bye"))