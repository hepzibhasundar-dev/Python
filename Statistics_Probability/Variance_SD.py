#Calculate variance and standard deviation
def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

def std_dev(data):
    return variance(data) ** 0.5
