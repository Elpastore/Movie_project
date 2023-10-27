# Movie Recommendation System
#Build data_base
def build_data_base():
    data_base = {}
    data_base["Hacules"] : {"Genre": "Action", "Year" : 2014, "Rate": 10}
    data_base["2000"] = {"Genre": "Action", "Year" : 2014, "Rate": 10},
    data_base["Titanic"] : {"Genre": "Romantic", "Year" : 2000, "Rate": 9}
    data_base["Wick"] = {"Genre": "Action", "Year" : 2023,"Duration": 120, "Rate": 9}
    data_base["Spiderman"] = {"Genre": "Action", "Year" : 2019,"Duration": 100, "Rate": 8.7}
    data_base["Naruto"] = {"Genre": "Anime", "Year" : 2014, "Duration": 90,"Rate": 10}
    data_base["300"] = {"Genre": "Action", "Year" : 2023, "Rate": 8}
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
    #C:/Users/User/Movie_project/filename
    with open(directory + filename, "w") as file_object:
        json.dump(data_base,file_object)
    print("Data has been saved to", filename)
# Function that load a database - Edited by JOHN
def load_data_base(filename, directory):
    import json
    if filename is None:
        filename = "My_data_base.json"
    if directory is None:
        directory = "./"  # Default to the current directory

    with open(directory + filename, "r") as file_object:
        data_base = json.load(file_object)
    print(f"Database loaded from {directory}{filename}")
    return data_base
# Function to save user movie list -JOHN'S TASK DONE
def save_user_movie_list(username, user_perf, filename=None, directory=None):
    import json
    if filename is None:
        filename = f"{username}'s_movie_list.json"
    if directory is None:
        directory = "./"  # Default to the current directory

    user_data = {}
    user_data[username] = user_perf
    with open(directory + filename, "w") as file_object:
        json.dump(user_data, file_object)
    print(f"User movie list for {username} has been saved to {filename}")

# Function for user login
def user_login(user_data):
    print("Welcom on our site!")
    print("Follow instruction to create your account")
    username = input("Username: ")
    password = input("Password: ")
    
    user_data[username] = password
    
    return user_data
# Function check for user login
def check_log(user_login):
    user_name = input("Enter your user name")
    for name, user_pass in user_login.items():
        if user_name == name:
            user_pass = input("Please enter your password")
            if user_pass == user_login[name]:
                print("Welcom{}".format(user_log))
                return True
                #Kester
                #load_data_base : check if the data empty
                #Add i new movie in the list
"""1. User name = Abdou
2. Pass_word = ********
dict = {"Adbou" : "Alx", "Eric" : "Hard", "Kester": "Easy"}
dict[key] ==>value
user_log = Kester"""
#main program
data_base = {}
user_data = {}
user_perf = []
#data_base = build_data_base()
#movie_suggession(data_base, user_perf)
directory = "./"
filename  = None
#directory = "C:/Users/User/"
#filename = "My_data_base.json"


# Condition in which user can get acces to the program and all available data  (Eric).

if not check_log:
    print("Failed to Authenticate User")
# print("Press 1 to Sign Up")
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
    print("9. Create an account")
    print("10. Save user movie list")
    print("11. Exit program")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            #build_data_base(data_base)
            print("Not available yet")
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
            user_data = user_login(user_data)
            for i in user_data.keys():
                print(i)
        case 10:
            username = input("Enter your username: ")
            save_user_movie_list(username, user_perf, filename, directory)
        case 11:
            break
        case _:
            print("Invalid option")