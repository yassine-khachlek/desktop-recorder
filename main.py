#!/usr/bin/python 
# -*- coding: utf-8 -*- 

## Here we imported both Gtk library and the os module and time
from gi.repository import Gtk 
import os 
import time


      
class Handler: 

  def buttonRecordClicked(self, button): 
    
    # SET THE FILENAME
    filename = time.strftime("%Y%m%dT%H%M%S") + ".avi" #ISO 8601 format
    
    ## SET THE FILEPATH
    filepathandname = os.environ["HOME"] + "/" + filename

    # SHOW THE RECORDING MESSAGE
    labelStatus.set_text("Recording " + filepathandname)
    
    ## Here exported the 'filepathandname' variable from Python to the 'filename' variable in the shell.
    os.environ["filename"] = filepathandname 
    
    ## Using 'os.system(COMMAND)' to execute any shell command or shell script, here we executed the 'avconv' command to record the desktop video & audio.
    os.system("avconv -f x11grab -r 25 -s `xdpyinfo | grep 'dimensions:'|awk '{print $2}'` -i :0.0 -vcodec libx264 -threads 4 $filename -y & ")

    # HIDE THE RECORD BUTTON & SHOW THE STOP BUTTON
    buttonRecord.hide();
    buttonStop.show();

  def buttonStopClicked(self, button): 
    ## Run the 'killall avconv' command when the stop button is clicked. 
    os.system("killall avconv")
    # HIDE THE STOP BUTTON & SHOW THE RECORD BUTTON
    buttonStop.hide();
    buttonRecord.show();
    labelStatus.set_text("Ready")
  
## Nothing new here.. We just imported the 'ui.glade' file. 
builder = Gtk.Builder() 
builder.add_from_file("ui.glade") 
builder.connect_signals(Handler())

# GET NEEDED UI ELEMENTS
window = builder.get_object("window1")
buttonRecord = builder.get_object("buttonRecord")
buttonStop = builder.get_object("buttonStop")
labelStatus = builder.get_object("labelStatus") 

# SHOW THE FIRST STATUS MESSAGE
labelStatus.set_text("Ready")

## Give that developer a cookie ! 
window.connect("delete-event", Gtk.main_quit) 
window.show_all() 
buttonRecord.hide();
buttonStop.hide();
buttonRecord.show();
Gtk.main()
