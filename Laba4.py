def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if line.strip() == '':
                count += 1
        return count

def count_lines_with_z(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if 'z' in line:
                count += 1
        return count

def count_z_occurrences(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content.count('z')

def count_lines_with_and(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if 'and' in line:
                count += 1
        return count

def print_statistics(file_path):
    print("File:", file_path)
    print(" total lines:", count_lines(file_path))
    print(" empty lines:", count_empty_lines(file_path))
    print(' lines with "z":', count_lines_with_z(file_path))
    print(' "z" count:', count_z_occurrences(file_path))
    print(' lines with "and":', count_lines_with_and(file_path))

if __name__ == "__main__":
    while True:
        file_path = input("Enter the path to the file (or 'q' to quit): ")
        if file_path.lower() == 'q':
            break
        print_statistics(file_path)