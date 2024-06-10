from setuptools import setup, find_packages

setup(
    name='dirtree2md',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dirtree2md = dirtree2md.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to output directory structure in Markdown format',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/dirtree2md',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
