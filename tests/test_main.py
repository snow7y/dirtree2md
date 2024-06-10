import unittest
import os
from dirtree2md.main import generate_markdown_tree

class TestGenerateMarkdownTree(unittest.TestCase):
    def setUp(self):
        # Setup a test directory structure
        os.makedirs('test_dir/sub_dir', exist_ok=True)
        with open('test_dir/file1.txt', 'w') as f:
            f.write('Test file 1')
        with open('test_dir/sub_dir/file2.txt', 'w') as f:
            f.write('Test file 2')

    def tearDown(self):
        # Remove the test directory structure
        import shutil
        shutil.rmtree('test_dir')

    def test_generate_markdown_tree(self):
        expected_output = "- test_dir/\n    - file1.txt\n    - sub_dir/\n        - file2.txt"
        actual_output = generate_markdown_tree('test_dir')
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
