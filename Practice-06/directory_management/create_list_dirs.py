import os
path = "/Users/timchik/Desktop/pp2/Practice-06/parent/child/grandchild"
os.makedirs(path, exist_ok=True)
print(f"Created directories: {path}")


path = "/Users/timchik/Desktop/pp2/Practice-06"
items = os.listdir(path)
for item in items:
    full_path = os.path.join(path, item)
    if os.path.isdir(full_path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")


search_path = "/Users/timchik/Desktop/pp2/Practice-06"
extension = ".txt"

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))