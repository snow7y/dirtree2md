import os
import logging
# logging.basicConfig(level=logging.DEBUG)
import fnmatch

def read_gitignore(gitignore_path):
    """
    Read .gitignore file and return a list of patterns.
    
    Parameters:
    gitignore_path (str): The path to the .gitignore file.
    
    Returns:
    list: A list of patterns to exclude.
    """
    with open(gitignore_path, 'r') as f:
        patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return patterns


def should_exclude(path, patterns, root_dir):
    """
    Check if the given path should be excluded based on the patterns.
    
    Parameters:
    path (str): The path to check.
    patterns (list): The list of patterns to match against.
    
    Returns:
    bool: True if the path should be excluded, False otherwise.
    """
    rel_path = os.path.join(path, root_dir).replace(os.sep, '/')
    for pattern in patterns:
        normalized_pattern = pattern.replace(os.sep, '/')
        if (fnmatch.fnmatch(rel_path, normalized_pattern) or
            fnmatch.fnmatch(rel_path, f'./{normalized_pattern}') or
            fnmatch.fnmatch(rel_path, f'**/{normalized_pattern}') or
            fnmatch.fnmatch(rel_path, f'{normalized_pattern}/**')): 
            print(f"Excluding {rel_path} due to pattern {normalized_pattern}")
            return True
        else:
            print(f"Not excluding {rel_path} for pattern {normalized_pattern}") 
    return False

def generate_markdown_tree(directory, exclude=[], gitignore_path=None):
    """
    Generate a markdown representation of the directory tree.
    
    Parameters:
    directory (str): The root directory to generate the tree from.
    exclude (list): List of directories to exclude from the tree.
    
    Returns:
    str: A string representing the directory tree in markdown format.
    """
    tree_lines = []
    exclude_paths = [os.path.abspath(ex) for ex in exclude]
    logging.debug(f"Exclude paths: {exclude_paths}")

    gitignore_patterns = []
    if gitignore_path:
        gitignore_patterns = read_gitignore(gitignore_path)

    for root, dirs, files in os.walk(directory):
        current_path = os.path.abspath(root)
        logging.debug(f"Current root: {current_path}")
        logging.debug(f"Current root: {dirs}")
        # Skip directories that are in the exclude list
        original_dirs = dirs[:]
        dirs[:] = [
            d for d in dirs 
            if os.path.abspath(os.path.join(root, d)) not in exclude_paths 
            and not should_exclude(os.path.join(root, d), gitignore_patterns, directory)
        ]

        logging.debug(f"Original dirs: {original_dirs}")
        logging.debug(f"Filtered dirs: {dirs}")

        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * level
        tree_lines.append(f'{indent}- {os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            tree_lines.append(f'{sub_indent}- {f}')
    return '\n'.join(tree_lines)

def make_markdown_file(markdown_tree, file_path):
    with open(file_path, 'w') as f:
        f.write(markdown_tree)
    print(f'Markdown tree saved to {file_path}')


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate Markdown directory tree')
    parser.add_argument('directory', type=str, help='Directory to generate tree from')
    parser.add_argument('-f', '--file', type=str, help='Output file to save the markdown tree')
    parser.add_argument('--exclude', nargs='*', default=[], help='Directories to exclude from the tree')
    parser.add_argument('--gitignore', type=str, help='Path to the .gitignore file')
    args = parser.parse_args()
    
    exclude_paths = [os.path.abspath(os.path.join(args.directory, ex)) for ex in args.exclude]
    markdown_tree = generate_markdown_tree(args.directory, exclude=exclude_paths, gitignore_path=args.gitignore)

    if args.file:
        make_markdown_file(markdown_tree, args.file)
    else:
        print(markdown_tree)

if __name__ == "__main__":
    main()
