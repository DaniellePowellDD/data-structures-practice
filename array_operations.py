"""
数组基础操作练习demo
包含数组的增删改查、排序、查找等常用操作
"""

class ArrayOperations:
    def __init__(self):
        self.data = []
    
    def insert(self, index, value):
        """在指定位置插入元素"""
        self.data.insert(index, value)
        return self.data
    
    def append(self, value):
        """在数组末尾添加元素"""
        self.data.append(value)
        return self.data
    
    def delete(self, index):
        """删除指定位置的元素"""
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None
    
    def update(self, index, value):
        """更新指定位置的元素"""
        if 0 <= index < len(self.data):
            self.data[index] = value
            return True
        return False
    
    def find(self, value):
        """查找元素第一次出现的位置"""
        try:
            return self.data.index(value)
        except ValueError:
            return -1
    
    def binary_search(self, value):
        """二分查找（数组需要已排序）"""
        sorted_data = sorted(self.data)
        left, right = 0, len(sorted_data) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if sorted_data[mid] == value:
                return mid
            elif sorted_data[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def bubble_sort(self):
        """冒泡排序"""
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data
    
    def quick_sort(self, arr=None, low=0, high=None):
        """快速排序"""
        if arr is None:
            arr = self.data.copy()
        if high is None:
            high = len(arr) - 1
            
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)
        return arr
    
    def partition(self, arr, low, high):
        """快速排序的分区函数"""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def reverse(self):
        """反转数组"""
        self.data.reverse()
        return self.data
    
    def get_max(self):
        """获取最大值"""
        return max(self.data) if self.data else None
    
    def get_min(self):
        """获取最小值"""
        return min(self.data) if self.data else None
    
    def size(self):
        """获取数组大小"""
        return len(self.data)
    
    def is_empty(self):
        """判断数组是否为空"""
        return len(self.data) == 0
    
    def display(self):
        """显示数组内容"""
        return self.data


def demo():
    """演示数组操作"""
    print("=== 数组操作演示 ===")
    
    arr = ArrayOperations()
    
    print("1. 添加元素:")
    arr.append(5)
    arr.append(3)
    arr.append(8)
    arr.append(1)
    print(f"   添加后: {arr.display()}")
    
    print("\n2. 插入元素:")
    arr.insert(2, 7)
    print(f"   在位置2插入7: {arr.display()}")
    
    print("\n3. 更新元素:")
    arr.update(1, 9)
    print(f"   更新位置1为9: {arr.display()}")
    
    print("\n4. 查找元素:")
    pos = arr.find(8)
    print(f"   元素8的位置: {pos}")
    
    print("\n5. 删除元素:")
    deleted = arr.delete(0)
    print(f"   删除位置0的元素{deleted}: {arr.display()}")
    
    print("\n6. 冒泡排序:")
    print(f"   排序前: {arr.display()}")
    arr.bubble_sort()
    print(f"   排序后: {arr.display()}")
    
    print("\n7. 二分查找:")
    pos = arr.binary_search(7)
    print(f"   查找元素7的位置: {pos}")
    
    print("\n8. 数组信息:")
    print(f"   大小: {arr.size()}")
    print(f"   最大值: {arr.get_max()}")
    print(f"   最小值: {arr.get_min()}")
    print(f"   是否为空: {arr.is_empty()}")


if __name__ == "__main__":
    demo()