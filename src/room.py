class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        # self.max_guests = 8
        self.guests = []
        self.songs = {}
        self.entry_fee = 10
        self.money = 0

    def check_if_free_space(self):
        if len(self.guests) > 4:
            print("Sorry, max 3 people")
            return False
        return True

    def check_in_guest(self, guest):
        room_free = self.check_if_free_space()
        paid = guest.buy_entry(self.entry_fee)
        if room_free and paid:
            self.guests.append(guest.name)
            self.add_money(self.entry_fee)

    def add_song_to_room(self, band, song):
        dicty = self.songs
        dicty.setdefault(band,[])
        dicty[band].append(song)

    def display_playlist(self, guest):
        reaction = guest.check_playlist(self.songs)
        return reaction

    def add_money(self, money):
        self.money += money

