def get_data( html):
    album_div_pos_i = html.find('<!-- start of song list -->')
    end1 = html.find('<!-- end of song list -->')
    end2 = html.find('<script type="text/javascript">', album_div_pos_i)
    if end2 < end1:
        end1 = end2
    html = html[ album_div_pos_i: end1]
    [albums, songs, lyrics] = get_content( html)
    return [albums, songs, lyrics]

def get_lyrics(html):
    start = html.find('<!-- Usage of azlyrics.com content by any third-party lyrics provider')
    end = html.find('<!-- MxM banner -->')
    lyrics = get_object(html, start, end, "lyrics")
    return lyrics

                    
def get_content( html):
    albums, songs, lyrics = [], [], []

    while True:
        flag = check_next( html)
        if flag == "A":
            [html, album] = get_part(html, "album")
            albums.append( album)
        elif flag == "S":
            temp1, temp2 = [], []
            while flag != "A" and flag != None:
                [html, lyr] = get_part(html, "lyrics")
                [html, song] = get_part(html, "song")
                temp2.append( lyr)
                temp1.append( song)
                flag = check_next( html)
            songs.append( temp1)
            lyrics.append( temp2)
        else:
            return [albums, songs, lyrics]


def check_next( html):
    album_mi = 'class="album">'
    song_mi  = 'target="_blank">'
    album_pos = html.find( album_mi)
    song_pos = html.find( song_mi)

    if song_pos == -1:
        return None
    else:
        if album_pos == -1:
            return "S"
        elif song_pos > album_pos:
            return "A"
        else:
            return "S"

def get_part( html, obj):
    if obj == "album":
        marker_i = 'class="album">'
        marker_f = '</div>'
    elif obj == "song":
        marker_i = 'target="_blank">'
        marker_f = '</a>'
    elif obj == "lyrics":
        marker_i = 'href="../'
        marker_f = '.html'
    marker_pos_i = html.find( marker_i)
    marker_pos_f = html.find( marker_f)
    some_object = get_object( html, marker_pos_i + len(marker_i),
                            marker_pos_f, obj)
    return [ html[marker_pos_i + len(marker_i):], some_object]


def get_object( html, init, final, obj):
    return clean(html[init:final], obj)


def clean(string, obj):
    string = string.replace("<b>", "")
    string = string.replace("</b>", "")
    string = string.replace('"', '')
    if obj != 'lyrics':
        string = string.replace('/', '')
    string = string.replace(':', '')
    string = string.replace('?', '')
    return string
