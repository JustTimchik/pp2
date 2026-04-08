names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for index, name in enumerate(names):
    print(f"{index}: {name}")

for name, score in zip(names, scores):
    print(f"{name} scored {score}")


values = ["10", "20", 30, 40.5]

converted = []

for v in values:
    if isinstance(v, str):
        converted.append(int(v))  # convert string to int
    elif isinstance(v, float):
        converted.append(int(v))  # convert float to int
    else:
        converted.append(v)

print("Converted:", converted)

a = "123"
b = float(a)
c = int(b)

print(type(a), type(b), type(c))