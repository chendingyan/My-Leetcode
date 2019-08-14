# 设计RandomPool结构
# 【题目】
# 设计一种结构，在该结构中有如下三个功能: insert(key):将某个key加入到该结构，做到不重复加入 delete(key):将原本在结构中的某个key移除 getRandom(): 等概率随机返回结构中的任何一个key。
# 【要求】 Insert、delete和getRandom方法的时间复杂度都是O(1)

# 首先需要两张表 map1 map2
# 先不考虑删除操作 如果只有insert和getRandom
# 每次加一个数 map1 key = str value = index map2 key = index value = str 然后getRandom随随机数 找index
# 如果考虑上删除 我们把map1最后一个记录 的str 换到删掉的位置的str size-=1 还是可以实现
import random
class RandomPool:
    def __init__(self):
        self.map1 = dict()
        self.map2 = dict()
        self.size = 0

    def insert(self, key):
        if key not in self.map1:
            self.map1[key] = self.size
            self.map2[self.size] = key
            self.size+=1

    def getRandom(self):
        if self.size == 0:
            return None
        index = random.randint(0,self.size-1)
        return self.map2[index]

    def delete(self, key):
        if key in self.map1:

            index = self.map1[key]
            self.map1.pop(key)
            last = self.map2[self.size-1]
            self.map1[last] = index
            self.map2[index] = last
            self.map2.pop(self.size-1)
            self.size-=1

if __name__ == '__main__':
    rp = RandomPool()
    rp.insert('a')
    rp.insert('b')
    rp.insert('c')
    print(rp.getRandom())
    print(rp.map1, rp.map2)
    rp.delete('b')
    print(rp.map1, rp.map2, rp.size)