import random
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def higher_lower():
    global score
    global game_over
    compare_a_key = random.choice(list(dictionary_a))
    compare_b_key = random.choice(list(dictionary_b))
    compare_a_value = dictionary_a[compare_a_key]
    compare_b_value = dictionary_b[compare_b_key]
    print(logo)
    print(f"Compare A: {compare_a_key}")
    print("\n" + vs)
    print(f"Compare B: {compare_b_key}")

    guess = input("Type 'A' for option A for 'B' for option B: ").lower()

    if guess == "a":
        if compare_a_value > compare_b_value:
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score: {score}.")
        elif compare_a_value < compare_b_value:
            game_over = True
            print(f"Wrong answer, you lose. Final score {score}")



    if guess == "b":
        if compare_b_value > compare_a_value:
            score += 1
            game_over = False
            print("\n" * 20)
            print(f"You're right! Current score: {score}.")
        elif compare_b_value < compare_a_value:
            game_over = True
            print(f"Wrong answer, you lose. Final score {score}")


dictionary_a = {
"NBA, a Club Basketball Competition, from United States." : 100,
"Cardi B, a Musician, frim United States." : 250,
}

dictionary_b = {
"Shakira, a Musician, from Colombia." : 200,
"Ronaldinho, a Footballer, fro Brazil." : 50,
}


print("Welcome to Higher or Lower!")
score = 0
game_over = False
while not game_over:
    higher_lower()


