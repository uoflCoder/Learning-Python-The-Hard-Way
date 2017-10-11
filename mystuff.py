#mystuff.py
def apple():
    print("I AM APPLES!")

tangerine = "Living reflection of a dream"


class MyStuff():

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
