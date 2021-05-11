#!/usr/bin/env python
# coding: utf-8

#  꼭 알아두어야할 자료구조 : 스택 (Stack)
#  데이터를 제한적으로 접근할 수 있는 구조
#  한쪽 긑에서만 자료를 넣거나 뺄 수 있는 구조
#  가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
# 
#  스택은 LIFO (Last in, First Out) 또는 FILO(First in, Last Out) 데이터 관리 방식을 따름
#  LIFO : 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책
#  FILO : 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책
# 
#  대표적인 스택의 활용
#     컴퓨터 내부의 프로세스 구조의 함수 동작 방식
#  주요 기능
#     push() : 데이터를 스택에 넣기
#     pop() : 데이터를 스택에서 꺼내기

# In[3]:


# 재귀 함수
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)


# In[4]:


recursive(4)


# 스택은 단순하고 빠른 성능을 위해 사용되므로, 보통 배열 구조를 활용해서 구현하는 것이 일반적임, 이 같은 경우, 위에서 열거한 단점이 있을 수 있다.
# 
# 

# In[16]:


stack_list = list()

def push(data):
    stack_list.append(data)
    
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


# In[17]:


for index in range(10):
    push(index)


# In[18]:


pop() 


# In[ ]:




