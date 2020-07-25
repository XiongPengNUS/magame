import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='magame',
     version='0.0.0',
     author="Peng Xiong",
     author_email="xiongpengnus@gmail.com",
     description="Write your own function to solve the maze!",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/XiongPengNUS/magame",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
