print('\n'.join(map(str, [int(1 / int(input()) * (sum([int(i) for i in input().split()]) - 1)) + 1 for _ in range(int(input()))])))
