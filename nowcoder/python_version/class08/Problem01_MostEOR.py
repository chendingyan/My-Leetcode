# 一个数组的异或和是指数组中所有的数异或在一起的结果。给定一个数组arr，求最大子数组异或和。
# 这道题利用的是前缀树

# 首先理解什么是异或 XOR
# 如果a、b两个值不相同，则异或结果为1。 如果a、b两个值相同，异或结果为0。 python里好像是^
# 对于一个arr 的最大子数组 可能是 i~i i-1~i i-2~i ...... 0 ~ i 那么这些异或怎么算？
# 先算总的整个arr的异或 0~i 那么i~i 就是0~i 异或 0~(i-1)   因为相同会变成0 0~i-1 异或 0~i-1 = 0 只剩下一个i多出来
# 同理 i-1 ~i = 0~i 异或 0~i-2
# xor[j...i]= xor[0...i] ^ xor[0...j-1] 然后xor[0...j-1]好像可以放到前缀树里面
# 但这个方法 不是最优解 我们在这里举例了一个4位二进制数的方法 这个方法可以做 一个数组 找里面的两个数的最大疑惑和 但并不是最优的
# 这个方法是前缀树加贪心 把所有的0-0 0-1 0-i 全部算出来放到前缀树里 在根据贪心  我们希望高位先变1
# 如果现在sum = x [0...i] 是1 我们要在前缀树里搜索0  如果是0 搜索1这样
# 如果是32位有符号整数 我们希望符号位走一样的 负负得正 正正还是正嘛



class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['end'] = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return cur.get('end', False)

    def startWith(self, prefix):
        cur = self.root
        for c in prefix:
            if not c in cur:
                return False
            cur = cur[c]
        return True

    def query(self, str):
        cur = self.root
        ans = []
        main_ans = []
        for c in str:
            if c == '0':
                qword = '1'
            elif c == '1':
                qword = '0'
            if qword in cur:
                cur = cur[qword]
                ans.append(qword)
                main_ans.append('1')
            else:
                cur = cur[c]
                ans.append(c)
                main_ans.append('0')

        ans = ''.join(ans)
        main_ans = ''.join(main_ans)
        return main_ans


def toBinary(num):
    return bin(num).replace('0b','').zfill(4)

def MaxEOR(arr):
    maxvalue = 0
    for i in range(len(arr)-1, 0, -1):
        array = arr[0:i]
        temp = 0
        for i in array:
            str = toBinary(temp)
            tree.insert(str)
            temp = temp ^ i
        sum = temp
        ans = tree.query(toBinary(sum))
        ans_num = int(ans, 2)
        maxvalue = max(ans_num, maxvalue)
    return maxvalue

if __name__ == '__main__':
    tree = Trie()



    # arr = ['11','1','15','10','13','4']
    arr = [11,1,15,10,13,4]
    print(MaxEOR(arr))



