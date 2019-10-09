# drop_you_like_a_block
A script for basic play of the game "BlockDrop". The strategy for this script is to watch only blocks in the bottom-row to avoid committing errors on falling (moving) blocks.

The game can be found at: https://arcade-7e162.web.app/blockdrop


## Requirements/Installation
The script is designed for Windows and is written in Python. Python 3.7+ (https://www.python.org/downloads/), Selenium (https://pypi.org/project/selenium/), and ChromeDriver (https://chromedriver.chromium.org/downloads) for the version of Chrome used (chrome://settings/help) is required.

To install, clone this repository to a desired location and either add the chromedriver executable to the directory (recommended) or add the executable to PATH.


## Using the Script
To run the script, navigate to the script directory in a Windows CLI and run __drop_you_like_a_block.py__. For example, the command may appear as the following:

> py drop_you_like_a_block.py


## Results
This script scores between 111-114 on average. A higher score may be achieved with parallel processing or a better algorithm.
Peformance is bottle-necked by a single cursor, single process/thread, and a random (any block in the bottom-row) approach to play.





