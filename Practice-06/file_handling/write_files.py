with open("/Users/timchik/Desktop/pp2/Practice-06/sample.txt", "a") as f:
    f.write("Line 3: Appended line\n")
    f.write("Line 4: Another appended line\n")

with open("/Users/timchik/Desktop/pp2/Practice-06/sample.txt", "r") as f:
    text=f.read()

print(text)