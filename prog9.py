def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            characters = len(content)

            print(f"Number of lines: {len(lines)}")
            print(f"Number of words: {len(words)}")
            print(f"Number of characters: {characters}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
filename = input("Enter the name of the text file: ")
count_file_stats(filename)
