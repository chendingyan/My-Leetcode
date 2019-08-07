def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    index, m = 0, len(substring)
    pnext = [0]*m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index!=0):
            index = pnext[index-1]
        else:
            pnext[i] = 0
            i += 1
    return pnext

def kmp(string, substring):
    pnext = gen_pnext(substring)
    m = len(substring)
    n = len(string)
    i , j = 0,0
    while i<n and j < m:
        if string[i] == substring[j]:
            i+=1
            j+=1
        elif j!= 0:
            j = pnext[j-1]
        else:
            i+=1
    if j == m:
        return i-j
    else:
        return -1

if __name__ == '__main__':
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    print(kmp(string, substring))
    # print(gen_pnext(substring))