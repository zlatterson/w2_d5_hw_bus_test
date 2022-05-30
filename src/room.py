from datetime import datetime

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.max_guests = 8
        self.guests = []
        self.songs = {}
        self.entry_fee = 10
        self.money = 0
        self.tab = {}

    def check_if_free_space(self):
        if len(self.guests) > self.max_guests:
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
        self.songs.setdefault(band,[])
        self.songs[band].append(song)

    def display_playlist(self, guest):
        reaction = guest.check_playlist(self.songs)
        return reaction

    def add_money(self, money):
        self.money += money

    def bar_request(self, guest, wanted_drink, drink_list):
        now = datetime.now()
        for drink in drink_list:
            if drink == wanted_drink:
                if guest.can_afford(drink_list[drink]):
                    guest.money -= drink_list[drink]
                    self.money += drink_list[drink]

                    cost_and_date = drink_list[drink], now.strftime("%H:%M")

                    self.tab.setdefault(guest.name,[])
                    self.tab[guest.name].append(cost_and_date)
        print(self.tab)



        
