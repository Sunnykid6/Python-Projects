def solution(S):
    occurrences = [0] * 256

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = ''
    best_res = -1

    for i in range(len(S)):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]
            print(best_res)

    return best_char

print(solution("hello"))


def solution(S):
    # I think O(n) 
    lowercase = []
    uppercase = []
    
    final = []
    for char in S:
        if (char >= 'A' and char  <= 'Z'):
            uppercase.append(char.lower())
        elif(char >= 'a' and char <= 'z'):
            lowercase.append(char)
    
    temp = set(uppercase)
    final = [ord(value) for value in lowercase if value in temp]
    
    if len(final) == 0:
        return  "NO"
    else:
        return chr(max(final)).upper()