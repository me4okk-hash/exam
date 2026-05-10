import random

def load_words():
    try:
        with open("words.txt", "r") as file:
            return file.read().lower().split()

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except:
        print("Помилка читання файлу")
        return []


def save_result(word, result):
    with open("history.txt", "a") as file:
        file.write(f"{word} - {result}\n")


def show_history():
    try:
        with open("history.txt", "r") as file:
            print("\nІсторія ігор:")
            print(file.read())

    except FileNotFoundError:
        print("Не знайдено файл з історією")


def play_game():
    words = load_words()
    if not words:
        return

    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Шибениця")

    while attempts > 0:

        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"\nСлово: {display_word}")
        print(f"Вгадані літери: {guessed_letters}")
        print(f"Спроб лишилось: {attempts}")

        guess = input("Введіть літеру або слово: ").lower()

        if guess == secret_word:
            print("Ви перемогли")
            save_result(secret_word, "Перемога")
            return

        if len(guess) > 1:
            new_letters = False

            for letter in guess:
                if letter in secret_word and letter not in guessed_letters:
                    guessed_letters.append(letter)
                    new_letters = True

            if new_letters:
                print("Частково вгадано слово")
            else:
                attempts -= 1
                print("Невірне слово")

        else:
            if guess in guessed_letters:
                print("Така літера вже є")
                continue

            if guess in secret_word:
                guessed_letters.append(guess)
                print("Є така літера")
            else:
                attempts -= 1
                print("Невірна літера")

        if all(letter in guessed_letters for letter in secret_word):
            print("Ви перемогли")
            save_result(secret_word, "Перемога")
            return

    print(f"Ви програли, слово було: {secret_word}")
    save_result(secret_word, "Програш")



def add_word():
    word = input("Введіть слово яке буде додано: ").lower().strip()

    if not word.isalpha():
        print("Слово має містити тільки літери")
        return
    
    with open("words.txt", "a") as file:
        file.write(word + "\n")

    print("Слово додано")

def main():
    while True:
        print("\n1. Грати")
        print("2. Історія")
        print("3. Додати слово")
        print("4. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_history()
        elif choice =="3":
            add_word()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()
