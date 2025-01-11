"""
哈希表实现练习demo
包含基于链地址法和开放地址法的哈希表实现
"""

class HashNode:
    """哈希表节点（用于链地址法）"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableChaining:
    """基于链地址法的哈希表"""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash(self, key):
        """哈希函数"""
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        else:
            return hash(key) % self.size
    
    def put(self, key, value):
        """插入键值对"""
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = HashNode(key, value)
            self.count += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            
            current.next = HashNode(key, value)
            self.count += 1
    
    def get(self, key):
        """获取值"""
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """删除键值对"""
        index = self._hash(key)
        current = self.table[index]
        
        if current is None:
            raise KeyError(f"Key '{key}' not found")
        
        if current.key == key:
            self.table[index] = current.next
            self.count -= 1
            return current.value
        
        while current.next:
            if current.next.key == key:
                value = current.next.value
                current.next = current.next.next
                self.count -= 1
                return value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """检查是否包含键"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def keys(self):
        """获取所有键"""
        result = []
        for i in range(self.size):
            current = self.table[i]
            while current:
                result.append(current.key)
                current = current.next
        return result
    
    def values(self):
        """获取所有值"""
        result = []
        for i in range(self.size):
            current = self.table[i]
            while current:
                result.append(current.value)
                current = current.next
        return result
    
    def items(self):
        """获取所有键值对"""
        result = []
        for i in range(self.size):
            current = self.table[i]
            while current:
                result.append((current.key, current.value))
                current = current.next
        return result
    
    def load_factor(self):
        """计算负载因子"""
        return self.count / self.size
    
    def display(self):
        """显示哈希表结构"""
        for i in range(self.size):
            print(f"  [{i}]: ", end="")
            current = self.table[i]
            chain = []
            while current:
                chain.append(f"({current.key}: {current.value})")
                current = current.next
            print(" -> ".join(chain) if chain else "None")


class HashTableOpenAddressing:
    """基于开放地址法的哈希表（线性探测）"""
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted = [False] * size
        self.count = 0
    
    def _hash(self, key):
        """哈希函数"""
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        else:
            return hash(key) % self.size
    
    def _find_slot(self, key):
        """找到键的槽位"""
        index = self._hash(key)
        original_index = index
        
        while (self.keys[index] is not None and 
               self.keys[index] != key and 
               not self.deleted[index]):
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        
        return index
    
    def put(self, key, value):
        """插入键值对"""
        if self.count >= self.size * 0.75:
            self._resize()
        
        index = self._find_slot(key)
        
        if self.keys[index] is None or self.deleted[index]:
            self.count += 1
        
        self.keys[index] = key
        self.values[index] = value
        self.deleted[index] = False
    
    def get(self, key):
        """获取值"""
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                return self.values[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """删除键值对"""
        index = self._hash(key)
        original_index = index
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                self.deleted[index] = True
                self.count -= 1
                return self.values[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """检查是否包含键"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def _resize(self):
        """扩容"""
        old_keys = self.keys
        old_values = self.values
        old_deleted = self.deleted
        
        self.size *= 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.deleted = [False] * self.size
        self.count = 0
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None and not old_deleted[i]:
                self.put(old_keys[i], old_values[i])
    
    def load_factor(self):
        """计算负载因子"""
        return self.count / self.size
    
    def display(self):
        """显示哈希表结构"""
        for i in range(self.size):
            status = "Deleted" if self.deleted[i] else "Active"
            if self.keys[i] is not None:
                print(f"  [{i}]: ({self.keys[i]}: {self.values[i]}) - {status}")
            else:
                print(f"  [{i}]: Empty")


class HashSet:
    """基于哈希表的集合实现"""
    def __init__(self, size=10):
        self.hash_table = HashTableChaining(size)
    
    def add(self, item):
        """添加元素"""
        self.hash_table.put(item, True)
    
    def remove(self, item):
        """移除元素"""
        self.hash_table.delete(item)
    
    def contains(self, item):
        """检查是否包含元素"""
        return self.hash_table.contains(item)
    
    def size(self):
        """获取集合大小"""
        return self.hash_table.count
    
    def is_empty(self):
        """检查是否为空"""
        return self.hash_table.count == 0
    
    def to_list(self):
        """转换为列表"""
        return self.hash_table.keys()
    
    def union(self, other_set):
        """并集"""
        result = HashSet()
        for item in self.to_list():
            result.add(item)
        for item in other_set.to_list():
            result.add(item)
        return result
    
    def intersection(self, other_set):
        """交集"""
        result = HashSet()
        for item in self.to_list():
            if other_set.contains(item):
                result.add(item)
        return result
    
    def difference(self, other_set):
        """差集"""
        result = HashSet()
        for item in self.to_list():
            if not other_set.contains(item):
                result.add(item)
        return result


class HashTableApplications:
    """哈希表应用示例"""
    
    @staticmethod
    def find_duplicates(arr):
        """查找数组中的重复元素"""
        seen = HashSet()
        duplicates = HashSet()
        
        for item in arr:
            if seen.contains(item):
                duplicates.add(item)
            else:
                seen.add(item)
        
        return duplicates.to_list()
    
    @staticmethod
    def two_sum(nums, target):
        """两数之和问题"""
        hash_map = HashTableChaining()
        
        for i, num in enumerate(nums):
            complement = target - num
            if hash_map.contains(complement):
                return [hash_map.get(complement), i]
            hash_map.put(num, i)
        
        return None
    
    @staticmethod
    def word_frequency(text):
        """统计单词频率"""
        word_count = HashTableChaining()
        words = text.lower().split()
        
        for word in words:
            word = word.strip('.,!?;:"()[]')
            if word:
                try:
                    count = word_count.get(word)
                    word_count.put(word, count + 1)
                except KeyError:
                    word_count.put(word, 1)
        
        return word_count.items()


def demo():
    """演示哈希表操作"""
    print("=== 链地址法哈希表演示 ===")
    
    ht1 = HashTableChaining(7)
    
    print("1. 插入键值对:")
    pairs = [("apple", 5), ("banana", 3), ("orange", 8), ("grape", 2), ("kiwi", 4)]
    for key, value in pairs:
        ht1.put(key, value)
        print(f"   插入 ({key}: {value})")
    
    print(f"\n2. 负载因子: {ht1.load_factor():.2f}")
    
    print("\n3. 哈希表结构:")
    ht1.display()
    
    print("\n4. 查找操作:")
    search_keys = ["apple", "grape", "mango"]
    for key in search_keys:
        try:
            value = ht1.get(key)
            print(f"   {key}: {value}")
        except KeyError:
            print(f"   {key}: 未找到")
    
    print(f"\n5. 所有键: {ht1.keys()}")
    print(f"   所有值: {ht1.values()}")
    
    print("\n6. 删除操作:")
    ht1.delete("banana")
    print("   删除 'banana' 后:")
    ht1.display()
    
    print("\n=== 开放地址法哈希表演示 ===")
    
    ht2 = HashTableOpenAddressing(7)
    
    print("1. 插入数字键值对:")
    for i in range(5):
        ht2.put(i * 10, f"value_{i}")
        print(f"   插入 ({i * 10}: value_{i})")
    
    print(f"\n2. 负载因子: {ht2.load_factor():.2f}")
    
    print("\n3. 哈希表结构:")
    ht2.display()
    
    print("\n=== 哈希集合演示 ===")
    
    set1 = HashSet()
    set2 = HashSet()
    
    print("1. 创建集合:")
    for item in [1, 2, 3, 4, 5]:
        set1.add(item)
    for item in [4, 5, 6, 7, 8]:
        set2.add(item)
    
    print(f"   集合1: {set1.to_list()}")
    print(f"   集合2: {set2.to_list()}")
    
    print("\n2. 集合操作:")
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)
    
    print(f"   并集: {union_set.to_list()}")
    print(f"   交集: {intersection_set.to_list()}")
    print(f"   差集: {difference_set.to_list()}")
    
    print("\n=== 哈希表应用演示 ===")
    
    print("1. 查找重复元素:")
    test_array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 1]
    duplicates = HashTableApplications.find_duplicates(test_array)
    print(f"   数组: {test_array}")
    print(f"   重复元素: {duplicates}")
    
    print("\n2. 两数之和:")
    nums = [2, 7, 11, 15]
    target = 9
    result = HashTableApplications.two_sum(nums, target)
    print(f"   数组: {nums}, 目标: {target}")
    print(f"   结果索引: {result}")
    
    print("\n3. 单词频率统计:")
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    word_freq = HashTableApplications.word_frequency(text)
    print(f"   文本: '{text}'")
    print("   词频统计:")
    for word, count in word_freq:
        print(f"     {word}: {count}")


if __name__ == "__main__":
    demo()