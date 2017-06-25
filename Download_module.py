import subprocess
import os
from pathlib import Path

ydl_opts = {
    'format': 'bestaudio/best',
    'verbose': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality': '192',
    }],
}


def download_audio(MUSIC_PATH, artist):
    #create folder for artist
    artist_path = create_dir(MUSIC_PATH, artist.name)

    albums = artist.albums
    for album_number, album_name in enumerate(albums):
        #create folder for album
        album_path = create_dir(artist_path, album_name)
        #creates a list with the name of the songs in the respective album
        songs_names = artist.songs[album_number]
        songs_file_path = create_songs_file(album_path, songs_names)
        #searches the youtube links of the respective songs
        songs_links = collect_songs_link(artist.name, songs_file_path, album_path)
        #downloads audio using youtube links
        download_youtube(songs_links, songs_names, album_path)


def create_dir(base_path, extension):
    path = base_path + '\\' + extension
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_songs_file(path, songs):
    file_path = path + '\\' + 'allSongs.txt'
    with open(file_path, 'w') as f:
        for song in songs:
            f.write(song + '\n')
    return file_path


def collect_songs_link(name, songs_file_path, album_path):
    link_path = album_path + '\\' + 'links.txt'
    #print link_path
    #print songs_file_path
    subprocess.call(['ruby', 'ScrapeLinks.rb', name, songs_file_path, link_path])
    return link_path


def clean_link(link):
    link = link[7:]
    link = link.replace('%3F', '?')
    link = link.replace('%3D', '=')
    n = link.find('&sa')
    return link[:n]


def choose_links(path):
    links = []
    with open(path, 'r') as f:
        links_list = f.readlines()
    count, music_counter = 0, 0
    for item in links_list:
        if item[0:5] == 'https':
            count +=1
        else:
            if music_counter < count:
                links.append(clean_link(item))
                music_counter += 1
    return links


def download_youtube(links_path, songs_names, download_path):
    links = choose_links(links_path)
    print "links: \n"
    print links
    for n, link in enumerate(links):
        path = download_path + '\\' + songs_names[n] + '.mp3'
        my_file = Path(path)
        if my_file.is_file():
            print "file already exists, skipped download" + path
            continue
        else:
            print link
            subprocess.call(['youtube-dl','-o', path ,"--extract-audio","--audio-format","mp3", link])
