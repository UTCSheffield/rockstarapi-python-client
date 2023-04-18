
from setuptools import find_packages, setup
  
setup(
    name='rockstarapi',
    version='0.1',
    description='A Python for making Rockstar Api available in FoxDot',
    author='UTC OLP Algorave Club',
    author_email='meggleton@utcsheffield.org.uk',
    packages=find_packages(include=['rockstarapi']),
    install_requires=[
        'FoxDot',
        'requests',
    ],
    setup_requires=["pytest-runner"],
    test_requires=["pytest==7.3.1"],
    test_suites="tests"
)