#!/usr/bin/env python
#script erases beads from tiff images
#needs a csv file from xmalab that has bead locations
#need to download resynthesizer
#make sure to locate the plug-in folder from gimp, and save this script there

from gimpfu import *
import csv
import os
import math

#function that erases beads
def erase_beads(image, drawable):
    #x and y parameters for select rectangle indicate location of the top left corner of the rectangle
    table = []
    operation = 0
    width = 17.0 
    height = 17.0
    corner_radius_x = 5
    corner_radius_y = 5
    samplingRadiusParam = 50
    directionParam = 0
    orderParam = 0
    compression = 0
    
    #specify filepaths - the 'r' in front of the string indicates the backlash should be intrepreted as raw character
    # XMA undistorted bead location file
    beadloc = r".csv"
    # main BVR folder with camera subfolders
    folderBVR = r"" 
    # name of cam1 subfolder
    folderCam1 = r"C001UND" 
    # name of cam2 subfolder
    folderCam2 = r"C002UND" 
    # extension for new folders with bead removed-images
    outext = r"_nobeads" 
    
    #make output folders
    folderCam1out = os.path.join(folderBVR,folderCam1+outext)
    folderCam2out = os.path.join(folderBVR,folderCam2+outext)

    if not os.path.exists(folderCam1out):
        os.mkdir(folderCam1out)

    if not os.path.exists(folderCam2out):
        os.mkdir(folderCam2out)

    #open csv file with bead locations 
    with open(beadloc, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader, None)
        for row in csvreader:
            table.append(row)
 
    #Remove beads in camera 1 view
    i = 0
    folder = os.listdir(os.path.join(folderBVR,folderCam1))
    while i < len(table):
        file = folder[i]
        filename = os.path.join(folderBVR,folderCam1, file)
        filenamesave = os.path.join(folderCam1out, file) #filenamesave is the location where you want to save new images
        image = pdb.gimp_file_load(filename, filename)
        drawable = pdb.gimp_image_get_active_drawable(image)
        display = pdb.gimp_display_new(image)
        pdb.gimp_displays_flush()
        
        #if math.isnan(float(table[i][0])) == False: #loop through frames
        j = 0
        beadloc = table[i]
        while j < len(beadloc): #loop through beads
            if math.isnan(float(beadloc[j+0])) == False:
                x = float(beadloc[j+0]) - width/2
                y = float(beadloc[j+1]) - height/2
                pdb.gimp_image_select_round_rectangle(image, operation, x, y, width, height, corner_radius_x, corner_radius_y)

            j += 4 
        pdb.python_fu_heal_selection(image, drawable, samplingRadiusParam, directionParam, orderParam)
    
        pdb.file_tiff_save(image, drawable, filenamesave, filenamesave, compression)
        pdb.gimp_display_delete(display)
        i += 1
        
    #Remove beads in camera 2 view
    i = 0
    folder = os.listdir(os.path.join(folderBVR,folderCam2))
    while i < len(table):
        file = folder[i]
        filename = os.path.join(folderBVR,folderCam2, file)
        filenamesave = os.path.join(folderCam2out, file) #filenamesave is the location where you want to save new images
        image = pdb.gimp_file_load(filename, filename)
        drawable = pdb.gimp_image_get_active_drawable(image)
        display = pdb.gimp_display_new(image)
        pdb.gimp_displays_flush()
        
        j = 0
        beadloc = table[i]
        while j < len(beadloc):
            if math.isnan(float(beadloc[j+2])) == False:
                x = float(beadloc[j+2]) - width/2
                y = float(beadloc[j+3]) - height/2
                pdb.gimp_image_select_round_rectangle(image, operation, x, y, width, height, corner_radius_x, corner_radius_y)
            j += 4 
        pdb.python_fu_heal_selection(image, drawable, samplingRadiusParam, directionParam, orderParam)
        
        pdb.file_tiff_save(image, drawable, filenamesave, filenamesave, compression)
        pdb.gimp_display_delete(display)
        i += 1

register(
    "python-fu-erase-beads",
    "Erases beads from TIFF images",
    "LONG DESCRIPTION",
    "Kaito Lee", "Kaito Lee", "2023",
    "Erase beads",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    erase_beads, menu="<Image>/Filters/Enhance")  # second item is menu location

main() 