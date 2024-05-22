# Music Player -> Spotify , AppleMusic , etc.

class MusicPlayer:
    def __init__(self, implementation):
        self.implementation = implementation
        
    # bridge
    def play(self, song):
        self.implementation.play_song(song)
    
# Implementation
class MusicPlayerImplementation:
    def play_song(self, song):
        pass
    
# Concrete Implementations
class AppleMusic(MusicPlayerImplementation):
    def play_song(self, song):
        print(f"Playing {song} on Apple Music")
        
class Spotify(MusicPlayerImplementation):
    def play_song(self, song):
        print(f"Playing {song} on Spotify")
        
spotify_player = MusicPlayer(Spotify())

spotify_player.play('This is new day')

apple_music = MusicPlayer(AppleMusic())
apple_music.play('I want it all ')