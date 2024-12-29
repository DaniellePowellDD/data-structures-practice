"""
链表实现练习demo
包含单向链表和双向链表的基本操作
"""

class ListNode:
    """链表节点"""
    def __init__(self, val=0):
        self.val = val
        self.next = None

class DoublyListNode:
    """双向链表节点"""
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    """单向链表"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """在链表末尾添加节点"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, val):
        """在链表头部添加节点"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, val):
        """在指定位置插入节点"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, val):
        """删除指定值的第一个节点"""
        if not self.head:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def delete_at(self, index):
        """删除指定位置的节点"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        self.size -= 1
    
    def find(self, val):
        """查找值，返回索引"""
        current = self.head
        index = 0
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        """获取指定位置的值"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for i in range(index):
            current = current.next
        return current.val
    
    def reverse(self):
        """反转链表"""
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
    
    def display(self):
        """显示链表内容"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None
    
    def length(self):
        """获取链表长度"""
        return self.size

class DoublyLinkedList:
    """双向链表"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, val):
        """在链表末尾添加节点"""
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def prepend(self, val):
        """在链表头部添加节点"""
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, val):
        """删除指定值的第一个节点"""
        current = self.head
        
        while current:
            if current.val == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            current = current.next
        return False
    
    def display_forward(self):
        """正向显示链表内容"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def display_backward(self):
        """反向显示链表内容"""
        result = []
        current = self.tail
        while current:
            result.append(current.val)
            current = current.prev
        return result
    
    def length(self):
        """获取链表长度"""
        return self.size


def demo():
    """演示链表操作"""
    print("=== 单向链表演示 ===")
    
    ll = LinkedList()
    
    print("1. 添加元素:")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print(f"   添加后: {ll.display()}")
    
    print("\n2. 插入元素:")
    ll.insert(2, 1.5)
    print(f"   在位置2插入1.5: {ll.display()}")
    
    print("\n3. 查找元素:")
    pos = ll.find(2)
    print(f"   元素2的位置: {pos}")
    
    print("\n4. 获取元素:")
    val = ll.get(3)
    print(f"   位置3的元素: {val}")
    
    print("\n5. 删除元素:")
    ll.delete(1.5)
    print(f"   删除1.5后: {ll.display()}")
    
    print("\n6. 反转链表:")
    ll.reverse()
    print(f"   反转后: {ll.display()}")
    
    print(f"\n7. 链表长度: {ll.length()}")
    
    print("\n=== 双向链表演示 ===")
    
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.prepend(5)
    
    print(f"正向遍历: {dll.display_forward()}")
    print(f"反向遍历: {dll.display_backward()}")
    
    dll.delete(20)
    print(f"删除20后正向遍历: {dll.display_forward()}")
    print(f"链表长度: {dll.length()}")


if __name__ == "__main__":
    demo()