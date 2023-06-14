Project-Cameron-Luke-Julian

**To play the game:**

Make sure Python is installed on your computer.
You can install the latest version of Python here:
https://www.python.org/downloads/

Make sure you have pygame installed.

**Steps:**

For windows:

1. open terminal

2. type 'pip install pygame'

3. open new terminal and type 'import pygame' to make sure it is working

For mac:

1. Install the Apple Xcode command line tools.
From a Terminal window, run the following command:
xcode-select --install

2. Install XQuartz from http://xquartz.macosforge.org/landing/.

3. Install Homebrew.
From a Terminal window, run the following command:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

4. Install Python 3.
From a Terminal window, run the following command:
brew install python3 hg sdl sdl_image sdl_mixer sdl_ttf portmidi

5. Install PyGame.
From a Terminal window, run the following command:
pip3 install hg+http://bitbucket.org/pygame/pygame

To play the game, simply open the main.py folder and enjoy!

**How the game works:**

Click the cookie and buy upgrades to yield more cookies per tick and click. Once you have reached enough 
cookies for an upgrade, the box color will turn green.

**To win the game:**

Accumulate enough cookies to buy "THE FINAL COOKIE!!!" and win the game.
You are free to play on once the game is over.

**To exit the game:**

Close the window using the x in the top right corner.

**Each File:**

 - Shop.py creates shop item objects and methods to call for each function.

 - Music.py holds game audio. It has functions that play certain audio files.

 - Counter.py keeps track of variables relating to cookie count, item cost, item limit, amount of each item. We call a
counter object in in this file that is referenced by both main.py and Shop.py.
