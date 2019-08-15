def generate_Next(str):
    next = [0] * len(str)
    next[0] = -1
    next[1] = 0
    i = 2
    cur = 0
    while i < len(str):
        if str[i-1] == str[cur]:
            next[i] = cur+1
            cur+=1
            i+=1
        elif cur != 0:
            cur = next[cur]
        else:
            i+=1
    return next

def kmp(str1, str2):
    next = generate_Next(str2)
    i,j = 0,0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i+=1
            j+=1
        elif j!=0:
            j = next[j]
        else:
            i+=1
    if j == len(str2):
        return i-j
    else:
        return -1

if __name__ == '__main__':
    str1 = 'abcabcababaccc'
    match = 'ababa'
    next = generate_Next(match)
    print(next)
    res = kmp(str1, match)
    print(res)
