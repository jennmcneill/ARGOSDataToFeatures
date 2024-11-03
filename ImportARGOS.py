##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2024
## Author: jenn.mcneill@duke.edu
##---------------------------------------------------------------------

# import packages
import sys, os, arcpy

# set input variables (hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = 'V:/ARGOSTracking/Scratch/ARGOSTrack.shp'