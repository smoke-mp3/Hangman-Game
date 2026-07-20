import random
import tkinter as tk
from tkinter import messagebox

hangman_words = {
    "Sports": [
        "Soccer", "Basketball", "Baseball", "Football", "Tennis", "Cricket", "Volleyball", 
        "Badminton", "Swimming", "Gymnastics", "Boxing", "Hockey", "Golf", "Rugby", 
        "Surfing", "Skateboarding", "Cycling", "Archery", "Fencing", "Wrestling", 
        "Karate", "Taekwondo", "Judo", "Athletics", "Rowing", "Sailing", 
        "Canoeing", "Handball", "Water Polo", "Table Tennis", "Weightlifting", "Triathlon", 
        "Lacrosse", "Curling", "Bobsleigh", "Snowboarding", "Skiing", "Ice Skating", 
        "Figure Skating", "Softball", "Squash", "Racquetball", "Polo", "Cricket", 
        "Darts", "Bowling", "Billiards", "Snooker", "Kickboxing", "Muay Thai"],
    "Video Games": ["Minecraft", "Roblox", "Fortnite", "Pokemon", "PacMan", "Tetris", 
        "Super Mario", "Zelda", "Sonic", "Among Us", "Halo", "Call of Duty", 
        "Grand Theft Auto", "Skyrim", "Fallout", "The Witcher", "Cyberpunk", "Valorant", 
        "League of Legends", "Dota", "Overwatch", "Apex Legends", "Counter Strike", "World of Warcraft", 
        "Hades", "Terraria", "Stardew Valley", "Animal Crossing", "Splatoon", "Super Smash Bros", 
        "Elden Ring", "Dark Souls", "Bloodborne", "Resident Evil", "Silent Hill", "Tomb Raider", 
        "Uncharted", "The Last of Us", "God of War", "SpiderMan", "Red Dead Redemption", "Assassin Creed", 
        "Borderlands", "BioShock", "Mass Effect", "Dragon Age", "Final Fantasy", "Kingdom Hearts", 
        "Monster Hunter", "Street Fighter", "Mortal Kombat", "Tekken", "Doom", "Wolfenstein", 
        "Portal", "Half Life", "Left 4 Dead", "Team Fortress", "Rocket League", "Fifa"],
    "Professions": ["Doctor", "Teacher", "Engineer", "Artist", "Chef", "Pilot", 
        "Firefighter", "Scientist", "Astronaut", "Lawyer", "Nurse", "Farmer", 
        "Architect", "Carpenter", "Electrician", "Plumber", "Mechanic", "Welder", 
        "Programmer", "Web Designer", "Data Analyst", "Accountant", "Banker", "Economist", 
        "Journalist", "Writer", "Editor", "Photographer", "Videographer", "Animator", 
        "Graphic Designer", "Fashion Designer", "Interior Designer", "Musician", "Singer",
        "Actor", "Director", "Producer", "Librarian", "Historian", "Archaeologist", 
        "Psychologist", "Therapist", "Pharmacist", "Dentist", "Surgeon", "Veterinarian", 
        "Biologist", "Chemist", "Physicist", "Geologist", "Meteorologist", "Astronomer", 
        "Politician", "Diplomat", "Judge", "Police Officer", "Detective", "Soldier"],
    "Cartoons": ["Looney Tunes", "Tom and Jerry","Toy Story", "Shrek", "The Matrix", "Inception", "Titanic", "Avatar", 
    "Star Wars", "Jurassic Park", "Avengers", "Frozen", "Lion King", "Gladiator", "Mickey Mouse and Friends", "Scooby-Doo", "The Flintstones", "The Jetsons",
        "Popeye the Sailor", "SpongeBob SquarePants", "Dexter's Laboratory", "The Powerpuff Girls", "Courage the Cowardly Dog", "Ed Edd n Eddy",
        "Johnny Bravo", "Rugrats", "Avatar The Last Airbender", "Ben 10", "Adventure Time", "Regular Show",
        "The Amazing World of Gumball", "Phineas and Ferb", "Gravity Falls", "Steven Universe", "Kim Possible", "The Simpsons",
        "Family Guy", "South Park", "Rick and Morty", "American Dad", "Futurama", "Bob's Burgers"],
    "Countries": ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", 
        "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", 
        "Azerbaijan", "Bahamas", "Bahrain", "Barbados", "Belarus", "Belgium", 
        "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
        "British Virgin Islands", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", 
        "Cameroon", "Canada", "Cabo Verde", "Central African Republic", "Chad", "Chile", "China", 
        "Christmas Island", "Cocos Islands", "Colombia", "Comoros", "Congo", "Democratic Republic of the Congo", 
        "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cyprus", "Czechia", "Denmark", 
        "Djibouti", "Dominica", "Dominican Republic", "Timor-Leste", "Ecuador", "Egypt", "El Salvador", 
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Falkland Islands", 
        "Micronesia", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "Gabon", 
        "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Grenada", "Guadeloupe", 
        "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", 
        "Iceland", "India", "Indonesia", "Iraq", "Ireland","Italy", "Jamaica", 
        "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", 
        "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", 
        "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", 
        "Martinique", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", 
        "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", 
        "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", 
        "Norfolk Island", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", 
        "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
        "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Samoa", 
        "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", 
        "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", 
        "South Africa", "South Georgia and the South Sandwich Islands", "South Korea", "South Sudan", 
        "Spain", "Sri Lanka", "Sudan", "St. Vincent and the Grenadines", "Suriname", 
        "Svalbard and Jan Mayen", "Sweden", "Switzerland", "Taiwan", "Tajikistan", "Tanzania", 
        "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", 
        "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Wallis and Futuna", 
        "Western Sahara", "Yemen", "Zambia", "Zimbabwe"],
    "Animals": ["Aardvark", "Albatross", "Alligator", "Alpaca", "Anteater", "Antelope", "Armadillo",
        "Badger", "Bat", "Bear", "Beaver", "Bison", "Buffalo", "Butterfly",
        "Camel", "Cheetah", "Chimpanzee", "Cobra", "Crocodile", "Cow",
        "Deer", "Dingo", "Dolphin", "Donkey", "Duck",
        "Eagle", "Elephant", "Elk",
        "Falcon", "Ferret", "Flamingo", "Fox", "Frog",
        "Gazelle", "Giraffe", "Goat", "Gorilla",
        "Hamster", "Hawk", "Hedgehog", "Hippopotamus", "Horse",
        "Iguana", "Impala",
        "Jaguar", "Jellyfish",
        "Kangaroo", "Koala",
        "Lemur", "Leopard", "Lion", "Llama",
        "Manatee", "Meerkat", "Monkey", "Moose",
        "Narwhal", "Newt",
        "Octopus", "Ostrich", "Otter", "Owl",
        "Panda", "Panther", "Parrot", "Penguin", "Pig", "Porcupine",
        "Quail",
        "Rabbit", "Raccoon", "Rat", "Rhinoceros",
        "Salamander", "Seal", "Shark", "Sheep", "Skunk", "Snake", "Squirrel",
        "Tiger", "Toad", "Tortoise", "Turkey",
        "Urchin",
        "Vulture",
        "Walrus", "Whale", "Wolf", "Woodpecker",
        "Xerus",
        "Yak",
        "Zebra"],
    "Foods": ["acai berry", "acini de pepe", "Aero chocolate bar", "agar agar", "almonds", "Alphabits cereal",
        "aloo gobi", "angel food cake", "angel hair pasta", "animal crackers", "apple", "Apple Jacks cereal",
        "applesauce", "apricot", "artichokes", "asiago cheese", "aubergine", "avocado", "bacon",
        "bagel", "baker's chocolate", "baklava", "balsamic dressing", "banana", "banana bread", "barbecue",
        "barley", "basil", "basmati rice", "BBQ", "bean salad", "bean sprouts", "beans", "beef",
        "beets", "bird's nest cookies", "bird's nest soup", "biscuit", "biscuits", "blackberry", "black bean buns",
        "black eyed peas", "black forest cake", "blueberry", "blueberry muffins", "Bok choy", "bologna",
        "borscht", "brains", "bread", "breadfruit", "breasts of chicken", "broccoli", "brownie", "brussel sprouts",
        "Bruschetta", "buffalo meat", "buffalo wings", "bulgur", "bun", "bundt cake", "burrito", "butter",
        "butter chicken", "butter squash", "cabbage", "cabbage rolls", "Caesar salad", "Caflib", "cake",
        "California dressing", "candy", "candy cane", "cannoli", "cantaloupe", "Caramel", "carrot cake", "carrots",
        "cashews", "cassava", "casserole", "cauliflower", "caviar", "celery", "cereal", "chalupas",
        "chamomile tea", "chapatis", "Cheddar cheese", "cheesecake", "cheeseburger", "cheesesteak", "Cheerios", "Cheetos",
        "cherry", "Chex Mix", "chick peas", "chicken", "chili con carne", "Chinese food", "chocolate", "chocolate chips",
        "chow mien noodles", "chowder", "chunky peanut butter", "churros", "chutney", "cider", "cilantro", "clams",
        "cobbler", "cocoa", "coconut", "cod", "coffee", "Coffee Crisp", "coleslaw", "compote", "cookies",
        "corn", "corn chips", "corn flakes", "corn fritters", "cornbread", "corndog", "cows tongue", "crab",
        "crabcakes", "cracker", "cranberries", "cranberry sauce", "crawfish", "cream cheese", "cream of mushroom", "cream puff",
        "creamsicle", "crepe", "Crème Brule", "croissants", "croutons", "cucumber", "cumquat", "currants",
        "curry", "custard", "dahl soup", "dairy", "dandelion greens", "Danish", "dark chocolate", "dates",
        "deviled eggs", "dill", "dill pickles", "dim sum", "Ding Dongs", "ditalini pasta", "dolmades", "donut",
        "Doritos", "Dream whip", "drumsticks", "duck", "durian", "Dutch apple pie", "Dutch cookies", "eclairs",
        "edamame", "egg nog", "eggplant", "eggroll", "eggs", "Eggs Benedict", "elbow macaroni", "elephant ears",
        "English muffin", "Eskimo pie", "escarole", "espresso", "fajitas", "falafal", "Fasolada soup", "feta",
        "fettuccine", "fiddlestick greens", "Fig Newtons", "figs", "fish", "flap jacks", "flapjacks", "flax oil",
        "flax seeds", "flour", "focaccia bread", "fortune cookie", "frankfurters", "free range eggs", "french fries", "french toast",
        "fricassee", "fried pie", "fried rice", "fritters", "frosting", "fruit", "fruit pie", "fruit salad",
        "fruitcake", "fudge", "fudgicle", "funnel cake", "gailan", "gala apples", "garbonzo", "garlic",
        "garlic bread", "gavioli", "gazpacho", "gelatin", "gelato", "giblets", "ginger", "ginger ale",
        "ginger beer", "gingerbread", "gizzards", "goat's milk", "goulash", "graham crackers", "granola", "grapefruit",
        "grapes", "grapeseed oil", "gravy", "green beans", "green olives", "green pepper", "guacamole", "guava",
        "gumbo", "gyoza", "haggis", "halibut", "ham", "hamburger", "hash browns", "Heinz ketchup", "herbs",
        "herrings", "hoagie", "Ho Ho's", "hog jowl", "Hollandaise", "hominy", "honey", "honey bun",
        "honeydew", "hot chocolate", "hot dog", "huckleberries", "hummus", "ice cream", "iced doughnut", "iced tea",
        "icee", "iceberg lettuce", "icing", "icing sugar", "Imitation crab", "imitation baco bits", "Impastata cheese", "Indian curry",
        "Indian jujubee", "Indian pudding", "infant formula", "instant coffee", "instant oatmeal", "irish stew", "ita palm", "italian bread",
        "italian dressing", "icy pole", "jalapeño", "jam", "jambalaya", "Jamaican patties", "Jell-O", "jelly",
        "jerky", "Jujubes", "juice", "kale", "kamut", "ketchup", "kidney beans", "kielbasa", "kiwi",
        "Kit Kat candy bar", "Kix cereal", "Knorr soup", "kohlrabi", "Kool-Aid", "Kraft dinner", "Kraft dressing", "kumquat",
        "lamb", "lasagna", "legumes", "lemon tarts", "lemonade", "lemons", "lentils", "lettuce",
        "licorice", "Life cereal", "lima bean", "linguine", "Little Debbies Snack Cakes", "liver", "liverwurst", "lobster",
        "long john donuts", "macaroni", "mackerel", "mahi-mahi", "mango", "manicotti", "maple syrup", "maraschino cherries",
        "margarine", "marmalade", "marmite", "marshmallows", "Mars bar", "martimonial cake", "masala", "mashed potatoes",
        "mayhaws", "mayonnaise", "meatloaf", "melon", "milk", "mince meat", "minestrone", "miso",
        "mozzarella", "muffin", "mushrooms", "mustard", "naan bread", "nachos", "Nalley’s chips", "Neapolitan ice cream",
        "Necco Wafers", "nectarines", "Nestle’s chocolate", "Neufatual cheese", "noodles", "nuggets", "Nutter-Butter Cookies",
        "nuts", "oat cakes", "oatmeal", "octopus", "okra", "Old Dutch chips", "olives", "omelet",
        "onion", "orange", "oregano", "organic salad", "Oreo cookies", "orzo", "ostrich eggs", "Ovaltine",
        "ox tail", "oysters", "paella", "pakora", "pancetta", "pancake", "papaya", "paprika",
        "parmesan", "parsley", "parsnips", "passionfruit", "pasta", "pastry", "pate", "pavlova",
        "peaches", "peanuts", "peanut butter", "pears", "pecans", "peking duck", "peppermint", "pepperoni",
        "peppers", "perch", "perogies", "persimmons", "pesto", "pickles", "pie", "pilaf",
        "pimentos", "pine nuts", "pineapple", "pinto beans", "pistachios", "pita bread", "pizza", "plantain",
        "plum", "plum sauce", "poi", "polenta", "pollock", "pomegranate", "popcorn", "popsicles",
        "pork", "porridge", "portabello mushrooms", "pot roast", "potatoes", "potato chips", "poutine", "prawns",
        "pretzels", "protein bars", "protein shakes", "pudding", "puffed wheat", "pumpernickel", "pumpkin", "putanesca",
        "quail", "quaker oatmeal", "quakes rice cakes", "quesadilla", "quiche", "quick oats", "quince", "quinoa",
        "quorn", "radicchio", "radish", "ramen", "raspberry", "ratatouille", "ravioli", "red delicious",
        "red lentils", "refried beans", "relish", "reuben sandwich", "rhubarb", "rice", "rice crackers", "rice paper",
        "ricotta cheese", "rigatoni", "rissotto", "ritz crackers", "rocky road ice cream", "roll-ups", "rolls", "romaine",
        "romano cheese", "rooibos", "rosehips", "roti", "salad",
        "salami", "salmon", "salsa", "samosa", "sandwich", "sasparilla", "sashimi", "satsuma",
        "sauce", "sausage", "scones", "sesame oil", "sesame seeds", "shallot", "shark fin soup", "shells",
        "shepherd's pie", "sherbet", "shish kabob", "shortbread", "shortcake", "shredded wheat", "shrimp", "skor's bars",
        "slop joes", "slushies", "smoothie shake", "smores", "snow peas", "soup", "sour cream", "soybean",
        "soysauce", "spaghetti", "spam", "spanish rice", "spanokopita", "sashimi", "spelt", "spinach",
        "spinach dip", "split peas", "squash", "squid", "starfruit", "starburst", "steak",
        "stoned wheat crackers", "string cheese", "stromboli", "stuffing", "succotash", "sundae", "sunflower seeds", "sushi",
        "sweet and sour", "sweet potato", "swiss chard", "swiss cheese", "swordfish", "tabasco pepper sauce", "tabbouleh salad", "taco",
        "taffy", "tahini", "tamale", "tamarind", "tangerine", "tapioca", "tarts", "tater tots",
        "tempeh", "tempura", "teriyaki", "thimbleberry", "thousand island salad dressing", "toast", "tofu",
        "tortellini", "tortillas", "torte", "tostitos", "tossed salad", "trifle", "triscuits", "truffle",
        "tuna", "turkey", "turmeric", "turnip",  "twinkies", "twizzlers",
     "unpasteurized milk", "upside down cake", "vakalolo", "vanilla", "veal", "vegetable soup", "vegetables",
        "vegemite", "venison", "vermicelli", "vichyssoise", "vidalia onion", "vine leaves", "vinegar", "virgin oil",
     "vomit fruit", "wafer", "waffles", "waldorf salad", "walleye fish", "walnuts", "wasabi",
        "water", "watercress", "watermelon", "wax bean", "wheat bread", "wild rice", "wings", "wonder bread",
        "wontons", "xigua", "xmas cake", "yaki soba", "yautia", "yellow beans",
         "yogurt", "yolk", "yorkshire pudding", "yucca", "zabaraglione sauce", "zander fish", "ziti",]}

chosen_category = random.choice(list(hangman_words.keys()))
chosen_word = random.choice(hangman_words[chosen_category])
word_to_guess = chosen_word.lower() 

guessed_letters = []
attempts = 6

window = tk.Tk()
window.title("Hangman Game")

def is_game_over():
    return check_win() or check_loss()

def check_loss():
    return attempts == 0

def check_win():
    return all((letter in guessed_letters or letter == " ") for letter in word_to_guess)

def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            messagebox.showinfo("Info", "You already guessed that letter.")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Congratulations!", "You've won!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_word_display()
            update_attempts_display() 
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Game Over", f"You've lost! The word was: {chosen_word}")
                reset_game()
        letter_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a single valid letter.")  

def reset_game():
    global chosen_category, chosen_word, word_to_guess, guessed_letters, attempts
    
    chosen_category = random.choice(list(hangman_words.keys()))
    chosen_word = random.choice(hangman_words[chosen_category])
    word_to_guess = chosen_word.lower()
    
    guessed_letters = []
    attempts = 6
    
    category_label.config(text=f"Category: {chosen_category}")
    update_word_display()
    update_attempts_display()
    draw_hangman()    

def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter == " ":
            display_word += "  "
        elif letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_label.config(text=display_word.strip())
            
def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}")

def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125, 120, 175, 170, width=4, tags="hangman")
    if attempts < 5:
        canvas.create_line(150, 170, 150, 220, width=4, tags="hangman")
    if attempts < 4:
        canvas.create_line(150, 185, 125, 210, width=4, tags="hangman")
    if attempts < 3:
        canvas.create_line(150, 185, 175, 210, width=4, tags="hangman")
    if attempts < 2:
        canvas.create_line(150, 220, 125, 250, width=4, tags="hangman")
    if attempts < 1:
        canvas.create_line(150, 220, 175, 250, width=4, tags="hangman")

category_label = tk.Label(window, text=f"Category: {chosen_category}", font=("Arial", 16, "bold"))
category_label.pack(pady=5)

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()
canvas.create_line(50, 250, 250, 250, width=4)  
canvas.create_line(200, 250, 200, 100, width=4) 
canvas.create_line(100, 100, 200, 100, width=4)  
canvas.create_line(150, 100, 150, 120, width=4) 

word_label = tk.Label(window, text="", font=("Arial", 24))
word_label.pack(pady=10)

attempts_label = tk.Label(window, text="", font=("Arial", 16))
attempts_label.pack(pady=5)

letter_entry = tk.Entry(window, font=("Arial", 16), width=5, justify="center")
letter_entry.pack(pady=5)

guess_button = tk.Button(window, text="Guess", command=guess_letter)
guess_button.pack(pady=2)

reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.pack(pady=2)
update_word_display()
update_attempts_display()
draw_hangman()

window.mainloop()
