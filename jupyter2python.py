#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import nbformat
from nbconvert import PythonExporter

# Function to convert a notebook file to a python file
def convert_notebook(notebook_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as file:
        nb = nbformat.read(file, as_version=4)
    
    # Convert to Python script
    exporter = PythonExporter()
    python_script, _ = exporter.from_notebook_node(nb)
    
    return python_script

# Directory where the .ipynb files are located
directory = '.'

# Convert each .ipynb file in the directory
for file in os.listdir(directory):
    if file.endswith('.ipynb'):
        # Get the new .py file name
        python_file_name = os.path.splitext(file)[0] + '.py'
        
        # Convert the notebook and get the python script
        python_script = convert_notebook(file)
        
        # Write the python script to the new file
        with open(python_file_name, 'w', encoding='utf-8') as python_file:
            python_file.write(python_script)
        
        print(f"Converted {file} to {python_file_name}")

