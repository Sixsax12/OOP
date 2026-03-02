class Media:
    def __init__(self,name,extension):
        self.__name = name
        self.__extension = extension
    def play(self):
        pass
    @property
    def name(self):
        return self.__name

class MP3(Media):
    def __init__(self,name):
        super().__init__(name,extension="MP3")
    def play(self):
        print("Playing MP3 file :",self.name)

class PodcastChennel:
    def __init__(self,host_name,chennel_name):
        self.__host_name = host_name
        self.__chennel_name = chennel_name
        self.__episode_list = []

    def add_episode(self,episode):
        self.__episode_list.append(episode)

    @property
    def chennel_name(self):
        return self.__chennel_name
    
    @property
    def episode_list(self):
        return self.__episode_list

class MediaList:
    def __init__(self):
        self.__media_list = []
    
    def add_media(self,media):
        self.__media_list.append(media)
    
    def play_all(self):
        for media in self.__media_list:
            media.play()
    @property
    def media_list(self):
        return self.__media_list

class Album(MediaList):
    def __init__(self,album_name,artist):
        super().__init__()
        self.__album_name = album_name
        self.__artist = artist

    def add_song(self,song):
        super().add_media(song)

    @property
    def album_name(self):
        return self.__album_name

class Artist:
    def __init__(self, artist_name):
        self.__artist_name = artist_name
        self.__album_list = []

    def add_album(self, album):
        self.__album_list.append(album)

    @property
    def artist_name(self):
        return self.__artist_name
    
    @property
    def album_list(self):
        return self.__album_list

class PlayList(MediaList):
    def __init__(self,name):
        super().__init__()
        self.__name = name

    def add_song(self,media):
        super().add_media(media)
    
    @property
    def name(self): 
        return self.__name

class MediaPlayer:
    def __init__(self):
        self.__artist_list = []
        self.__podcast_channel_list = []
        self.__playlist = []

    def add_playlist(self,playlist):
        self.__playlist.append(playlist)

    def add_podcast_channel(self,podcast_channel):
        self.__podcast_channel_list.append(podcast_channel)
    
    def play_podcast(self,podcast_name,channel_name):
        for podcast_channel in self.__podcast_channel_list:
            if podcast_channel.chennel_name == channel_name:
                for episode in podcast_channel.episode_list:
                    if episode.name == podcast_name:
                        episode.play()
                        break
    def play_song(self,song_name,artist_name,album_name):
        for artist in self.__artist_list:
            if artist.artist_name == artist_name:
                for album in artist.album_list:
                    if album.album_name == album_name:
                        for song in album.media_list:
                            if song.name == song_name:
                                song.play()
                                break
    
    def play_album(self,album_name,artist_name):
        for artist in self.__artist_list:
            if artist.artist_name == artist_name:
                for album in artist.album_list:
                    if album.album_name == album_name:
                        album.play_all()

    def play_playlist(self,playlist_name):
        for playlist in self.__playlist:
            if playlist.name == playlist_name:
                playlist.play_all()
    
    def search_song(self,name):
        for artist in self.__artist_list:
            for album in artist.album_list:
                if album.album_name == name:
                    album.play_all()
                else:
                    for song in album.media_list:
                        if song.name == name:
                            song.play()

