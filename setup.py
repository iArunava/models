import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='AI Models',
        version='0.01',
        author='Arunava Chakraborty (@iArunava)',
        author_email='iarunavaofficial@gmail.com',,
        description='contains implementations of all AI models',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/iArunava/models',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: MIT License',
            'Operating System :: OS Independent',
        ],
    )
