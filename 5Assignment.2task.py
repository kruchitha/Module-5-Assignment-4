"""Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""
user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(user_input)
    print("data successfully written to output.txt.")
additional_data = '\n' + input("Enter additional text to append: ")
with open("output.txt", "a") as g:
    g.write(additional_data)
    print("data successfully appended.")
with open("output.txt", "r") as k:
    for line in k:
        print(line.strip())
