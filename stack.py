"""
栈实现练习demo
包含基于数组和链表的栈实现
"""

class ArrayStack:
    """基于数组的栈实现"""
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity
    
    def push(self, item):
        """入栈"""
        if self.capacity and len(self.items) >= self.capacity:
            raise OverflowError("Stack overflow")
        self.items.append(item)
    
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取栈的大小"""
        return len(self.items)
    
    def display(self):
        """显示栈内容（从栈底到栈顶）"""
        return self.items.copy()


class StackNode:
    """栈节点"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """基于链表的栈实现"""
    def __init__(self):
        self.head = None
        self._size = 0
    
    def push(self, item):
        """入栈"""
        new_node = StackNode(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.data
    
    def is_empty(self):
        """检查栈是否为空"""
        return self.head is None
    
    def size(self):
        """获取栈的大小"""
        return self._size
    
    def display(self):
        """显示栈内容（从栈顶到栈底）"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


class StackApplications:
    """栈的应用示例"""
    
    @staticmethod
    def is_balanced_parentheses(expression):
        """检查括号是否平衡"""
        stack = ArrayStack()
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in pairs:
                stack.push(char)
            elif char in pairs.values():
                if stack.is_empty():
                    return False
                top = stack.pop()
                if pairs[top] != char:
                    return False
        
        return stack.is_empty()
    
    @staticmethod
    def infix_to_postfix(expression):
        """中缀表达式转后缀表达式"""
        stack = ArrayStack()
        postfix = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    postfix.append(stack.pop())
                stack.pop()
            elif char in precedence:
                while (not stack.is_empty() and 
                       stack.peek() != '(' and 
                       precedence.get(stack.peek(), 0) >= precedence[char]):
                    postfix.append(stack.pop())
                stack.push(char)
        
        while not stack.is_empty():
            postfix.append(stack.pop())
        
        return ''.join(postfix)
    
    @staticmethod
    def evaluate_postfix(expression):
        """计算后缀表达式"""
        stack = ArrayStack()
        
        for char in expression:
            if char.isdigit():
                stack.push(int(char))
            elif char in '+-*/':
                if stack.size() < 2:
                    raise ValueError("Invalid expression")
                
                b = stack.pop()
                a = stack.pop()
                
                if char == '+':
                    result = a + b
                elif char == '-':
                    result = a - b
                elif char == '*':
                    result = a * b
                elif char == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    result = a / b
                
                stack.push(result)
        
        if stack.size() != 1:
            raise ValueError("Invalid expression")
        
        return stack.pop()
    
    @staticmethod
    def decimal_to_binary(number):
        """十进制转二进制"""
        if number == 0:
            return "0"
        
        stack = ArrayStack()
        
        while number > 0:
            stack.push(number % 2)
            number //= 2
        
        binary = ""
        while not stack.is_empty():
            binary += str(stack.pop())
        
        return binary


def demo():
    """演示栈操作"""
    print("=== 基于数组的栈演示 ===")
    
    stack1 = ArrayStack()
    
    print("1. 入栈操作:")
    for i in [1, 2, 3, 4, 5]:
        stack1.push(i)
        print(f"   入栈 {i}: {stack1.display()}")
    
    print("\n2. 栈顶元素:")
    print(f"   栈顶: {stack1.peek()}")
    
    print("\n3. 出栈操作:")
    while not stack1.is_empty():
        popped = stack1.pop()
        print(f"   出栈 {popped}: {stack1.display()}")
    
    print("\n=== 基于链表的栈演示 ===")
    
    stack2 = LinkedStack()
    
    print("1. 入栈操作:")
    for i in ['A', 'B', 'C', 'D']:
        stack2.push(i)
        print(f"   入栈 {i}: {stack2.display()}")
    
    print(f"\n2. 栈大小: {stack2.size()}")
    
    print("\n3. 出栈操作:")
    for _ in range(2):
        popped = stack2.pop()
        print(f"   出栈 {popped}: {stack2.display()}")
    
    print("\n=== 栈应用演示 ===")
    
    print("1. 括号平衡检查:")
    expressions = ["()", "()[]{}", "((()))", "([)]", "((()"]
    for expr in expressions:
        result = StackApplications.is_balanced_parentheses(expr)
        print(f"   '{expr}' 平衡: {result}")
    
    print("\n2. 中缀转后缀:")
    infix = "a+b*c"
    postfix = StackApplications.infix_to_postfix(infix)
    print(f"   {infix} -> {postfix}")
    
    print("\n3. 计算后缀表达式:")
    postfix_expr = "23*1+"
    result = StackApplications.evaluate_postfix(postfix_expr)
    print(f"   {postfix_expr} = {result}")
    
    print("\n4. 十进制转二进制:")
    numbers = [10, 25, 42]
    for num in numbers:
        binary = StackApplications.decimal_to_binary(num)
        print(f"   {num} -> {binary}")


if __name__ == "__main__":
    demo()