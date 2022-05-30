class Guest:
    def __init__(self, name, age, money, favourite_song):
        self.name = name
        self.age = age
        self.money = money
        self.favourite_song = favourite_song
        self.tab = 0

    def can_afford(self, fee):
        return self.money > fee

    def buy_entry(self, fee):
        check_can_afford = self.can_afford(fee)
        if check_can_afford:
            self.money -= fee
            return True
        return False

    def check_playlist(self, playlist):
        for songs in playlist:
            for song in playlist[songs]:
                if song == self.favourite_song:
                    return "That's my favourite song!"
                else:
                    return "I am indifferent to this playlist"



    