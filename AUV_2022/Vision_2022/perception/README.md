# CODE BY ZAHID AND IFRAH for task 1 

### Gate detection without red flare avoidance


## Perception Code Overview

conda create -n urobotics python=3.7

conda activate urobotics

pip3 install -r requirements.txt

pip3 install -e perception/


cd perception 

python setup.py build_ext --inplace

cythonize file_to_cythonize.pyx



