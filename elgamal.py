import sys
import random


def GCD(a,b): #
    while b:
        a, b = b, a % b
    return a

def inverse(a, n):
    t, new_t=0, 1
    r, new_r=n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t-quotient*new_t
        r, new_r = new_r, r-quotient*new_r
    if r>1:
        raise ValueError("a er ikke invertibel!!!")
    if t<0:
        t=t+n
    return t



def hent_parameter(parameter):
    with open(parameter,'r') as f:
        p = int(f.readline().strip())
        g = int(f.readline().strip())
        B = int(f.readline().strip())
    return p, g, B

def hent_private_key(private_key):
    with open(private_key,'r') as f:
        d = int(f.readline().strip())
    return d

def hent_message(message):
    with open(message,'r') as f:
        message = int(f.readline().strip())
    return message

def signature(output, r, s):
    with open(output,'w') as f:
        f.write(str(r) + '\n')
        f.write(str(s) + '\n')

def signering(p, g, B, d, message):
    k = random.randint(1, p-2)
    while GCD(k,p-1) != 1:
        k = random.randint(1, p-2)
    r = pow(g, k, p)
    k_invers = inverse(k, p - 1)
    s = ((message -d*r) * k_invers) % (p-1)
    return r, s


def main():
    parameter = sys.argv[1]
    privat_key = sys.argv[2]
    message = sys.argv[3]
    output = sys.argv[4]

    p, g, B = hent_parameter(parameter)
    d = hent_private_key(privat_key)
    message = hent_message(message)

    r, s = signering(p, g, B, d, message)
    signature(output, r, s)

if __name__ == "__main__":
    main()
