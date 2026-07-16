from setuptools import setup, find_packages

setup(
    name='speech-recognition-project',
    version='0.1.0',
    author='Vu Hung',
    author_email='vuhung16plus+python@gmail.com',  # TODO: replace with project email
    description='A project for recognizing speech from audio files using pocketsphinx.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pocketsphinx',
        # Add other dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'pocketsphinx.py = pocketsphinx_app:main',  # Assuming main is the entry function in pocketsphinx_app.py
        ],
    },
)