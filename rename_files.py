import os

folder_path = "Photos"  # folder path to where photos are stored
prefix = "image_"       #  prefix for photos

for index, filename in enumerate(os.listdir(folder_path)):
    # Construct new name for each photo
    extension = os.path.splitext(filename)[1]
    new_filename = prefix + str(index) + extension
    
    # rename the file
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    
print("All files in the folder have been renamed with the prefix:", prefix)
