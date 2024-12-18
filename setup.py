from setuptools import setup, find_packages

setup(
    name='happy_dataset_summarizer',
    version='0.1.0',
    author='azario0',
    author_email='azariomalek@gmail.com',
    description='A tool for generating comprehensive dataset reports to use with LLM',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/happy_dataset_summarizer',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'happy-dataset-summarizer=happy_dataset_summarizer.happy_dataset_summarizer:main',
        ],
    },
)