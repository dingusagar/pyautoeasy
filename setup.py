from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'A simple GUI automation tool to automate your boring tasks'

# Setting up
setup(
    name="pyautoeasy",
    version=VERSION,
    author="Dingu Sagar",
    author_email="<dingusagar@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'PyAutoGUI==0.9.53',
        'pynput==1.7.3',
        'tabulate==0.8.9'
    ],
    keywords=['python', 'pyautoeasy', 'pyautogui', 'automate gui', 'automate ui', 'ui automation'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': ['pyautoeasy=pyautoeasy.cli:main'],
    }
)
