# RDML-Python

This is a wraper for the rdmlpython python library to handle RDML files.

Prepare your computer
---------------------

`pip install twine`

`pip install wheel`


Clone the repository
--------------------

`git clone --recursive https://github.com/RDML-consortium/rdmlpython.git rdmlpython`

`python setup.py bdist_wheel --universal`

`twine upload dist/*`

Update the repository
---------------------

`git submodule update --recursive --remote`

`rm -rf rdmlpython.egg-info dist build`

`python setup.py bdist_wheel --universal`

`twine upload dist/*`

