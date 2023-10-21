# Movie Recommendation System
#Build data_base
def build_data_base():

    data_base = {
        "Wick": {"Genre": "Action", "Year" : 2023, "Rate": 9},
        "Spiderman": {"Genre": "Action", "Year" : 2019, "Rate": 8.7},
        "Naruto" : {"Genre": "Anime", "Year" : 2014, "Rate": 10}
    }

    data_base["3 under"] = {"Genre": "Action", "Year" : 2023, "Rate": 8}
    return data_base
def add_new_movie(data_base):
    keyword = "ALX_is_hard"
    password = input("Enter the password")
    if password != keyword:
        print("Wrong password try again")
    else:
        name = input("Enter the name of the movie you want to add: ")
        genre = input("Enter the genre of the movie: ")
        year = int(input("Enter the release date of the movie: "))
        rate = float(input("Enter the rating of the movie: "))
        data_base[name] = {"Name": name, "Genre": genre, "Year" : year, "Rate": rate}
        print("{} is successfully added".format)
    return data_base

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
def user_list(preference):
    for pref in preference:
        print("{:s} ".format(pref))
#main program
data_base = {}
user_perf = []
data_base = build_data_base()
value_search =  input("Enter the right value: genre, year, rate")
search = input("Enter your preference: ")
for movie, nested in data_base.items():
    if value_search in nested:
        if nested[value_search] == search:
            #print("Found a match: ", movie)
            user_perf.append(movie)
if user_perf:
    for movie in user_perf:
        print(movie)
else:
    print("No matches found")


"""while (True):        
    print("User interface: \n")
    print("1. Get the database")
    print("2. Get all available movies")
    print("3. Get user preference")
    print("4. Get recommandation movie")
    print("5. Add new movie in a data_base")
    print("6. Print the users list")
    print("7. Exit program")
    choice = int(input("Enter your choice: "))
    if (choice == 7):
        break
    elif (choice == 2):
        for key, value in data_base.items():
            print(key)
            print(value)
    elif (choice == 3):
        user_perf = use_perference(data_base)
    elif (choice ==  5):
        add_new_movie(data_base)
    elif (choice == 6):
        user_list(user_perf)"""