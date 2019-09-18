# Facial ML trained model test program
This is a piece of reality test program for testing the trained ML data model.

## Set environment for MacOS

### clone this github repo
- git clone https://github.com/angui100/fer2013_model_test.git

### install python3.7
- Take reference from URL: https://realpython.com/installing-python/

### install pip
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py

### set up python virtual environment
- python3 -m venv the-name-of-your-python-virtual-environment
- source the-name-of-your-python-virtual-environment/bin/activate
- For example as below<br>
- python3 -m venv emovm<br>
- source emovm/bin/activate

### install the opencv (opencv-contrib-python-4.1.1.26)
sudo pip install opencv-contrib-python

### install all required packaged (denpendences)
cd FER2013_Model_Test
- pip install -r requirements.txt

### Running tests

You can run the tests with:

```
python3 do_test.py

```

### Quit this process
press Ctrl + c

## Set environment for Windows
### Windows environment need Admin previlige to install Python3 packages
### Link abot to get ADMIN Access
https://www.itechtics.com/enable-administrator-account-windows-10/<br/>

https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/<br/>

https://www.itechtics.com/enable-administrator-account-windows-10/<br/>

https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/<br/>

### install python3.7
- Take reference from URL: https://realpython.com/installing-python/
### install PIP for windows
https://www.makeuseof.com/tag/install-pip-for-python/<br/>

### Run following command to install following tools
- pip install virtualenv
- pip install virtualenvwrapper-win

### Make a directory for this project then cd into the project directory to clone the github repo
- git clone https://github.com/angui100/fer2013_model_test.git

### Create Python virtual running environment under your project directory as below
mkvirtualenv HelloPeter

### Go into the cloned repo directory
cd fer2013_model_test

### Run PIP to install all dependence packages
pip install -r requirements.txt
pip install opencv-contrib-python  

### run the test program
python do_test.py

