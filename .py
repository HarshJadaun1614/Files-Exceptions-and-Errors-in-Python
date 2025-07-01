#Task 1: Read a File and Handle ErrorsAdd commentMore actions

try:
    # Attempt to open the file
    with open("sample.txt", "r") as file:
        # Read and print each line
        print("Contents of 'sample.txt':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")


#Task 2: Write and Append Data to a File

user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
additional_input = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display the final content
print("\nFinal contents of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
