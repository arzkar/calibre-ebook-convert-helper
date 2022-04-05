from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='ebook-convert-helper',
    author='Arbaaz Laskar',
    author_email="arzkar.dev@gmail.com",
    description="A helper cli for calibre's ebook-convert CLI which is used to convert all files in an directory into another format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.3.2",
    license='Apache License',
    url="https://github.com/arzkar/calibre-ebook-convert-helper",
    packages=find_packages(
        include=['ebook_convert_helper', 'ebook_convert_helper.*']),
    include_package_data=True,
    install_requires=[
        'tqdm>=4.62.3',
        'colorama>=0.4.4'
    ],
    entry_points='''
        [console_scripts]
        ebook-convert-helper=ebook_convert_helper.cli:main
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
