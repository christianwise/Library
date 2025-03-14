import os

def find_libraries_txt_files(root_dir):
    """Recursively find all libraries.txt files in the directory."""
    libraries_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'libraries.txt':
                libraries_files.append(os.path.join(dirpath, filename))
    return libraries_files

def collect_library_names(files):
    """Collect all unique library names into a single list."""
    all_libraries = set()

    for file in files:
        with open(file, 'r') as f:
            for line in f:
                library = line.strip()
                all_libraries.add(library)
    
    return list(all_libraries)

def write_unique_libraries(all_libraries, files):
    """Update each file to only contain libraries from the all-in-one list."""
    all_libraries_set = set(all_libraries)  # Convert to set for faster lookup

    for file in files:
        print(f"Processing file: {file}")  # Log the file path being processed
        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for line in lines:
                library = line.strip()
                if library in all_libraries_set:
                    f.write(library + '\n')
                    all_libraries_set.remove(library)  # Remove to ensure it's only written once

def main():
    root_dir = 'python_libraries'  # Adjust this path as needed
    libraries_files = find_libraries_txt_files(root_dir)
    all_libraries = collect_library_names(libraries_files)
    write_unique_libraries(all_libraries, libraries_files)

if __name__ == "__main__":
    main()
