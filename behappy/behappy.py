import random

class behappy:
    """
    A class to handle and display positive and uplifting messages.

    Attributes:
        messages (list): A list of positive and encouraging sentences.
    """

    def __init__(self):
        """
        Initializes the HappyMessages instance with a predefined list of positive sentences.
        """
        self.messages = [
            "You are amazing just the way you are!",
            "Today is a great day to accomplish something wonderful!",
            "Your smile lights up the room.",
            "Believe in yourself and all that you are.",
            "You bring so much joy to those around you.",
            "Every day is a new opportunity for happiness.",
            "You make the world a better place simply by being in it.",
            "Your positivity is contagious and inspiring.",
            "You have the power to make dreams come true.",
            "Remember, you are loved and appreciated.",
            "Life is full of beautiful moments waiting for you.",
            "Your kindness makes a huge difference.",
            "You are capable of achieving incredible things.",
            "Never forget how special you are.",
            "You bring so much light and warmth into the world.",
            "Celebrate every little victory—you deserve it!",
            "Your laughter is the best sound ever.",
            "You are a wonderful person with so much to offer.",
            "Thank you for being you—it's truly fantastic!",
            "Keep shining, because you’re doing amazing things."
        ]

    def make_me_happy(self):
        """
        Prints a random positive sentence from the list of messages.

        This method selects a random sentence from the instance's list of happy messages
        and prints it to encourage and uplift the reader.
        """
        print(random.choice(self.messages))

# Example usage:
# Create an instance of behappys
#happy = behappys()
# Print a random happy message
#happy.make_me_happy()