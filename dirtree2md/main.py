import os

def generate_markdown_tree(directory):
    """
    Generate a markdown representation of the directory tree.
    
    Parameters:
    directory (str): The root directory to generate the tree from.
    
    Returns:
    str: A string representing the directory tree in markdown format.
    """
    tree_lines = []
    for root, dirs, files in os.walk(directory):
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
    args = parser.parse_args()
    
    markdown_tree = generate_markdown_tree(args.directory)

    if args.file:
        make_markdown_file(markdown_tree, args.file)
    else:
        print(markdown_tree)

if __name__ == "__main__":
    main()
