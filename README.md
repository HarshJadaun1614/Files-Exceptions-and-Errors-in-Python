#Task 1: Read a File and Handle Errors Add commentMore actions

This Python program is designed to read the contents of a file named sample.txt and handle errors gracefully. Here's a breakdown of its functionality:

 Functionality Overview:

File Reading:

The program tries to open sample.txt in read mode ("r").

If successful, it reads and prints each line from the file, stripping any extra whitespace from the ends (using .strip()).

Error Handling:

FileNotFoundError: If sample.txt does not exist in the directory, the program prints an error message:

"Error: The file 'sample.txt' was not found."

Other Exceptions: If any other unexpected error occurs (like permission issues or encoding errors), the program catches it and prints a message with the error details.

 Purpose:

To ensure that the program does not crash when the file is missing or any other error occurs, making it robust and user-friendly.


#Task 2: Write and Append Data to a File


 Functionality Overview:

 Step 1: Write to the File

The program takes user input using input().

It opens output.txt in write mode ("w"), which:

Creates the file if it doesn't exist.

Overwrites the file if it already exists.

The user's input is then written to the file, followed by a newline.

 Step 2: Append to the File

The program takes additional user input.

It opens output.txt in append mode ("a"), which:

Adds new content to the end of the file without deleting existing data.

The additional input is appended with a newline.

 Step 3: Read and Display the File

The program reopens output.txt in read mode ("r").

It reads and prints each line in the file, stripping off any trailing whitespace using .strip().

 Purpose:

To demonstrate how to:

Write data to a file,

Append new data without erasing old content,

Read and display the full contents of the file.
