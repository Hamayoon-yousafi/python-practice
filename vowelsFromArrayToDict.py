alphabets = ["a", "b", "c" , "d" , "e" , "f" , "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
answer = {}

for alphabet in alphabets:
    if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
        answer[alphabet] = 0 
print(answer)