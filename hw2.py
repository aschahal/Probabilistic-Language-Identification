import sys
import math

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    X = {char: 0 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    with open(filename, encoding = 'utf-8') as f:
        for line in f:
            for char in line:
                # Case-folding
                char = char.upper()
                if 'A' <= char <= 'Z':
                    X[char] += 1

    return X

def compute_F(X, p, py):
    # F(y) = log f(y) = log P(Y = y) + ΣXi * log pi
    F = math.log(py)
    for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        F += X[char] * math.log(p[i])
    return F

def main():
    X = shred("letter.txt")

    # Q1: Print character counts
    print("Q1")
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(char, X[char])

    e, s = get_parameter_vectors()

    # Q2: Compute X1 log e1 log s1
    print("Q2")
    print(f"{X['A'] * math.log(e[0]):.4f}")
    print(f"{X['A'] * math.log(s[0]):.4f}")

    # Q3: Compute F(English) and F(Spanish)
    F_english = compute_F(X, e, 0.6)
    F_spanish = compute_F(X, s, 0.4)

    print("Q3")
    print(f"{F_english:.4f}")
    print(f"{F_spanish:.4f}")

    #Q4: Compute P(Y = English | X)
    if F_spanish - F_english >= 100:
        prob = 0
    elif F_spanish - F_english <= -100:
        prob = 1
    else:
        prob = 1 / (1 + math.exp(F_spanish - F_english))

    print("Q4")
    print(f"{prob:.4f}")

if __name__ == "__main__":
    main()




