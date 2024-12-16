from datetime import date

words_list = [
    "apple", "banana", "grape", "orange", "peach", "pear", "plum", "cherry", "kiwi", "melon",
    "berry", "mango", "lemon", "lime", "papaya", "fig", "date", "coconut", "apricot", "avocado",
    "carrot", "potato", "tomato", "onion", "garlic", "pepper", "spinach", "broccoli", "cabbage", "lettuce",
    "bean", "pea", "corn", "rice", "wheat", "barley", "oat", "bread", "cheese", "butter",
    "milk", "yogurt", "cream", "egg", "meat", "fish", "chicken", "beef", "pork", "lamb",
    "cake", "cookie", "brownie", "pastry", "pie", "donut", "pancake", "waffle", "toast", "bagel",
    "syrup", "honey", "sugar", "chocolate", "candy", "peppermint", "marshmallow", "caramel", "icecream", "popcorn",
    "coffee", "tea", "water", "juice", "soda", "wine", "beer", "whiskey", "vodka", "rum",
    "pasta", "spaghetti", "pizza", "burger", "sandwich", "salad", "soup", "stew", "chili", "noodles",
    "sushi", "taco", "burrito", "quesadilla", "nachos", "samosa", "dumpling", "springroll", "pancake", "omelette",
    "knife", "fork", "spoon", "plate", "bowl", "cup", "glass", "straw", "napkin", "tray",
    "table", "chair", "lamp", "couch", "desk", "bookshelf", "bed", "pillow", "blanket", "wardrobe",
    "mirror", "window", "door", "wall", "ceiling", "floor", "roof", "stairs", "elevator", "balcony",
    "garden", "yard", "fence", "gate", "path", "driveway", "garage", "shed", "barn", "greenhouse",
    "car", "truck", "bus", "train", "plane", "boat", "bicycle", "motorcycle", "scooter", "skateboard",
    "road", "street", "avenue", "boulevard", "highway", "bridge", "tunnel", "intersection", "crosswalk", "sign",
    "clock", "watch", "calendar", "diary", "notebook", "pen", "pencil", "eraser", "ruler", "scissors",
    "book", "magazine", "newspaper", "novel", "dictionary", "atlas", "encyclopedia", "manual", "journal", "thesis",
    "computer", "laptop", "keyboard", "mouse", "monitor", "printer", "scanner", "speaker", "microphone", "camera",
    "phone", "tablet", "charger", "battery", "cable", "adapter", "flashdrive", "harddrive", "router", "modem",
    "cloud", "network", "server", "database", "software", "hardware", "system", "algorithm", "code", "program",
    "virus", "bug", "error", "debug", "test", "deploy", "release", "update", "patch", "version",
    "game", "puzzle", "riddle", "quiz", "challenge", "competition", "tournament", "match", "score", "goal",
    "team", "player", "coach", "referee", "stadium", "arena", "court", "field", "track", "pool",
    "mountain", "river", "lake", "forest", "desert", "ocean", "island", "beach", "cliff", "valley",
    "rain", "snow", "storm", "cloud", "wind", "sun", "moon", "star", "planet", "galaxy",
    "animal", "dog", "cat", "bird", "fish", "horse", "cow", "sheep", "pig", "rabbit",
    "lion", "tiger", "bear", "wolf", "elephant", "giraffe", "zebra", "monkey", "kangaroo", "panda",
    "house", "apartment", "building", "skyscraper", "factory", "warehouse", "store", "shop", "market", "mall",
    "city", "town", "village", "suburb", "country", "state", "province", "region", "district", "territory",
    "friend", "family", "neighbor", "colleague", "boss", "teacher", "student", "doctor", "nurse", "police",
    "firefighter", "soldier", "pilot", "driver", "engineer", "scientist", "artist", "musician", "actor", "writer","mountain", "river", "lake", "forest", "desert", "ocean", "island", "beach", "cliff", "valley",
    "rain", "snow", "storm", "cloud", "wind", "sun", "moon", "star", "planet", "galaxy",
    "animal", "dog", "cat", "bird", "fish", "horse", "cow", "sheep", "pig", "rabbit",
    "lion", "tiger", "bear", "wolf", "elephant", "giraffe", "zebra", "monkey", "kangaroo", "panda",
    "house", "apartment", "building", "skyscraper", "factory", "warehouse", "store", "shop", "market", "mall",
    "city"
]  


def get_word_of_the_day():
    today = date.today()
    day_of_year = today.timetuple().tm_yday  
    print(len(words_list),day_of_year)
    return words_list[day_of_year - 1]  