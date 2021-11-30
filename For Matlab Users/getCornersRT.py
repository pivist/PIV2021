"""
This script receives an image as input and outputs a .mat file with the Aruco markers' coordinates (in pixels),
ids, rotations to camera frame as 1x3 vectors with rotation angles in radians, and translations in meters.
The order of the coordinates, rotation vectors and translations is the same as the order of the ids.
Example: if ids[0] has value 2 then corners[0] has corners of Aruco marker with id=2, and the first line of
rvecs and tvecs are the rotation and translation of this marker.
"""

import sys
import numpy as np
import cv2
from cv2 import aruco as aruco
from scipy.io import savemat
import argparse

def initArucoPos(template, aruco_dict, arucoParameters):
    """
    Returns the corners of the Aruco markers in the template image. Note that the corners sequence is the same as
    the ids sequence. Example: if ids[0] has value 2 then corners[0] has corners of Aruco marker with id=2.

    :param template: template image
    :param aruco_dict: dictionary of Aruco codes used in the template image
    """
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray_template, aruco_dict, parameters=arucoParameters)

    if len(corners) == 0:
        print("Could not detect Aruco markers. Exiting.")
        exit(0)

    print("Detected {} Aruco markers.".format(np.size(corners,0)))

    return corners, ids

def argParsing():
    " Parses command line arguments."

    parser = argparse.ArgumentParser(description='Receives an image with some Aruco markers and outputs their \
                                                  coordinates, ids, rotations (vectors with 3 rotation angles \
                                                  in radians) and translations.')
    parser.add_argument('img', metavar='image_path',
                        help='Path to image, with extension (.png, .jpg, ...)')
    parser.add_argument('len', metavar='markerLength', type=float,
                        help='Length of each Aruco marker, in meters.')
    parser.add_argument('fx', type=float,
                        help='The x-axis focal length of the camera in pixels.')
    parser.add_argument('fy', type=float,
                        help='The y-axis focal length of the camera in pixels.')
    parser.add_argument('cx', type=float,
                        help='The x-axis optical center of the camera in pixels.')
    parser.add_argument('cy', type=float,
                        help='The y-axis optical center of the camera in pixels.')

    return parser.parse_args()

if __name__ == "__main__":
    args = argParsing()

    img_template = cv2.imread(args.img)
    if img_template is None:
        print("Unable to read the template.")
        exit(-1)

    #The arucos in the template must be the ones in this dictionary
    dict4_7by7 = aruco.getPredefinedDictionary(aruco.DICT_7X7_50)

    arucoParameters = aruco.DetectorParameters_create()
    corners, ids = initArucoPos(img_template, dict4_7by7, arucoParameters)

    #Intrinsic parameters matrix
    camera_matrix = np.array([[args.fx, 0, args.cx],
                              [0, args.fy, args.cy],
                              [0, 0, 1]])
    #Matrix of distortion coefficients
    dist_matrix = np.array([0, 0, 0, 0])
    rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, args.len, camera_matrix, dist_matrix)

    dict = {"corners": corners, "ids": ids, "RotVecs": rvecs, "TVecs": tvecs}
    savemat("cornersIdsRT.mat", dict)
