class Song:
    lyrics = "Twinkle litte star"

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


Twinkle = Song(["Twinkle, twinkle little star, ",
                   "How I wonder what you are,",
                   "Up above the world so high,"])

Twinkle.sing_me_a_song()