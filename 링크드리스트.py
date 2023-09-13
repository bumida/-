#!/usr/bin/env python
# coding: utf-8

# # 링크드 리스트 (Linked List)
# 
# 1. 링크드 리스트 (Linked List) 구조
# 연결 리스트라고도 함
# 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조 이 구조를 단점을 극복하기위해서 링크드리스트
# 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조(데이터를 추가적으로 추가할수있다)
# 본래 C언어에서는 주요한 데이터 구조지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원
# 
#    링크드 리스트 기본 구조와 용어
#    노드(Node) : 데이터 저장 단위 (데이터값, 포인터)로 구성
#    포인터(pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
#
# In[1]:


# 노드 구현
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None    


# In[1]:


class Node:
    def _init_(self, data, next=None):
        self.data = data
        self.next = next


# In[3]:


# Node와 Node 연결하기 (포인터 활용)
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1  

# 링크드 리스트로 데이터 추가하기
class Node:
    def _init_(self, data, next=Node):
        self.data = data
        self.data = next
        
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)   
    
node1 = Node(1)
node2 = node1
for index in range(2,10):
    add(index)
    
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)


# # 링크드 리스트의 장단점 (전통적인 C언어에서의 배열과 링크드 리스트)
# 
#  
