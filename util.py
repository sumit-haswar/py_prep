from typing import List
from random import randint

def generate_random_list(count: int) -> List[int]:
    list = []
    for _ in range(0, count):
        num = randint(1,100)
        list.append(num)
    return list

def generate_distinct_random_list(count: int) -> List[int]:
    map = set()
    for _ in range(0, count):
        num = randint(1,100)
        while num in map:
            num = randint(1,100)
        map.add(num)
    return [val for val in map]
