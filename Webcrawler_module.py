import Parser_module as Parser
import urllib2
import os

class Webcrawler( object ):

    def __init__( self, artist ):
        self.artist = artist.replace(" ", "").lower()
        self.url = "http://www.azlyrics.com/" + self.artist[0] + "/" + self.artist + ".html"

    def __repr__( self ):
        return( "<Webcrawler --- url: {0}, artist: {1}".format(
            self.url, self.artist))

    def __str__( self ):
        return( "<Webcrawler --- url: {0}, artist: {1}".format(
            self.url, self.artist))

    def load_artist_music( self ):
        response = urllib2.urlopen(self.url)
        html = response.read()
        """
        dir_curr = os.getcwd()
        with open(dir_curr + '/artist.txt', 'w') as f:
            f.write(html)
        """
        [albums, songs, lyrics_links] = Parser.get_data( html)
        lyrics = self.lyrics_crawler(lyrics_links)
        return [albums, songs, lyrics]

    def lyrics_crawler(self, links):
        urls=['http://www.azlyrics.com/' + item + '.html' for sublist in links for item in sublist ]
        lyrics = []
        for url in urls:
            response = urllib2.urlopen(url)
            html = response.read()
            lyrics.append(Parser.get_lyrics(html))
        return lyrics
