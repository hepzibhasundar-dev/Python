from collections import Counter
def mean(data):
    return sum(data) / len(data)

def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 != 0 else (s[mid-1] + s[mid]) / 2

def mode(data):
    count = Counter(data)
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

data = [1, 2, 2, 3, 4, 4, 4, 5]
print(mean(data))
print(median(data))
print(mode(data))
