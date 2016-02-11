def squared(num):
    try:
        return int(num) ** 2
    except ValueError:
        return num * len(num)

print(squared(5))
print(squared('2'))
print(squared('tim'))