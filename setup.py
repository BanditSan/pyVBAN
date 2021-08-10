from setuptools import setup

setup(
    name='pyvban',
    version='1.0.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pyaudio',
    ],
)
