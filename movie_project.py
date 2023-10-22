# Movie Recommendation System
#Build data_base
def build_data_base(data_base):

    data_base["Wick"] = {"Genre": "Action", "Year" : 2023,"Duration": 120, "Rate": 9}
    data_base["Spiderman"] = {"Genre": "Action", "Year" : 2019,"Duration": 100, "Rate": 8.7}
    data_base["Naruto"] = {"Genre": "Anime", "Year" : 2014, "Duration": 90,"Rate": 10}
    data_base["3 under"] = {"Genre": "Action", "Year" : 2023, "Rate": 8}
    return data_base
# Function that add new movie in the data_base
def add_new_movie(data_base):
    keyword = "ALX_is_hard"
    password = input("Enter the password: ")
    if password != keyword:
        print("Wrong password try again!")
    else:
        name = input("Enter the name of the movie you want to add: ")
        genre = input("Enter the genre of the movie: ")
        year = int(input("Enter the release date of the movie: "))
        duration = int(input("Enter the duration"))
        rate = float(input("Enter the rating of the movie: "))
        data_base[name] = {"Name": name, "Genre": genre, "Year" : year, "Duration": duration,"Rate": rate}
        print("{} is successfully added".format)
    return data_base
def get_available_movie(data_base):
    if not data_base:
        print("Empty list")
    else:
        for key, value in data_base.items():
            print(key)
            print(value)
#Function that store use preference if found
def use_perference(data_base):
    preference = []
    choice = input("Enter Y for adding otherwise press N: ")
    while (choice == "Y"):
        user_pref = input("Enter your preferences: ")
        for movie, value in data_base.items():
            if user_pref in movie:
                print("Movie found: ")
                print(movie)
                preference.append(user_pref)

        choice = input("Enter Y for adding otherwise press N: ")
    
    return preference
#Function to give give movies sugesssion
def movie_suggession(data_base, user_pref=[]):
    
    value_search =  input("Enter the right value: genre, year, rate: ")
    search = input("Enter your preference: ")
    
    for movie, nested in data_base.items():
        if value_search in nested:
            if nested[value_search] == search:
                #print("Found a match: ", movie)
                user_pref.append(movie)
                
    if user_pref:
        for movie in user_pref:
            print(movie)
    else:
        print("No matches found")
def user_list(preference):
    for pref in preference:
        print("{:s} ".format(pref))
# Function that save the data_base
def save_data_base(data_base, filename, directory):
    import json
    with open(directory + filename, "w") as file_object:
        json.dump(data_base,file_object)
    print("Data has been saved to", filename)
# Function that load a database
def load_data_base(filename, directory):
    import json
    with open(directory + filename, "r") as file_object:
        data_base = json.load(file_object)
    print(f"Database loaded from {directory}{filename}")
    return data_base
#main program
import time
data_base = {}
user_perf = []
#data_base = build_data_base()
#movie_suggession(data_base, user_perf)
#directory = "c:/Users/User/Movie_project/"
#filename  = "movie_data.json"
directory = "C:/Users/User/"
filename = "My_data_base.json"


while (True):        
    print("User interface: \n")
    print("1. Get the database")
    print("2. Get all available movies")
    print("3. Get user preference")
    print("4. Get recommandation movie")
    print("5. Add new movie in a data_base")
    print("6. Print the users list")
    print("7. Save the data_base")
    print("8. Load data")
    print("9. Exit program")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            build_data_base(data_base)
        case 2:
            get_available_movie(data_base)
        case 3:
            user_perf = use_perference(data_base)
        case 4:
            movie_suggession(data_base, user_perf)
        case 5:
            data_base = add_new_movie(data_base)
        case 6:
            user_list(user_perf)
        case 7:
            save_data_base(data_base, filename, directory)
        case 8:
            data_base = load_data_base(filename, directory)
        case 9:
            break
        case _:
            print("Invalid option")
""" if (choice == 9):
        break
    elif (choice == 2):
        if not data_base:
            print("Empty database")
        else:
            for key, value in data_base.items():
                print(key)
                print(value)
    elif (choice == 3):
        user_perf = use_perference(data_base)
    elif (choice ==  5):
        add_new_movie(data_base)
    elif (choice == 6):
        user_list(user_perf)
    elif (choice == 7):
        save_data_base(data_base, filename, directory)
    elif (choice == 8):
        import json
        with open(directory + filename, "r") as file_object:
            data_base = json.load(file_object)
        print(f"Database loaded from {directory}{filename}")"""
