from setuptools import setup, find_packages

requires = ['numpy','pandas']

setup(
    name="ancient_dragon",
    version="0.0.1",
    author="longxl87",
    author_email="331942615@qq.com",
    description="data mining tools",
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    packages=find_packages(),
    # install_requires=[
    #      "numpy>=1.26.4",
    #      "pandas>=2.2.2",
    # ],
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # python_requires='>=3.10',
)