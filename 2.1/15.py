# В ожидании доставки

N, M, T = map(int, (input() for i in range(3)))

end_time_in_minutes = N * 60 + M + T
hours = end_time_in_minutes // 60 % 24
minutes = end_time_in_minutes % 60

print(f"{hours:0>2}:{minutes:0>2}")
