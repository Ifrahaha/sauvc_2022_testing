# Task 1 Code by Zahid and Ifrah

## Inside the perception folder, navigate into the 'tasks' -> 'gate' and run the file named 'Task 1.py'

### Follow the instruction as below:


## Installation
```
conda create -n AUV python=3.8
```

* 1) activate it with
```
conda activate AUV
```

* 2) and install all dependencies with
```
pip3 install -r requirements.txt
```

* 3) and install it
```
pip3 install -e perception/
```

```
cd perception
```
```
python setup.py build_ext --inplace
```
```
cythonize file_to_cythonize.pyx
```


### Alternative Method to make an environment

```
sudo apt-get install python3-venv
cd~
python3 -m venv auv
cd ~/auv
source bin/activate
```