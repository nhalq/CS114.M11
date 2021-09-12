_Stats, _Time = map(int, input().split())
_Time = _Time % (2 * _Stats)
print(_Time if _Time <= _Stats else _Stats - (_Time - _Stats))
