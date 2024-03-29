[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42885)

# 문제 설명

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.


**제한사항**
---------

 * 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
 * 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
 * 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
 * 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.


**입출력 예**
-------------

people	| limit	| return
---|---|---
[70, 50, 80, 50]	| 100	| 3
[70, 80, 50]	| 100	| 3



# 풀이
```python
from collections import deque

def solution(people, limit): 
    people.sort()
    people = deque(people)
    answer = 0
    while len(people) > 1:
        if(people[0] + people[-1]) <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()
        answer += 1
    return answer + len(people)
```
정답 보다는 효율성 개선이 중요한 문제

정렬된 deque에서 가장 큰 요소와 가장 작은 요소를 이용하면 효율적으로 해결 가능

현 시점에서 가장 가벼운 사람과 가장 무거운 사람을 비교하여 보트 제한을 넘지 않으면 출발 (보트 탑승 제한이 2인이므로 가능)

그렇지 않다면 가장 무거운 사람을 혼자 출발 시킨다. (Greedy)


초기 해결 방법의 문제점
--------------
처음에는 이중 for문을 사용한 방법으로 구현하였으나 테스트 케이스는 모두 통과해도 효율성 검사를 하나도 통과하지 못했다. 

최근 코딩테스트에서도 이중 반복문을 사용해서 효율성 검사 하나를 통과하지 못했었는데 이 문제를 잘 기억해야겠음



효율성 비교
------

이중 반복문 사용 | 양방향 deque 사용
---|---
![image](https://user-images.githubusercontent.com/102650903/183052313-e12247ca-f091-42b6-b349-e80eac79b36f.png) | ![image](https://user-images.githubusercontent.com/102650903/183052401-31947308-9c94-4aa0-85e9-49b7f3e9b349.png)


