import os

def generate_structure(root_dir):
    structure = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        structure.append(f"{indent}{os.path.basename(dirpath)}/")
        
        subindent = '│   ' * level + '├── '
        for i, filename in enumerate(filenames):
            if i == len(filenames) - 1:
                subindent = '│   ' * level + '└── '
            structure.append(f"{subindent}{filename}")
        
        if not filenames:
            structure[-1] = structure[-1].replace('├── ', '└── ')
    
    return structure

def save_structure_to_file(structure, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in structure:
            f.write(line + '\n')
    print(f"Structure saved to {filename}")

if __name__ == "__main__":
    root_directory = input("Enter the root directory to generate structure from: ")
    if not os.path.exists(root_directory):
        print(f"Root directory '{root_directory}' does not exist.")
    else:
        structure = generate_structure(root_directory)
        save_filename = input("Enter the filename to save the directory structure: ")
        save_structure_to_file(structure, save_filename)
