import os
from datetime import datetime

# Directory where the files are located
directory = '.'

# Rename the files based on their creation date
for filename in os.listdir(directory):
    # Skip directories
    if not os.path.isfile(os.path.join(directory, filename)):
        continue
    
    # Get the path to the file
    file_path = os.path.join(directory, filename)
    
    # Get the creation time of the file and format it
    creation_time = os.path.getctime(file_path)
    date_str = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
    
    # Prepare the new file name
    name, extension = os.path.splitext(filename)
    new_name = f"{date_str}_{name}{extension}"
    
    # Rename the file
    os.rename(file_path, os.path.join(directory, new_name))
    print(f"Renamed {filename} to {new_name}")

if __name__ == '__main__':
    main()