import shutil

source_file = "/Users/timchik/Desktop/pp2/Practice-06/exm.txt"
destination_folder = "/Users/timchik/Desktop/pp2/Practice-06/parent"

shutil.move(source_file, destination_folder)
print("File moved")