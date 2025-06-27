# Доставка

A, B, C = map(int, (input() for i in range(3)))

route_length = B - A
travel_time = route_length / C

print(f"{travel_time:.2f}")