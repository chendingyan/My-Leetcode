class TrieNode:
    def __init__(self):
        self.path = 0
        self.end = 0
        self.map = [None for i in range(26)]
        #每一个节点有26条路

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word is None:
            return
        node = self.root
        for i in word:
            index = ord(i) - ord('a')
            if node.map[index] == None:
                node.map[index] = TrieNode()
            node = node.map[index]
            node.path +=1

        node.end+=1

    def search(self, word):
        if word is None:
            return False
        node = self.root
        for i in word:
            index = ord(i) - ord('a')
            if node.map[index] is None:
                return False
            node = node.map[index]
        if node.end == 0:
            return False
        return True

    def delete(self, word):
        if self.search(word) == False:
            return
        node = self.root
        for i in word:
            index =  ord(i) - ord('a')
            node.map[index].path-=1
            if node.map[index].path == 0:
                node.map[index] = None
                return
            node = node.map[index]
        node.end-=1
    #返回以字符串pre为前缀的单词数量。
    def prefixNumber(self, pre):
        if pre is None:
            return
        node = self.root
        for i in pre:
            index = ord(i) - ord('a')
            if node.map[index] is None:
                return 0
            node = node.map[index]
        return node.path


if __name__ == '__main__':
    # tree = Trie()
    # tree.insert('apple')
    # tree.insert('banana')
    # print(tree.search('appl'))
    # print(tree.search('applee'))
    # print(tree.search('apple'))
    # tree.delete('apple')
    # print(tree.search('apple'))
    # print(tree.prefixNumber('ap'))
    # tree.insert('app')
    # tree.insert('apple')
    # print(tree.search('appl'))
    # print(tree.prefixNumber('app'))

    trie = Trie()

    trie.insert("apple")
    print(trie.search("apple")) #true
    print(trie.search("app")) #false
    print(trie.prefixNumber("app"))
    trie.insert("app")
    print(trie.search("app"))
    trie.insert("app")
    print(trie.prefixNumber("app"))
