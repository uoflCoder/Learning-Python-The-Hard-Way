#Exercise 40

mystuff = {'apple':'I AM APPLES!'}
print(mystuff['apple'])


import mystuff
mystuff.apple()
print(mystuff.tangerine)


from mystuff import MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)

from mystuff import Song

your_song = Song(["And you should tell everybody",
                    "that this is your song",
                    "it might be quite simple but",
                    "now that it's done...."])

your_song.sing_me_a_song()
