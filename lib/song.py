# class Song:
#     # Class attribute for tracking the number of songs

#     count = 0
#     genres = []
#     artists = []
#     genre_count = {}
#     artist_count = {}

#     def __init__(self, name, artist, genre):
#         # Initialize a song with name, artist, and genre.
#         # Updating all class-level tracking attributes.

#         self.name = name
#         self.artist = artist
#         self.genre = genre

#         # Updating all tracking metrics
#         self.add_song_to_count()
#         self.add_to_genres()
#         self.add_to_artists()
#         self.add_to_genre_count()
#         self.add_to_artist_count()

#     @classmethod
#     def add_song_to_count(cls):
#         # incrementing the song counter
#         cls.count += 1

#     @classmethod
#     def add_to_genres(cls):
#         # Adding genre to the list of genres if not already there
#         if cls.genre not in cls.genres:
#             cls.genres.append(cls.genre)

#     @classmethod
#     def add_to_artists(cls):
#         # Adds new artist to artists list if not already present
#         if cls.artist not in cls.artists:
#             cls.artists.append(cls.artist)

#     @classmethod
#     def add_to_genre_count(cls):
#         # Update histogram of genres and their counts
#         # Get the current genre from the instance being initialized
#         current_genre = cls.genre
        
#         # Update the genre_count dictionary
#         if current_genre in cls.genre_count:
#             cls.genre_count[current_genre] += 1
#         else:
#             cls.genre_count[current_genre] = 1

#     @classmethod
#     def add_to_artist_count(cls):
#         # Update histogram of artists and their song counts
#         current_artist = cls.artist
        
#         if current_artist in cls.artist_count:
#             cls.artist_count[current_artist] += 1
#         else:
#             cls.artist_count[current_artist] = 1

class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update all tracking metrics
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1