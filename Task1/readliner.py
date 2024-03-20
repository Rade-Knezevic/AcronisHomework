import os

def count_lines_in_directory(directory):
    lines_count = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    lines_count[os.path.join(root, file)] = len(lines)
            except Exception as e:
                print(f"Error reading file {file}: {e}")
    return lines_count

# Example usage:
# Replace '/path/to/directory' with the actual directory path you want to inspect.
# directory_path = '/path/to/directory'
# result = count_lines_in_directory(directory_path)
# print(result)
