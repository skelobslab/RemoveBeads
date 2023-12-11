# RemoveBeads
Installing Software
Install GIMP here:  https://www.gimp.org/

Install the Resynthesizer plug-in for gimp. The main Github repo is here: https://github.com/bootchk/resynthesizer. For Windows, download the archived zip folder containing required scripts: https://github.com/pixlsus/registry.gimp.org_static/blob/master/registry.gimp.org/files/Resynthesizer_v1.0-i686.zip.  

After installing GIMP, locate the plug-in folder. Go to Preference -> Folders -> Plug-ins to see where the GIMP folder is located.

Extract all files from Resynthesizer into the plug ins folder. 

Check to see if Resynthesizer appears in GIMP. Navigate to Filters -> Enhance. If you see "Heal Selection", you successfully added Resynthesizer to GIMP.

 If the option is not appearing, you may need to specifically add the "resynthesizer" folder in Preference -> Folders->Plug-ins

Removing Beads
In XMALab, export the undistorted (unfiltered) 2D trial images (see XMALab Processing). 

Download the erase_beads.py python script from the Repo. Edit the filepaths for the trial you are removing images for, then copy the python script into the plug-ins folder. Note that you may not have permission to edit the script directly in the plug-ins folder, so edit the file prior to copying it into the folder.

You will need to provide the trial's BVR folder path, as well as the names of the camera subfolders. The script will create new folders for the exported images, with "_nobeads" appended to the camera subfolder name (ie.. "C001UND_nobeads"). If you want to name the exported folder something else, this can be edited in the script.

Restart GIMP.

Check if you added erase_beads.py properly by going to Filters->Enhance. You should see "Erase beads" if it worked. 

To start bead removal, navigate to "Erase beads" and select it. Select OK on the pop-up window, and the script should begin. It will take several minutes.

