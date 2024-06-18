import random

# List of everyday objects
objects = [
    "toothbrush", "remote control", "laptop", "backpack", "water bottle", "socks", "coffee mug", "notebook",
    "pencil", "phone charger", "frying pan", "knife", "cutting board", "spatula", "baking sheet", "casserole dish",
    "blender", "microwave", "toaster", "air fryer", "dish soap", "laundry detergent", "vacuum cleaner", "mop",
    "broom", "dustpan", "bucket", "glass cleaner", "dish sponge", "scrub brush", "cleaning gloves", "iron", 
    "ironing board", "laundry basket", "hanger", "washing machine", "dryer", "bed sheets", "blanket", "pillow",
    "towel", "bath mat", "toilet paper", "shower curtain", "toothpaste", "hairbrush", "shampoo", "conditioner",
    "soap", "deodorant", "razor", "scissors", "tape measure", "hammer", "screwdriver", "pliers", "drill", "nails",
    "screws", "wrench", "allen wrench", "flashlight", "batteries", "extension cord", "power strip", "water filter",
    "can opener", "coffee maker", "kettle", "measuring cups", "measuring spoons", "mixing bowls", "plate", "bowl",
    "cutlery", "glassware", "mug", "tumbler", "thermos", "food storage container", "whisk", "corkscrew", "cheese grater",
    "colander", "strainer", "kitchen scissors", "pot", "saucepan", "stock pot", "oven mitt", "kitchen towel", 
    "cutting board", "ladle", "slotted spoon", "tongs", "vegetable peeler", "apple corer", "grater", "zester",
    "food processor", "stand mixer", "waffle maker", "rice cooker", "slow cooker", "pressure cooker", "electric grill",
    "microwave oven", "oven", "stove", "refrigerator", "freezer", "dishwasher", "trash can", "recycling bin", "compost bin",
    "garden hose", "lawn mower", "rake", "shovel", "pruning shears", "watering can", "plant pot", "garden gloves",
    "wheelbarrow", "broom", "dustpan", "mop", "bucket", "window cleaner", "mirror", "frame", "calendar", "clock", "lamp",
    "light bulb", "candle", "fire extinguisher", "smoke detector", "carbon monoxide detector", "first aid kit", "bandage",
    "thermometer", "pain reliever", "antiseptic", "cotton swabs", "tweezers", "scissors", "nail clipper", "nail file",
    "sunscreen", "insect repellent", "umbrella", "raincoat", "hat", "gloves", "scarf", "sunglasses", "wallet", "keys",
    "backpack", "luggage", "passport", "identification card", "phone", "tablet", "laptop", "charger", "earphones", "mouse",
    "keyboard", "monitor", "printer", "scanner", "camera", "tripod", "memory card", "USB drive", "hard drive", "router",
    "modem", "speaker", "microphone", "webcam", "remote control", "game console", "joystick", "VR headset", "smartwatch"
]

# List of funny titles
funny_titles = {
    "toothbrush": "Commander of Clean Teeth",
    "remote control": "Master of the Channels",
    "laptop": "Overlord of Emails",
    "backpack": "Carrier of Chaos",
    "water bottle": "H2O Guardian",
    "socks": "Feet Warmth Wizard",
    "coffee mug": "Elixir Holder",
    "notebook": "Scribble Sage",
    "pencil": "Graphite Sorcerer",
    "phone charger": "Battery Reviver",
    # ... add more mappings as needed
}

# Simple jokes
jokes = {
    "toothbrush": "Why did the toothbrush go to school? Because it wanted to brush up on its studies!",
    "remote control": "Why did the remote control get promoted? Because it was always in control!",
    "laptop": "Why was the laptop always invited to parties? Because it knew how to crash them!",
    "backpack": "Why was the backpack so good at keeping secrets? Because it was a carrier of chaos!",
    "water bottle": "Why did the water bottle go to therapy? Because it had too many emotional spills!",
    "socks": "Why don't socks ever get lost? Because they always stay paired up!",
    "coffee mug": "Why did the coffee mug file a police report? It got mugged!",
    "notebook": "Why did the notebook go on a diet? It wanted to reduce its margins!",
    "pencil": "Why did the pencil seem unreliable? It kept breaking under pressure!",
    "phone charger": "Why was the phone charger always so calm? Because it knew how to keep things charged!",
    # ... add more jokes as needed
}

def ask_questions():
    print("Think of an everyday object and I'll try to guess it!")
    print("Answer the following questions with 'yes' or 'no':")
    questions = [
        "Is it something you use daily?",
        "Is it found in the kitchen?",
        "Can it fit in your pocket?",
        "Is it something electronic?",
        "Is it used for cleaning?",
        # Add more questions as needed
    ]
    for question in questions:
        response = input(question + " ")
        if response.lower() not in ["yes", "no"]:
            print("Please answer with 'yes' or 'no'.")
            return None
    return input("Great! What is the object you are thinking of? ").lower()

def respond_with_joke(obj):
    if obj in funny_titles:
        title = funny_titles[obj]
        joke = jokes[obj]
        print(f"Oh, you are using the {obj}? You mean the {title}? {joke}")
    else:
        print("Hmm, I couldn't find that object in my database. Try another one!")

def main():
    obj = ask_questions()
    if obj:
        respond_with_joke(obj)

if __name__ == "__main__":
    main()
