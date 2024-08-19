def my_range(start=None, stop=None, step=None):
    if start != None and stop == None and step == None:
        stop = start
        start = 0
        while start < stop:
            yield start
            start += 1
    
    if start != None and stop != None and step == None:
        while start < stop:
            yield start
            start += 1
    
    if start != None and stop != None and step != None:
        while start < stop:
            yield start
            start += step

print(list(my_range(10)))
print(list(my_range(2, 20)))
print(list(my_range(3, 30, 3)))