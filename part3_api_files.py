# Task 3: File I/O and Exception Handling

def process_student_data():
    content = "Python is an interpreted, high-level, general-purpose programming language."
    
    # 1. Writing to a file
    try:
        with open("python_notes.txt", "w") as f:
            f.write(content)
        print("Successfully created python_notes.txt")
    except Exception as e:
        print(f"Error writing file: {e}")

    # 2. Reading from a file and handling errors
    try:
        with open("python_notes.txt", "r") as f:
            data = f.read()
            print(f"File Content: {data}")
    except FileNotFoundError:
        # Logging error to a file if reading fails
        with open("error_log.txt", "a") as err_file:
            err_file.write("File python_notes.txt not found.\n")
        print("Error: File not found. Logged to error_log.txt")

process_student_data()
