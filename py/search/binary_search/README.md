# 이진 탐색 Binary Search 
- 살펴보는 범위를 절반 씩 줄여가며 답을 찾는다. 
- 탐색 전에 반드시 정렬이 되어있어야 한다. 
- 시간 복잡도 O(logN), 정렬을 같이 하면 O(NlogN)
- 탐색을 여러번 반복할 때 사용하기 좋다. 
  - 선형 탐색 O(N) N번 -> O(N^2)
  - 이진 탐색 O(logN) N번 -> O(NlogN)

## 이진탐색 라이브러리
### C++ - lower/upper_bound
```
vector<int> v = {0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9}
int three = upper_bound(v.begin(), v.end(), 3) - lower_bound(v.begin(), v.end(), 3) 
int four = upper_bound(v.begin(), v.end(), 3) - lower_bound(v.begin(), v.end(), 3) 
int six = upper_bound(v.begin(), v.end(), 3) - lower_bound(v.begin(), v.end(), 3)
printf("number of 3: %d\n", three); // 2 
printf("number of 4: %d\n", four);  // 0
printf("number of 6: %d\n", six);   // 3 
```
- `upper_bound(시작점, 끝점, 찾을 수)` 하면 찾는 값 초과의 가장 작은 인덱스를 반환한다.
- `lower_bound(시작점, 끝점, 찾을 수)` 하면 찾는 값 이상의 가장 작은 인덱스를 반환한다.

### Python - bisect_left/right
```python
from bisect import bisect_right, bisect_left
v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3) # 4 - 2
four = bisect_right(v, 4) - bisect_left(v, 4) # 4 - 4
six = bisect_right(v, 6) - bisect_left(v, 6) # 7 - 4
print(f'number of 3: {three}') # 2
print(f'number of 4: {four}')  # 0 
print(f'number of 6: {six}')   # 3
```
- `bisect_right` 찾는 값 초과의 가장 작은 인덱스를 반환한다. 
- `bisect_left` 찾는 값 이상의 가장 작은 인덱스를 반환한다. 


## Parametric Search - 매개변수 탐색
- 최적화 문제를 결중 문제로 바꿔 이진탐색으로 푸는 방법
  - 최적화 문제 Optimization Problem 
    -> 문제 상황을 만족하는 변수의 최솟값, 최댓값을 구하는 문제 
  - 결정 문제 Decision Problem 
    Yes/No 문제
  - 매개변수 Parameter가 주어지면 True / False 가 결정되어야 한다
  - 가능한 해의 영역이 연속적이어야 한다
  - 범위를 반씩 줄여가면서 가운데 값이 True인지 False인지 구한다
  - 이진탐색과 똑같은 원리