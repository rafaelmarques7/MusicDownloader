from Webcrawler_module import Webcrawler

class Artist( object ):
    
    def __init__( self, name, MUSIC_PATH ):
        self.name = name
        self.albums = []
        self.info = []
        self.lyrics = []
        self.songs = []
        self.music_path = MUSIC_PATH

    def artist_get( self ):
        crawler = Webcrawler( self.name)
        [albums, songs, lyrics] = crawler.load_artist_music()
        self.albums = albums
        self.songs = songs
        self.lyrics = lyrics
        self.write_text()

    def write_text(self):
        lyrics_path = self.music_path + '\\' + self.name + '\\lyrics'
        print "lyrics type"
        print self.lyrics
    
    def __repr__( self ):
        return( "<Artist --- name: {0}, albums: {1}, info: {2}, songs: {3}, lyrics{4}".format(
            self.name, self.albums, self.info, self.songs, self.lyrics))

    def __str__( self ):
        return( "<Artist --- name: {0}, albums: {1}, info: {2}, songs: {3}, lyrics{4}".format(
            self.name, self.albums, self.info, self.songs, self.lyrics))
