def read_file(file_path):
    """
    Reads and prints the content of a file line by line.
    
    Parameters:
    file_path (str): The path to the file to be read.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  # 'end' is used to avoid adding extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e.strerror}")

# Example usage
read_file('sample.txt')
