class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        list_1 =[]
        list_1.append(self.name)
        list_1.append(self.next)
        list_1 = list(set(list_1))
        if len(list_1) ==1:
            return False
        else:
            return True

first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())