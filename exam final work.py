import random

def load_words():
    try:
        with open("words.txt", "r") as file:
            words = file.read().split()
            return words
    
    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except:
        print("Помилка читання файлу")
        return []

    
def save_result(word, result):
    with open("history.txt", "a") as file:
        file.write(f"Слово: {word}, Результат: {result}\n")


def show_history():
    try:
        with open("history.txt", "r") as file:
            print("\nІсторія ігор:")
            print(file.read())

    except FileNotFoundError:
        print("Не знайдено файл з історією")
        return []

    except:
        print("Історія порожня")


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


        print(f"Слово: {display_word}")
        print(f"Вгадані літери: {guessed_letters}")
        print(f"Спроб лишилось: {attempts}")

        guess = input("Введіть літеру/слово: ").lower()


        if guess == secret_word:
            print("Ви перемогли")
            save_result(secret_word, "Перемога")
            return

        if len(guess) == 1:
            if guess in guessed_letters:
                print("Така літера вже є")
                continue

            guessed_letters.append(guess)

            if guess not in secret_word:
                attempts -= 1
                print("Невірна літера/слово")

        else:
            print("Невірна літера/слово")
            attempts -= 1


        if all(letter in guessed_letters for letter in secret_word):
            print("Ви перемогли")
            save_result(secret_word, "Перемога")
            return

    print(f"Ви програли, слово було: {secret_word}")
    save_result(secret_word, "Програш")


def main():
    while True:
        print("\n1. Грати")
        print("2. Історія")
        print("3. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    main()
