import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='selenium-cmd',
    version='0.0.2',
    license='MIT',
    description='Tool to control Selenium from command line',
    long_description_content_type='text/markdown',
    long_description=README,
    python_requires='>=3',
    project_urls={
        "Source": "https://github.com/patkle/selenium-cmd",
    },
    keywords='selenium xpath testing',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    author='Patrick Klein',
    packages=['selenium_cmd'],
    install_requires=[
        'importlib-metadata ~= 1.0 ; python_version < "3.8"',
        'selenium',
        'parsel'
    ]
)
