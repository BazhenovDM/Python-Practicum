# Поиск гор

def find_mountains(heights):
    return tuple(i + 1 for i in range(1, len(heights) - 1) if heights[i - 1] < heights[i] > heights[i + 1])
