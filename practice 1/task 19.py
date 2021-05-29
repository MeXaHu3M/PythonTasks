n = int(input())
letters = list(input())
print()

def BruteCheck(word):
    for let in letters:
        if  let not in word:
            return False
    return True

def Brute(word = ''):
    if len(word) < n:
        for let in letters:
            Brute(word + let)
    elif BruteCheck(word):
        print(word)
Brute()