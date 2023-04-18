
from setuptools import setup
  
setup(
    name='rockstarapi',
    version='0.1',
    description='A Python for making Rockstar Api available in FoxDot',
    author='UTC OLP Algorave Club',
    author_email='meggleton@utcsheffield.org.uk',
    packages=['rockstarapi'],
    install_requires=[
        'FoxDot',
        'requests',
    ],
)