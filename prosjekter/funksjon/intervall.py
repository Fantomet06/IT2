"""
def overlapp_intervall(a,b,c,d):
    if a < c and b < c:
        return False
    elif a > d and b > d:
        return False
    else:
        return True
    
a,b= input("Skriv inn intervall 1: ").split()
c,d= input("Skriv inn intervall 2: ").split()
if overlapp_intervall(int(a),int(b),int(c),int(d)): print("\nIntervallene overlapper") 
else: print("\nIntervallene overlapper ikke")
"""

