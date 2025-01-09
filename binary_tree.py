"""
二叉树实现练习demo
包含二叉树的创建、遍历、搜索等操作
"""

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    """二叉树实现"""
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """插入节点（层序插入）"""
        new_node = TreeNode(val)
        
        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = new_node
                return
            elif not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def preorder(self, node=None):
        """前序遍历（根-左-右）"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.append(node.val)
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
        return result
    
    def inorder(self, node=None):
        """中序遍历（左-根-右）"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.extend(self.inorder(node.left))
            result.append(node.val)
            result.extend(self.inorder(node.right))
        return result
    
    def postorder(self, node=None):
        """后序遍历（左-右-根）"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            result.append(node.val)
        return result
    
    def level_order(self):
        """层序遍历"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """计算树的高度"""
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def count_nodes(self, node=None):
        """计算节点数量"""
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def find(self, val, node=None):
        """查找节点"""
        if node is None:
            node = self.root
        
        if not node:
            return False
        
        if node.val == val:
            return True
        
        return self.find(val, node.left) or self.find(val, node.right)
    
    def find_path(self, val, node=None, path=None):
        """查找到指定值的路径"""
        if node is None:
            node = self.root
        if path is None:
            path = []
        
        if not node:
            return None
        
        path.append(node.val)
        
        if node.val == val:
            return path.copy()
        
        left_path = self.find_path(val, node.left, path)
        if left_path:
            return left_path
        
        right_path = self.find_path(val, node.right, path)
        if right_path:
            return right_path
        
        path.pop()
        return None


class BinarySearchTree:
    """二叉搜索树实现"""
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """插入节点"""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        """递归插入"""
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val):
        """搜索节点"""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        """递归搜索"""
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        return self._search_recursive(node.right, val)
    
    def delete(self, val):
        """删除节点"""
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        """递归删除"""
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            temp = self._find_min(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)
        
        return node
    
    def _find_min(self, node):
        """找到最小值节点"""
        while node.left:
            node = node.left
        return node
    
    def find_min(self):
        """找到最小值"""
        if not self.root:
            return None
        node = self._find_min(self.root)
        return node.val
    
    def find_max(self):
        """找到最大值"""
        if not self.root:
            return None
        
        node = self.root
        while node.right:
            node = node.right
        return node.val
    
    def inorder(self, node=None):
        """中序遍历（有序输出）"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.extend(self.inorder(node.left))
            result.append(node.val)
            result.extend(self.inorder(node.right))
        return result
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """验证是否为有效的二叉搜索树"""
        if node is None:
            node = self.root
        
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.val) and
                self.is_valid_bst(node.right, node.val, max_val))


class TreeApplications:
    """树的应用示例"""
    
    @staticmethod
    def expression_tree_evaluate(expression):
        """表达式树求值（简化版）"""
        if expression.isdigit():
            return int(expression)
        
        return expression
    
    @staticmethod
    def lowest_common_ancestor(root, p, q):
        """最近公共祖先"""
        if not root or root.val == p or root.val == q:
            return root
        
        left = TreeApplications.lowest_common_ancestor(root.left, p, q)
        right = TreeApplications.lowest_common_ancestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right
    
    @staticmethod
    def is_balanced(node):
        """判断是否为平衡二叉树"""
        def check_height(node):
            if not node:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return check_height(node) != -1


def demo():
    """演示二叉树操作"""
    print("=== 二叉树演示 ===")
    
    bt = BinaryTree()
    
    print("1. 插入节点:")
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        bt.insert(val)
    print(f"   插入 {values}")
    
    print("\n2. 遍历操作:")
    print(f"   前序遍历: {bt.preorder()}")
    print(f"   中序遍历: {bt.inorder()}")
    print(f"   后序遍历: {bt.postorder()}")
    print(f"   层序遍历: {bt.level_order()}")
    
    print(f"\n3. 树的属性:")
    print(f"   高度: {bt.height()}")
    print(f"   节点数: {bt.count_nodes()}")
    
    print(f"\n4. 查找操作:")
    search_val = 5
    found = bt.find(search_val)
    path = bt.find_path(search_val)
    print(f"   查找 {search_val}: {found}")
    print(f"   路径: {path}")
    
    print("\n=== 二叉搜索树演示 ===")
    
    bst = BinarySearchTree()
    
    print("1. 插入节点:")
    bst_values = [50, 30, 70, 20, 40, 60, 80]
    for val in bst_values:
        bst.insert(val)
    print(f"   插入 {bst_values}")
    
    print(f"\n2. 中序遍历（有序）: {bst.inorder()}")
    
    print(f"\n3. 搜索操作:")
    search_val = 40
    found_node = bst.search(search_val)
    print(f"   搜索 {search_val}: {'找到' if found_node else '未找到'}")
    
    print(f"\n4. 最值查找:")
    print(f"   最小值: {bst.find_min()}")
    print(f"   最大值: {bst.find_max()}")
    
    print(f"\n5. 验证BST: {bst.is_valid_bst()}")
    
    print("\n6. 删除节点:")
    print(f"   删除前: {bst.inorder()}")
    bst.delete(30)
    print(f"   删除30后: {bst.inorder()}")
    
    print("\n=== 树的应用演示 ===")
    
    print("1. 构建测试树:")
    test_tree = BinaryTree()
    for val in [3, 5, 1, 6, 2, 0, 8, 7, 4]:
        test_tree.insert(val)
    
    print("2. 平衡性检查:")
    is_balanced = TreeApplications.is_balanced(test_tree.root)
    print(f"   树是否平衡: {is_balanced}")


if __name__ == "__main__":
    demo()