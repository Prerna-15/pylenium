# pylenium
Sample codes of Pylenium

The installations for pylenium include:
1. Install python 3.x

2. Use any editor. The recommended editor is PYCHARM as it is python supported and most importantly it has pytest support which is a test framework used specifically in pylenium.
  1) Use Virtualenv while creating project.
  2) Check if python 3 is installed in terminal.
  3) check if pipenv is installed if not then use the command:
        pip install pipenv
  4) Specifically use pipenv to install all packages properly.
        pipenv install pyleniumio. 
  5) Check if following things are locked after installing pylenium in the project structure:
        conftest.py
        pipfile
        pipfile.lock
        pylenium.json
  6) Check the settings:
        project > settings > tools > python integrated tools > default test runner > pytest
        
3. Chromedriver should be installed in the path if you are using pyleniumio version greater than 1.4.1. In case of any issue,    we can follow the documentation following:
   https://elsnoman.gitbook.io/pylenium/misc/install-chromedriver
   
4. Cheers! All set up done.. Start Coding..
