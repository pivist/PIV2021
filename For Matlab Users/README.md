These files are for those of you using Matlab, since using OpenCV with Matlab is not trivial. Even if you are using Matlab, you still need to have Python installed in your machine, as well as the required packages.

## Installing Python
If you aren't sure on how to install Python, you can follow [this tutorial](https://www.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html).
Make sure that you installed the Python version you install is supported by your Matlab version (more information on this in the previous link). The scripts in this folder were developed in Python 3.7 so you should install Python 3.7 or similar.

### Required packages
You also need to install some Python packages: Numpy, OpenCV and OpenCV contrib module. We reccomend using [pip](https://pip.pypa.io/en/stable/installation/) as such:

`pip install numpy opencv-python opencv-contrib-python`

## Running Python scripts inside Matlab
Once everything is configured, you should be able to run Python scripts in Matlab using something like

`output = py.getCorners.run('img_name.png')`

See [this link](https://www.mathworks.com/help/matlab/matlab_external/call-user-defined-custom-module.html) for more information.

## Troubleshooting
If you have issues with this setup visit [this link](https://github.com/altermarkive/Calling-Python-from-Matlab). If you still can't solve your issues, open an issue on this github and describe the problem.
