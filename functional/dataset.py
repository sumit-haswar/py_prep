# | Name            | Field      | Born | Nobel Prize? |
# |-----------------|------------|------|--------------|
# | Ada Lovelace    | math       | 1815 | no           |
# | Emmy Noether    | math       | 1882 | no           |
# | Marie Curie     | math       | 1867 | yes          |
# | Tu Youyou       | physics    | 1930 | yes          |
# | Ada Yonath      | chemistry  | 1939 | yes          |
# | Vera Rubin      | chemistry  | 1928 | no           |
# | Sally Ride      | physics    | 1951 | no           |
import collections
from pprint import pprint
import itertools
from functools import reduce
import time
import multiprocessing
import os
import concurrent.futures

# tuple and named-tuples
Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel_prize'])
scientists = (
    Scientist('Ada Lovelace', 'math', 1815, False),
    Scientist('Emmy Noether', 'math', 1882, False),
    Scientist('Marie Curie', 'math', 1867, True),
    Scientist('Tu Youyou', 'physics', 1930, True),
    Scientist('Ada Yonath', 'chemistry', 1939, True)
)
#filter

def nobel_filter(x):
    return x.nobel_prize is True

# pprint(tuple(filter(nobel_filter, scientists)))

#map
x = list(map(lambda s: s.name, scientists))

#reduce:
# print(reduce(lambda sum, curr: sum + ( 1 if curr.nobel_prize else 0 ),
#              scientists,
#              0))

def reducer(acc, curr):
    if curr.field in acc:
        acc[curr.field].append(curr.name)
    else:
        acc[curr.field] = []
        acc[curr.field].append(curr.name)
    return acc

grouped_list = reduce(reducer, scientists, {})

# you can also use a default-dict instead of a blank dict
default_dict = collections.defaultdict(list)
# pprint(grouped_list)

# itertools.groupby
grouped_dict = {item[0]: tuple(item[1])
                for item in itertools.groupby(scientists, lambda s: s.field)
                }

# pprint(grouped_dict)
# Section 5: Parallel Processing With multiprocessing

def transform(item):
    # print(f'Process {os.getpid()}, record {item.name}')
    time.sleep(1)
    return {'name': item.name,
            'age': 2020 - item.born}

start = time.time()
result = list(map(transform, scientists))
end = time.time()
print('result time: {0}'.format(end - start))


start = time.time()
pool = multiprocessing.Pool()
# pool = multiprocessing.Pool(processes=1, maxtasksperchild=2)
result2 = list(pool.map(transform, scientists))
end = time.time()
print('result2 time: {0}'.format(end - start))

# using concurrent.future, Python 3 only
start = time.time()
# concurrent.futures also provides ThreadPoolExecutor
with concurrent.futures.ProcessPoolExecutor() as executor:
    result3 = list(executor.map(transform, scientists))

end = time.time()
print('result3 time: {0}'.format(end - start))

# GIL (global interpreter lock) no two threads can execute python code at the same time
# to counter it one can use Process based parallel processing in Python
