#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


# 1차원 배열: 리스트로 구현시
data = [1,2,3,4,5]
print(data)


# In[6]:


# 2차원 배열: 리스트로 구현시
data = [[1,2,3], [4,5,6],[7,8,9]]
print(data[0])
print(data[0][1])
print(data[2][2])
print(data[2][1])
print(data[2][0])


# # 대표적인 데이터 구조 : 큐 (Queue)

# In[7]:


### 가장 먼저 넣은 데이터를 가장 먼저  꺼낼 수 있는 구조 (FIFO) first in first out
# 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
# queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue()
# 프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용
# Queue() : 가장 일반적인 큐 자료 구조
# LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조라고 보면 됨)
# PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

# 일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음


# In[12]:


# Queue()로 큐 만들기 (가장 일반적인 큐, FIFO(First-in, First-Out))
import queue

data_queue = queue.Queue()

data_queue.put("hello world")
data_queue.put(1)


# In[14]:


data_queue.qsize()
data_queue.get()


# In[15]:


data_queue.qsize()


# In[22]:


# PriorityQueue()로 큐 만들기 첫번째튜플에 항목이 '우선순위' 두번째가 '데이터'
import queue

data_queue = queue.PriorityQueue()

data_queue.put((10,"data"))
data_queue.put((5, "2"))
data_queue.put((16, "third data"))


# In[19]:


data_queue.qsize()


# In[23]:


data_queue.get()


# In[24]:


data_queue.get()


# In[29]:


# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

queue_list = list()  
    
def enqueue(data):
    queue_list.append(data)
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


# In[30]:


for index in range(10):
    enqueue(index)


# In[27]:


len(queue_list)


# In[31]:


dequeue()


# In[ ]:




