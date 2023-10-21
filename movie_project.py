# Movie Recommendation System
#Build data_base
data_base = {}
data_base = {
    "Wick": {"Genre": "Action", "Year" : 2023, "Rate": 9},
    "Spiderman": {"Genre": "Action", "Year" : 2019, "Rate": 8.7},
    "Naruto" : {"Genre": "Anime", "Year" : 2014, "Rate": 10}
}

data_base["3 under"] = {"Genre": "Action", "Year" : 2023, "Rate": 8}

while (True):        
    print("User interface: \n")
    print("1. Get the database")
    print("2. Get all available movies")
    print("3. Get user preference")
    print("4. Get recommandation movie")
    print("5. Add new movie in a data_base")
    print("6. Exit program")
    choice = int(input("Enter your choice: "))
    if (choice == 6):
        break
    if (choice == 2):
        for key, value in data_base.items():
            print(key)
            print(value)
    if (choice ==  5):
        keyword = "ALX_is_hard"
        password = input("Enter the password")
        if password == keyword:
            name = input("Enter the name of the movie you want to add: ")
            genre = input("Enter the genre of the movie: ")
            year = int(input("Enter the release date of the movie: "))
            rate = float(input("Enter the rating of the movie: "))
            data_base[name] = {"Name": name, "Genre": genre, "Year" : year, "Rate": rate}
        print("{} is successfully added".format)
    else:
        print("Wrong password try again")

        