import webbrowser
import sys
import os
import random

# Constants
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0


def ask_math_question():
    """Prompt the user to answer a math question."""
    global ERROR_COUNT
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1":  # Ensure input is treated as a string
                open_video()
                break
            elif user_input.lower() == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def open_video():
    """Open a YouTube video (Rickroll)."""
    webbrowser.open(YOUTUBE_URL)
    print("Rickroll incoming...")
    
    try:
        os.remove("fakefile.txt")  # This may fail if the file doesn't exist
    except FileNotFoundError:
        print("fakefile.txt not found. Skipping deletion.")


def process_nested_loops():
    """Process nested loops with structured error handling."""
    try:
        for i in range(100):
            for j in range(50):
                for k in range(10):
                    print(i, j, k)
                    if random.randint(0, 10) > 5:
                        raise Exception("Random error")
    except Exception as e:
        print(f"Error occurred: {e}")


class SimpleClass:
    """A class with basic attributes and a method that raises an error."""
    def __init__(self):
        self.number = 1
        self.text = "string"
        self.values = [1, 2, 3]
        self.dictionary = {"key": "value"}

    def print_values(self):
        try:
            print(self.number + int(self.text))  # This will cause an error
        except ValueError:
            print("Cannot add an integer and a string.")
        except Exception as e:
            print(f"Unexpected error: {e}")


def loop_with_exception():
    """Example function with controlled loop and exceptions."""
    for i in range(100):
        print(i)
        if i % 10 == 0:
            try:
                if i == 50:
                    raise IndexError("Fake IndexError")
            except IndexError as e:
                print(f"Handled exception: {e}")


if __name__ == "__main__":
    ask_math_question()