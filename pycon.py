# For Sullivan 2019 Pycon "FUN CODE" contest
import random
from functools import reduce

def quick_sort(left: int, right: int, array: list) -> None:
    """
    주어진 배열을 정렬... 할까?

    :param left: 구획의 가장 왼쪽
    :param right: 구획의 가장 오른쪽
    :param array: 정렬할 배열
    :retrun: 없음
    """

    # 기준이 되는 배열의 index를 맨 왼쪽 값으로 지정한다.
    pivot = left

    # 만일 순회할 범주가 없으면, 종료한다.
    if left >= right:
        return 

    # 해당 범주를 순회하다, 기준값보다 작거나 같으면 바꿔준다
    switch_point = pivot
    for i in range(left+1, right+1):
        if array[i] <= array[pivot]:
            switch_point += 1
            array[i], array[switch_point] = array[switch_point], array[i]

    # 순회가 종료될 때, switch_point를 기점으로 작은 것이 앞, 큰 것이 뒤에 존재하게 된다.
    array[pivot], array[switch_point] = array[switch_point], array[pivot]
    pivot = switch_point

    # pivot 값 기준으로 앞, 뒤 범위에 같은 일을 반복한다.
    quick_sort(left, pivot-1, array)
    quick_sort(pivot+1, right, array)


def validate(array: list) -> None:
    temp = -1
    for i in search:
        if temp > i:
            print("\033[91m✖ 실패했습니다.. 하지만 상관은 없죠!")
            return
        temp = i
    
    print("\033[92m✔ 성공했습니다!")


if __name__ == "__main__":
    search = list(range(1, 10000))
    random.shuffle(search)

    quick_sort(0, len(search)-1, search)

    # 제대로 정렬되었는지 확인하는 코드..인데
    # 제대로 정렬 되던 말던, 재미만 있으면 되잖아요?
    validate(search)
    