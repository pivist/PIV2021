These files are for those of you using Matlab, since using OpenCV with Matlab is not trivial. Even if you are using Matlab, you still need to have Python installed in your machine, as well as the required packages.

### Important
For **Task 1** of the project you'll only need `getCorners.py`

## Installing Python
If you aren't sure on how to install Python, you can follow [this tutorial](https://www.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html).
Make sure that the Python version you install is supported by your Matlab version (more information on this in the previous link, but if you're using Matlab2019a you should install Python3.7.9 64-bit). The scripts in this folder were developed in Python 3.7 so you should install Python 3.7 or similar.

### Required packages
You also need to install some Python packages: Numpy, Scipy, OpenCV and OpenCV contrib module. We reccomend using [pip](https://pip.pypa.io/en/stable/installation/), just type in a terminal (after installing Python):

`pip install numpy scipy opencv-python opencv-contrib-python`

## Veryfing your Python installation
1. Open a terminal and type `python --version`. You should see an output similar to `Python 3.7.9`.
2. Open Matlab and enter the command `pyversion`. You should see something similar to
```
       version: '3.7'
    executable: 'C:\some_path\Python\Python37\python.exe'
       library: 'C:\some_path\Python\Python37\python37.dll'
          home: 'C:\some_path\Python\Python37'
      isloaded: 1
```
3. You're good to go!

Having issues? See the Issues section, we'll be creating some issues with the most common problems and possible solutions.

## Running Python scripts inside Matlab
Once everything is configured, you should use the Matlab code bellow to run getCorners.py and load the data into your Matlab workspace

```
py.getCorners.run("C:\Users\Asus\Desktop\ist\piv_related\img1.png");

aux = load('cornersIds.mat');
aux_corners = squeeze(aux.corners);
corners = permute(aux_corners, [1,3,2]);
ids = aux.ids;

clear aux aux_corners

fprintf("\nNote: The first detected Aruco marker is corners(1,:,:), the second is (2,:,:), and so on\n")
```

See [this link](https://www.mathworks.com/help/matlab/matlab_external/call-user-defined-custom-module.html) for more information.
