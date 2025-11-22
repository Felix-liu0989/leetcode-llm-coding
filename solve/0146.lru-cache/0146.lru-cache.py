'''
@index 146
@title LRU 缓存
@difficulty 中等
@tags design,hash-table,linked-list,doubly-linked-list
@draft false
@link https://leetcode.cn/problems/lru-cache/description/
@frontendId 146
@solved false
'''


# LRU算法 get和put操作的实现
# get操作：如果key存在，则返回对应的value，并将该节点移到链表头部；如果key不存在，则返回-1
# put操作：如果key存在，则更新对应的value，并将该节点移到链表头部；如果key不存在，则创建新的节点，并插入到链表头部
# 如果链表满了，则删除链表头部的节点
# 如果链表未满，则直接插入到链表尾部

from typing import Optional
class Node:
    __slots__ = "key","val","prev","next"
    def __init__(self,key=0,value=0):
        self.key = key
        self.val = value

class LRUCache:
    def __init__(self,capacity:int):
        self.cap = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.key_to_node = {}
        
    def get_node(self,key:int)-> Optional[Node]:
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.add_to_head(node)
        return node
        
    def get(self,key:int)-> int:
        node = self.get_node(key)
        return node.val if node else -1
    
    def put(self,key:int,value:int):
        node = self.get_node(key)
        if node:
            node.val = value
            return
        
        new_node = Node(key,value)
        self.key_to_node[key] = new_node
        self.add_to_head(new_node)
        
        if len(self.key_to_node) > self.cap:
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)
        
        
    def remove(self,node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.prev = None
        node.next = None
        
    def add_to_head(self,node:Node):
        node.prev = self.dummy
        node.next = self.dummy.next
        # dummy <- node -> dummy.next
        
        self.dummy.next.prev = node
        self.dummy.next = node
        # dummy <-> node <-> dummy.next
        
    