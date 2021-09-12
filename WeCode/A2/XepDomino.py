from functools import reduce
print(reduce((lambda _0, _1: _0 * _1), map(int, input().split())) // 2)
