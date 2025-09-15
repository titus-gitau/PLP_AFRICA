# WEEK 1:BASIC  CALCULATOR PROGRAM
I created a simple calculator program  that does the following using python programming language :
The program intakes two float type numbers and peroforms various basic math operations(sum,subtraction,product,division,modulus).
The program then outputs the results of this operations.


# WEEK 2 ASSIGNMENT: LISTS AND LISTS MANIPULATIONS 
## Objectives 

->Create an empty list called my_list.

->Append the following elements to my_list: 10, 20, 30, 40.

->Insert the value 15 at the second position in the list.

->Extend my_list with another list: [50, 60, 70].

->Remove the last element from my_list.

->Sort my_list in ascending order.

->Find and print the index of the value 30 in my_list.



# WEEK 3 Assignment: Discount Calculator in Python

## 📌 Assignment Description
Create a function named `calculate_discount(price, discount_percent)` that calculates the final price after applying a discount.  
The function should take the original price (`price`) and the discount percentage (`discount_percent`) as parameters.  

- If the discount is **20% or higher**, apply the discount.  
- Otherwise, return the original price.  

Using the `calculate_discount` function, prompt the user to enter the original price of an item and the discount percentage.  
Print the final price after applying the discount, or if no discount was applied, print the original price.


## Solution Overview
The program is divided into two parts:
1. **Function Definition**  
   - `calculate_discount(price, discount_percent)` checks if the discount is at least 20%.  
   - If true, it applies the discount and returns the reduced price.  
   - If false, it simply returns the original price.

2. **User Interaction**  
   - Prompts the user to enter the original price of an item.  
   - Prompts the user to enter the discount percentage.  
   - Calls the function and prints the final result.  


# WEEK 4: File Read & Write with Error Handling in Python

This is a simple Python program I wrote while learning **file handling** and **error handling**.  
It asks the user for a filename, reads the file, modifies its contents, and saves the result into a **new file**.  

## Features
- Asks the user to type a filename.
- Reads the file if it exists.
- Converts all text to **UPPERCASE** (you can change this to other modifications).
- Handles common errors such as:
  - File not found. 
  - Permission denied. 
  - Other unexpected errors.


# WEEK 5:Assignment 1:-> Design Your Own Class! 

Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

Designed a Smartphone class with attributes like brand, model, storage, and methods such as make_call() and charge().
A subclass Smartwatch inherits from Smartphone and overrides some behavior to demonstrate polymorphism.

## Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

Created an Animal base class and subclasses (Dog, Bird, Fish) that all implement the move() method differently, showcasing polymorphism.


# Week 7 Assignment: Data Analysis with Pandas & Visualization with Matplotlib

## 🎯 Assignment Objectives
- Load and explore a dataset using **Pandas**.  
- Perform **basic data analysis** such as summary statistics and grouping.  
- Create **visualizations with Matplotlib**, including:  
  - Line chart  
  - Bar chart    
  - Scatter plot  
- Document findings and observations.


## 📚 Tasks Completed
1. **Dataset Loading & Cleaning**  
   - Loaded a CSV dataset.  
   - Checked data structure, data types, and missing values.  
   - Cleaned dataset by handling missing data.  

2. **Basic Analysis**  
   - Calculated mean, median, standard deviation, and other descriptive statistics.  
   - Grouped data by a categorical column and calculated averages.  
   - Identified simple patterns and insights.  

3. **Visualizations**  
   - **Line Chart** to show trends over time.  
   - **Bar Chart** comparing averages across categories.  
   - **Scatter Plot** showing relationship between two numerical variables.  

4. **Findings**  
   - Group averages showed clear category differences.    
   - Scatter plots made visible relationships between features.  


## ✅ Outcome
This assignment demonstrated how **Pandas** can be used for data cleaning and analysis, and how **Matplotlib** helps bring out insights visually.  
The combination of the two provides both **statistical understanding** and **visual interpretation** of data.  

