# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。 
# 
#  实现 LFUCache 类： 
# 
#  
#  LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象 
#  int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。 
#  void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之
# 前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。 
#  
# 
#  注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。 
# 
#  为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。 
# 
#  当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "g
# et"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lFUCache = new LFUCache(2);
# lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
# lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lFUCache.get(1);      // 返回 1
#                       // cache=[1,2], cnt(2)=1, cnt(1)=2
# lFUCache.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
#                       // cache=[3,1], cnt(3)=1, cnt(1)=2
# lFUCache.get(2);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
#                       // cache=[3,1], cnt(3)=2, cnt(1)=2
# lFUCache.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
#                       // cache=[4,3], cnt(4)=1, cnt(3)=2
# lFUCache.get(1);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
#                       // cache=[3,4], cnt(4)=1, cnt(3)=3
# lFUCache.get(4);      // 返回 4
#                       // cache=[3,4], cnt(4)=2, cnt(3)=3 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= capacity, key, value <= 104 
#  最多调用 105 次 get 和 put 方法 
#  
# 
#  
# 
#  进阶：你可以为这两种操作设计时间复杂度为 O(1) 的实现吗？ 
#  Related Topics 设计 
#  👍 385 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_val_dict = {}
        self.key_freq_dict = {}
        self.freq_keys = {}

    def get(self, key: int) -> int:
        if key in self.key_val_dict.keys():
            value = self.key_val_dict[key]
            self.update_freq(key)
            print(value)
            return value
        else:
            print(-1)
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_val_dict.keys():
            self.key_val_dict[key] = value
            self.update_freq(key)
        else:
            if self.size == self.capacity:
                self.remove_least_freq()
                self.size -= 1

            self.key_val_dict[key] = value
            self.key_freq_dict[key] = 1
            self.min_freq = 1
            self.add_to_freq_keys(1, key)
            self.size += 1

    def update_freq(self, key):
        old_freq = self.key_freq_dict[key]
        self.key_freq_dict[key] += 1
        self.freq_keys[old_freq].remove(key)
        if not self.freq_keys[old_freq] and self.min_freq == old_freq:
            self.min_freq = old_freq + 1
        self.add_to_freq_keys(old_freq + 1, key)

    def remove_least_freq(self):
        least_freq_key = self.freq_keys[self.min_freq].pop(0)
        self.key_val_dict.pop(least_freq_key)
        self.key_freq_dict.pop(least_freq_key)

    def add_to_freq_keys(self, freq, key):
        if not self.freq_keys.get(freq):
            self.freq_keys[freq] = [key]
        else:
            self.freq_keys[freq].append(key)

    def show(self):
        print(f'key value map: {self.key_val_dict}')
        print(f'key freq map: {self.key_freq_dict}')
        print(f'freq keys map: {self.freq_keys}')
        print(f'size: {self.size}')
        print(f'min_freq: {self.min_freq}')


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # obj = LFUCache(2)
    # obj.put(1, 1)
    # obj.show()
    # print(obj.get(1))
    # obj.show()
    # obj.put(2, 2)
    # obj.put(3, 3)
    # obj.show()
    obj = LFUCache(10)

    ops = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
           [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
           [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
           [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
           [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6]]
    # [4, 29], [3], [9], [6],
    # [3, 4], [1], [10], [3, 29],
    # [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
    # [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
    # [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]
    for i in ops:
        if len(i) == 1:
            obj.get(i[0])
        elif len(i) == 2:
            obj.put(i[0], i[1])
    obj.show()

# [null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,14,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,24,null,4,29,-1,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,-1,null,null,null,24,null,null,null,20,null,null,null,29,-1,-1,null,null,null,null,20,null,null,null,null,null,null,null]
# [null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,14,null,null,18,null,null,11,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,11,null,null,null,null,29,null,null,null,null,17,-1,18,null,null,null,-1,null,null,null,20,null,null,null,29,18,18,null,null,null,null,20,null,null,null,null,null,null,null]
