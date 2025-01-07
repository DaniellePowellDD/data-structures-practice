"""
队列实现练习demo
包含基于数组和链表的队列实现，以及循环队列和双端队列
"""

class ArrayQueue:
    """基于数组的队列实现"""
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity
    
    def enqueue(self, item):
        """入队"""
        if self.capacity and len(self.items) >= self.capacity:
            raise OverflowError("Queue overflow")
        self.items.append(item)
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """查看队头元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def rear(self):
        """查看队尾元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取队列大小"""
        return len(self.items)
    
    def display(self):
        """显示队列内容"""
        return self.items.copy()


class QueueNode:
    """队列节点"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """基于链表的队列实现"""
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0
    
    def enqueue(self, item):
        """入队"""
        new_node = QueueNode(item)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self._size += 1
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.front_node.data
        self.front_node = self.front_node.next
        
        if self.front_node is None:
            self.rear_node = None
        
        self._size -= 1
        return data
    
    def front(self):
        """查看队头元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front_node.data
    
    def rear(self):
        """查看队尾元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear_node.data
    
    def is_empty(self):
        """检查队列是否为空"""
        return self.front_node is None
    
    def size(self):
        """获取队列大小"""
        return self._size
    
    def display(self):
        """显示队列内容"""
        result = []
        current = self.front_node
        while current:
            result.append(current.data)
            current = current.next
        return result


class CircularQueue:
    """循环队列实现"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item):
        """入队"""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def front_item(self):
        """查看队头元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    
    def rear_item(self):
        """查看队尾元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.rear]
    
    def is_empty(self):
        """检查队列是否为空"""
        return self.size == 0
    
    def is_full(self):
        """检查队列是否已满"""
        return self.size == self.capacity
    
    def get_size(self):
        """获取队列大小"""
        return self.size
    
    def display(self):
        """显示队列内容"""
        if self.is_empty():
            return []
        
        result = []
        i = self.front
        for _ in range(self.size):
            result.append(self.queue[i])
            i = (i + 1) % self.capacity
        return result


class Deque:
    """双端队列实现"""
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        """从前端添加元素"""
        self.items.insert(0, item)
    
    def add_rear(self, item):
        """从后端添加元素"""
        self.items.append(item)
    
    def remove_front(self):
        """从前端移除元素"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)
    
    def remove_rear(self):
        """从后端移除元素"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()
    
    def front(self):
        """查看前端元素"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]
    
    def rear(self):
        """查看后端元素"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]
    
    def is_empty(self):
        """检查双端队列是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取双端队列大小"""
        return len(self.items)
    
    def display(self):
        """显示双端队列内容"""
        return self.items.copy()


class QueueApplications:
    """队列应用示例"""
    
    @staticmethod
    def hot_potato(names, num):
        """烫手山芋游戏（约瑟夫问题）"""
        queue = ArrayQueue()
        for name in names:
            queue.enqueue(name)
        
        while queue.size() > 1:
            for _ in range(num):
                queue.enqueue(queue.dequeue())
            queue.dequeue()
        
        return queue.dequeue()
    
    @staticmethod
    def is_palindrome(string):
        """使用双端队列检查回文"""
        deque = Deque()
        for char in string.lower():
            if char.isalpha():
                deque.add_rear(char)
        
        while deque.size() > 1:
            if deque.remove_front() != deque.remove_rear():
                return False
        
        return True


def demo():
    """演示队列操作"""
    print("=== 基于数组的队列演示 ===")
    
    queue1 = ArrayQueue()
    
    print("1. 入队操作:")
    for i in [1, 2, 3, 4]:
        queue1.enqueue(i)
        print(f"   入队 {i}: {queue1.display()}")
    
    print(f"\n2. 队头元素: {queue1.front()}")
    print(f"   队尾元素: {queue1.rear()}")
    
    print("\n3. 出队操作:")
    for _ in range(2):
        dequeued = queue1.dequeue()
        print(f"   出队 {dequeued}: {queue1.display()}")
    
    print("\n=== 基于链表的队列演示 ===")
    
    queue2 = LinkedQueue()
    
    print("1. 入队操作:")
    for char in ['A', 'B', 'C']:
        queue2.enqueue(char)
        print(f"   入队 {char}: {queue2.display()}")
    
    print(f"\n2. 队列大小: {queue2.size()}")
    
    print("\n3. 出队操作:")
    while not queue2.is_empty():
        dequeued = queue2.dequeue()
        print(f"   出队 {dequeued}: {queue2.display()}")
    
    print("\n=== 循环队列演示 ===")
    
    cqueue = CircularQueue(5)
    
    print("1. 填满队列:")
    for i in range(5):
        cqueue.enqueue(i)
        print(f"   入队 {i}: {cqueue.display()}")
    
    print("\n2. 部分出队后再入队:")
    for _ in range(2):
        dequeued = cqueue.dequeue()
        print(f"   出队 {dequeued}: {cqueue.display()}")
    
    for i in [5, 6]:
        cqueue.enqueue(i)
        print(f"   入队 {i}: {cqueue.display()}")
    
    print("\n=== 双端队列演示 ===")
    
    deque = Deque()
    
    print("1. 双端添加:")
    deque.add_front(1)
    print(f"   前端添加1: {deque.display()}")
    deque.add_rear(2)
    print(f"   后端添加2: {deque.display()}")
    deque.add_front(0)
    print(f"   前端添加0: {deque.display()}")
    deque.add_rear(3)
    print(f"   后端添加3: {deque.display()}")
    
    print("\n2. 双端移除:")
    front = deque.remove_front()
    print(f"   前端移除{front}: {deque.display()}")
    rear = deque.remove_rear()
    print(f"   后端移除{rear}: {deque.display()}")
    
    print("\n=== 队列应用演示 ===")
    
    print("1. 烫手山芋游戏:")
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    winner = QueueApplications.hot_potato(names, 3)
    print(f"   参与者: {names}")
    print(f"   每次传递3次，获胜者: {winner}")
    
    print("\n2. 回文检查:")
    test_strings = ["radar", "hello", "level", "python"]
    for s in test_strings:
        is_pal = QueueApplications.is_palindrome(s)
        print(f"   '{s}' 是回文: {is_pal}")


if __name__ == "__main__":
    demo()