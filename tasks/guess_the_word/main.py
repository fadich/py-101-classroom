"""
Комп"ютер загадує слово зі списку words і пропонує користувачеві відгатати його за шість спроб.

Користувач вводе слово, а комп"ютер "відповідає" на нього таким чином:
- яккщо літера не зістрічається в загаданому слові, на її місці комп"ютер ставить крапку (.);
- якщо літера зустрічається, але на іншому місці - знак питання (?);
- якщо литера є і знаходиться на правильній позиції - знак оклику (!).

Приклад. Загадане слово - "Agent". Користувач вводить "Angel", відповідь комп"ютера повинна бути:
<<< !???.  # 1 літера - вірно; 2,3,4 - є такі, але на інших позиціяї; 5 літера в слові відсутня

Якщо користувач не відгадав слово за 6 спроб - програма завершується і коп"ютер виводить загадане слово.

!!! Зверніть увагу, що літери в словах можуть повторюватись:
Якщо користувач вводить "focus", то для загаданого "Class" потрібно вивести "..?.!" - остання літера вірна


-------------------- Додатково --------------------

1. Зробити гру регістронезалежною (не важливо, маленькі чи великі літери вводяться).

2. Зробити валідацію того, що вводить користувач: лише 5 літер латінецею
   (якщо користувач ввів щось невірне - ця спроба не рахується і комп"ютер лише пропонує ввести ще раз).

3. Ввести в гру підрахунок балів - на свій розсуд. Врахуйте, чи вгадана літера, чи на правильному місці, з якої спроби,
                                                                                                                   тощо.

"""

import string
import random


words = [
    "Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis", "Beach", "Birth", "Block", "Blood", "Board", "Brain",
    "Bread", "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest", "Chief", "Child", "China", "Claim", "Class",
    "Clock", "Coach", "Coast", "Court", "Cover", "Cream", "Crime", "Cross", "Crowd", "Crown", "Cycle", "Dance", "Death",
    "Depth", "Doubt", "Draft", "Drama", "Dream", "Dress", "Drink", "Drive", "Earth", "Enemy", "Entry", "Error", "Event",
    "Faith", "Fault", "Field", "Fight", "Final", "Floor", "Focus", "Force", "Frame", "Frank", "Front", "Fruit", "Glass",
    "Grant", "Grass", "Green", "Group", "Guide", "Heart", "Henry", "Horse", "Hotel", "House", "Image", "Index", "Input",
    "Issue", "Japan", "Jones", "Judge", "Knife", "Laura", "Layer", "Level", "Lewis", "Light", "Limit", "Lunch", "Major",
    "March", "Match", "Metal", "Model", "Money", "Month", "Motor", "Mouth", "Music", "Night", "Noise", "North", "Novel",
    "Nurse", "Offer", "Order", "Other", "Owner", "Panel", "Paper", "Party", "Peace", "Peter", "Phase", "Phone", "Piece",
    "Pilot", "Pitch", "Place", "Plane", "Plant", "Plate", "Point", "Pound", "Power", "Press", "Price", "Pride", "Prize",
    "Proof", "Queen", "Radio", "Range", "Ratio", "Reply", "Right", "River", "Round", "Route", "Rugby", "Scale", "Scene",
    "Scope", "Score", "Sense", "Shape", "Share", "Sheep", "Sheet", "Shift", "Shirt", "Shock", "Sight", "Simon", "Skill",
    "Sleep", "Smile", "Smith", "Smoke", "Sound", "South", "Space", "Speed", "Spite", "Sport", "Squad", "Staff", "Stage",
    "Start", "State", "Steam", "Steel", "Stock", "Stone", "Store", "Study", "Stuff", "Style", "Sugar", "Table", "Taste",
    "Terry", "Theme", "Thing", "Title", "Total", "Touch", "Tower", "Track", "Trade", "Train", "Trend", "Trial", "Trust",
    "Truth", "Uncle", "Union", "Unity", "Value", "Video", "Visit", "Voice", "Waste", "Watch", "Water", "While", "White",
    "Whole", "Woman", "World", "Youth",
]


LETTER_RIGHT_POSITION = "!"
LETTER_WRONG_POSITION = "?"
LETTER_MISSED = "."


def init_game():
    target_word = random.choice(words).lower()

    i = 0
    while i < 6:
        player_letters = list(input(f"[{i + 1}/6] >>> ").lower())

        if len(player_letters) != 5:
            print("Only five-letter-words supported")
            continue

        if set(player_letters) - set(string.ascii_lowercase):
            print("Unsupported symbols, use letters instead")
            continue

        target_letters = list(target_word)

        # Find the right-position letters
        for position, letter in enumerate(player_letters):
            if letter == target_letters[position]:
                player_letters[position] = LETTER_RIGHT_POSITION
                target_letters[position] = None  # Mark as "found"

        target_letters = [i for i in target_letters if i]  # Filter target letter

        # Find wrong-position or missed letters
        for position, letter in enumerate(player_letters):
            if letter == LETTER_RIGHT_POSITION:
                continue

            if letter in target_letters:
                player_letters[position] = LETTER_WRONG_POSITION
                target_letters.remove(letter)  # Just not to make duplicates
            else:
                player_letters[position] = LETTER_MISSED

        if player_letters == [LETTER_RIGHT_POSITION] * 5:
            print("Congrats, you've won!")
            break

        print("".join(player_letters))

        i += 1
    else:
        print(f"Sorry, you lost. The guessed word is {target_word}")


def loop_game():
    while True:
        init_game()

        if input("\nWant to play again [Y/n]? ").lower() not in ["", "y", "yes"]:
            break


if __name__ == "__main__":
    try:
        loop_game()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nGoodbye!")
