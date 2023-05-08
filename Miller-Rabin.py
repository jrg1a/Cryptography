import random
import time


tilfeldig = random.SystemRandom() # Random number
def single_test(n, a):
    eksponent =n-1
    while not eksponent & 1:
        eksponent >>= 1        
    if pow(a, eksponent, n) ==1: 
        return True
    while eksponent < n-1:
        if pow(a, eksponent, n)==n-1:
            return True   
        eksponent <<= 1 
    return False
    
def miller_rabin(n, k=40): 
    for i in range(k):
        x = tilfeldig.randrange(2, n - 1)
        if not single_test(n, x):
            return False         
    return True
    

def generate_prime(bits):   # Generate random numbers
    start = time.time()
    while True:  # odd numberzz
        odd = (tilfeldig.randrange(1 << bits-1, 1 << bits) << 1) + 1
        if miller_rabin(odd):
            print(f"Time used: {time.time() - start}.")
            return odd




if __name__ == "__main__":
    # enter the the desired length of the bit()!
    #p = generate_prime(500)
    #p = generate_prime(671)
    p = generate_prime(1024)
    print(p)




"""
#Notat: 
# 1 < a < n-1 , a is any random number
# if n is prime, then a^(n-1) = 1(mod n)
# a^(n-1)-1 = 0(mod n)
# (a^(n-1/2)-1) * (a^(n-1/2)+1) = 0 (mod n)
"""