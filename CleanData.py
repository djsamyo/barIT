import os

directory = 'Dataset/Original'
x = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if "Canny" in f:
        print(f)
        x += 1
        os.remove(f)
    # if os.path.isfile(file_path):
    #   os.remove(file_path)
    #   print("File has been deleted")
    # else:
    #   print("File does not exist")
