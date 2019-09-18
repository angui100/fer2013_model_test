# Facial ML trained model test program
This is a piece of reality test program for testing the trained ML data model.

## Set environment

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
