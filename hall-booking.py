class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []

        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        shows_information = (id, movie_name, time)
        self._show_list.append(shows_information)

        seats = []
        for r in range(self._rows):
            row = []
            for c in range(self._cols):
                row.append('0')
            seats.append(row)
        self._seats[id] = seats


    def book_seats(self, show_id, book_seat):
        for row, col in book_seat:
            if not (1 <= row <= self._rows) or not (1 <= col <= self._cols):
                raise print("Invalid seat")

            if self._seats[show_id][row - 1][col - 1] != '0':
                raise print("Seat already booked")
            self._seats[show_id][row - 1][col - 1] = '1'

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, show_id):
        available_seats = self._seats[show_id]
        seat_matrix = "\n".join([" ".join(row) for row in available_seats])
        return seat_matrix

# Replica system

class Counter:
    def __init__(self, cinema):
        self._cinema = cinema

    def view_all_shows(self):
        all_shows = []
        for hall in self._cinema._hall_list:
            all_shows.extend(hall.view_show_list())
        return all_shows

    def booking_ticket(self, show_id, book_seat):
        for hall in self._cinema._hall_list:
            try:
                hall.book_seats(show_id, book_seat)
                print("\n")
                return f'Booking successfully for the show {show_id} and your seat is {book_seat}'
            except:
                pass

    def view_available_seats(self, show_id):
        for hall in self._cinema._hall_list:
            try:
                return hall.view_available_seats(show_id)
            except:
                pass
        raise print("Invalid show ID")


hall = Hall(7, 7, 1)
hall.entry_show("110", "Spider Man", "12:00 PM")
hall.entry_show("111", "Iron Man", "12:00 PM")

replica = Counter(Star_Cinema)

# handling all option

while True:
    print('\n')
    print("1. View all shows today")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")
    option = input("Enter option: ")

    print('\n')

    if option == "1":
        print(replica.view_all_shows())

    elif option == "2":
        show_id = input("Enter show ID: ")
        print('\n')
        try:
            print(replica.view_available_seats(show_id))
        except:
            pass

    elif option == "3":
        show_id = input("Enter show ID: ")
        num_tickets = int(input("Enter number of tickets: "))
        book_seat = []
        for _ in range(num_tickets):
            row = int(input("Enter seat row: "))
            col = int(input("Enter seat column: "))
            book_seat.append((row, col))
        try:
            print(replica.booking_ticket(show_id, book_seat))
        except:
            pass

    elif option == "4":
        break

