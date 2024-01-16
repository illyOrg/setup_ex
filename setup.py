from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='An example Python package',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'numpy>=1.0.0',
        'pyyaml==3.10'
        # Add other dependencies here
    ],
    tests_require=[
        'pytest>=5.0.0',
        'mock>=4.0.0',
        # Add other test dependencies here
    ],
    entry_points={
        'console_scripts': [
            'example_script = example_package.scripts.example_script:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
