n = int(input()) 
m = int(input())
t = int(input())

time = n * 60 + m + t
hour = (time // 60) % 24
minute = time % 60

print(f'{hour:0>2}:{minute:0>2}')