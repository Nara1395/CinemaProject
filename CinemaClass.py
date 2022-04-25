class CinemaClass():
    def __init__(self):
        self.movies_dict = {'Morbius': {'price': 8, 'max_slots': 10, 'total_bought': 0}}

    def add_movie(self, movie_name):
        print("\n----- Movie Details -----")
        print(f"Movie Name: {movie_name}")
        print(f"Movie Max Price: {self.movies_dict[movie_name]['price']}")
        print(f"Movie Max Slot: {self.movies_dict[movie_name]['max_slots']}")
        print("----- Movie Added -----\n")

    def get_movie_name(self):
        movie_name = input("Enter Movie Name: ")
        self.movies_dict[movie_name] = {}
        self.set_movie_price(movie_name)

    def set_movie_price(self, movie_name):
        movie_price = int(input("Enter Movie Price: "))
        self.movies_dict[movie_name]["price"] = movie_price
        self.set_movie_max_slot(movie_name)

    def set_movie_max_slot(self, movie_name):
        movie_max_slot = int(input("Enter Movie Max Slot: "))
        self.movies_dict[movie_name]["max_slots"] = movie_max_slot
        self.movies_dict[movie_name]["total_bought"] = 0
        self.add_movie(movie_name)

    def remove_movie(self):
        movie_remove = input("Enter Movie Name to be removed: ")
        self.movies_dict.pop(movie_remove)
        print(f"Movie: {movie_remove} has been deleted.")

    def buy_movie(self):
        for key, value in self.movies_dict.items():
            print(key)
        movie_name = input("Enter Movie Name to buy: ")
        print(f"Remaining Tickets: {self.movies_dict[movie_name]['max_slots']}")
        self.buy_movie_amount(movie_name)

    def buy_movie_amount(self, movie_name):
        amount_to_buy = int(input("Enter amount to buy: "))
        remaining_slots = self.movies_dict[movie_name]['max_slots'] - amount_to_buy
        self.movies_dict[movie_name]["total_bought"] += amount_to_buy
        self.movies_dict[movie_name]['max_slots'] = remaining_slots

    def show_movies(self):
        for key, value in self.movies_dict.items():
            print(f"{key} - ${value['price']}")

    def movie_menu(self):
        while True:
            print("----- Movie Interface -----")
            print("1 - Add Movie")
            print("2 - Remove Movie")
            print("3 - Buy Movie")
            print("4 - Show all Movies")
            print("0 - Exit Interface")
            option = input("Choose option: ")
            if option.strip() == "1":
                print("You have selected Option 1: Add - Movie")
                self.get_movie_name()
            elif option.strip() == "2":
                print("You have selected Option 2: Remove - Movie")
                self.remove_movie()
            elif option.strip() == "3":
                print("You have selected Option 3: Buy - Movie")
                self.buy_movie()
            elif option.strip() == "4":
                print("You have selected Option 4: Show all Movies")
                self.show_movies()
            elif option.strip() == "0":
                print("You have selected Option 0: Exit Interface")
                break
            else:
                print("Invalid Option")
