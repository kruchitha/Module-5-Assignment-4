"""ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
try:
    with open('sample.txt', 'r') as f:
        print("Reading file content: ")
        for line_num, line_content in enumerate(f, start=1):
            print(f"Line {line_num}: {line_content.strip()}")
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found.")