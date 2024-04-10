#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime

# Function to calculate age
def calculate_age(birthdate, on_date):
    return on_date.year - birthdate.year - ((on_date.month, on_date.day) < (birthdate.month, birthdate.day))

# Prompt for birthday and convert to datetime object
birthday_str = input("Enter your birthday (mm/dd/yyyy): ")
birthday = datetime.strptime(birthday_str, "%m/%d/%Y")

# Get the current date
current_date = datetime.now()

# Calculate current age
current_age = calculate_age(birthday, current_date)

# Prompt for a future date and convert to datetime object
future_date_str = input("Enter a future date (mm/dd/yyyy): ")
future_date = datetime.strptime(future_date_str, "%m/%d/%Y")

# Calculate future age
future_age = calculate_age(birthday, future_date)

# Output the results
print(f"Birthday: {birthday.strftime('%m/%d/%Y')}")
print(f"Current day: {current_date.strftime('%m/%d/%Y')} - Current Age: {current_age}")
print(f"Future date: {future_date.strftime('%m/%d/%Y')} - Age will be: {future_age}")

