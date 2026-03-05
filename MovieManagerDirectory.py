class Movie:
    def __init__(self, movie_id, title, director, release_year, genre):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def display(self):
        print(f"\nID: {self.movie_id}")
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Release Year: {self.release_year}")
        print(f"Genre: {self.genre}")

movie_list=[]

def is_unique_id(movie_id):
    for movie in movie_list:
        if movie.movie_id == movie_id:
            return False
    return True

def add_movie():
    print("\n Add a New Movie")
    movie_id = input("Enter Movie ID: ")
    if not is_unique_id(movie_id):
        print("Movie ID already exists. Please try again")
        return

    title = input("Enter Title: ")
    director = input("Enter Director: ")

    try:
        release_year = int(input("Enter Release Year: "))
    except ValueError:
        print("Release year must be a number!")
        return

    genre = input("Enter Genre: ")

    new_movie = Movie(movie_id, title, director, release_year, genre)
    movie_list.append(new_movie)
    print("Movie Added Successfully!")

def view_movies():
    print("\n All Movies")
    if not movie_list:
        print("No Movies in the Collection!")
        return
    for movie in movie_list:
        movie.display()

def search_movie():
    print("\n Search Movie by Title")
    title = input("Enter title to search: ").lower()
    found = False
    for movie in movie_list:
        if movie.title.lower() == title:
            movie.display()
            found = True
    if not found:
        print("No Movie Found with that Title!")

def update_movie():
    print("\n Update Movie")
    movie_id = input("Enter Movie ID: ")
    for movie in movie_list:
        if movie.movie_id == movie_id:
            print("Leave field blank.")
            new_title = input(f"New title [{movie.title}]: ") or movie.title
            new_director = input(f"New director [{movie.director}]: ") or movie.director
            new_genre = input(f"New genre [{movie.genre}]: ") or movie.genre

            try:
                new_year_input = input(f"New release year [{movie.release_year}]: ")
                new_year = int(new_year_input) if new_year_input else movie.release_year
            except ValueError:
                print("Invalid Year!")
                return

            movie.title = new_title
            movie.director = new_director
            movie.genre = new_genre
            movie.release_year = new_year

            print("Movie Updated!")
            return
        print("Empty!")

def delete_movie():
    print("\n Delete Movie")
    movie_id = input("Enter Movie ID: ")
    for movie in movie_list:
        if movie.movie_id == movie_id:
            movie_list.remove(movie)
            print("Movie Deleted!")
            return
    print("Empty!")

def menu():
    while True:
        print("\n*** Movie Manager Directory ***")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie by Title")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            search_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            delete_movie()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

menu()
