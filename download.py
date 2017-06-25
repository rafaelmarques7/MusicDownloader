#!/usr/bin/env python

#_______________________________________________________________________________
#THE WORKFLOW OF THIS PROGRAM IS ORGANIZED AS FOLLOWS
#   1) COLLECT ARTIST INFO - ORGANIZE INTO ALBUMS
#   2) COLLECT YOUTUBE LINKS - FOR EACH MUSIC, FOR EACH ALBUM
#   3) DOWNLOAD AUDIO - FOR EACH MUSIC, SAVE IN ALBUM FOLDER
#_______________________________________________________________________________
#imports
import sys
import os
from Artist_module import Artist
import Download_module

#_______________________________________________________________________________
MUSIC_PATH = 'D:\\music'
#_______________________________________________________________________________
#MAIN
if __name__ == "__main__":  
    artist_name = sys.argv[1]

    #collects all information about an artist
    print "collecting info about " + artist_name
    artist = Artist(artist_name, MUSIC_PATH)
    artist.artist_get()
    #print artist

    #downloads music
    Download_module.download_audio(MUSIC_PATH, artist)

