from setuptools import setup

setup(
    name='pyvban',
    version='1.0.0',
    url='https://github.com/BanditSan/pyVBAN',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pyaudio',
    ],
    packages=['pyVBAN.py'],
)
