import numpy as np
import random

# 세 학생의 찍기 방식(pattern)

a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]

for i in range(1,2000):
    a += [1,2,3,4,5]
for i in range(1,1250):
    b += [2,1,2,3,2,4,2,5]
for i in range(1,1000):
    c += [3,3,1,1,2,2,4,4,5,5]
    
ans_list = []


# 5지 선다의 문제 10000개 풀이

for _ in range(10000):
    ans_list.append(random.randint(1,5))

    
correct_a = np.zeros(10000, dtype=int)
             
for i in range(10000):
    if a[i] == ans_list[i]:
        correct_a[i]=1
    elif a[i] !=ans_list[i]:
        correct_a[i]=0   
sum_a = np.sum(correct_a)

correct_b = np.zeros(10000, dtype=int)
             
for i in range(10000):
    if b[i] == ans_list[i]:
        correct_b[i]=1
    elif b[i] !=ans_list[i]:
        correct_b[i]=0

sum_b = np.sum(correct_b)

correct_c = np.zeros(10000, dtype=int)
             
for i in range(10000):
    if c[i] == ans_list[i]:
        correct_c[i]=1
    elif c[i] !=ans_list[i]:
        correct_c[i]=0

sum_c = np.sum(correct_c)

# 각 학생이 찍어서 맞춘 개수 순서로 정렬

list_rank = {"1번학생" : sum_a,"2번학생" : sum_b, "3번학생" : sum_c}
print(list_rank)
sort_rank = sorted(list_rank.items(),key=lambda x:x[1], reverse = True)
print(sort_rank)

for key, value in sort_rank:
    print(key, ":" ,value, "개를 맞추었습니다.")

