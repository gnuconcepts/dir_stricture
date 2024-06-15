import os

def parse_structure_file(structure_file):
    with open(structure_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    structure = []
    current_path = []

    for line in lines:
        line = line.rstrip('\n')
        if line.strip() == "":
            continue

        level = (len(line) - len(line.lstrip('├──│   '))) // 4
        entry = line.strip().replace('├── ', '').replace('└── ', '').replace('│   ', '')
        
        while len(current_path) > level:
            current_path.pop()
        
        current_path.append(entry)
        structure.append(os.path.join(*current_path))
    
    return structure

def create_structure(structure, base_path):
    for path in structure:
        full_path = os.path.join(base_path, path)
        if '.' in os.path.basename(full_path):
            # It's a file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                pass
        else:
            # It's a directory
            os.makedirs(full_path, exist_ok=True)
    print("Directory structure created successfully.")

if __name__ == "__main__":
    structure_file = input("Enter the filename containing the directory structure: ")
    if not os.path.isfile(structure_file):
        print(f"File '{structure_file}' does not exist.")
    else:
        root_directory = input("Enter the root directory where the structure should be created: ")
        if not os.path.exists(root_directory):
            print(f"Root directory '{root_directory}' does not exist.")
        else:
            structure = parse_structure_file(structure_file)
            create_structure(structure, root_directory)
