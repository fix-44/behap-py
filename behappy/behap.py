import random


def behappy():
    """
    Prints a random positive and uplifting sentence from a predefined list.

    This function selects a random sentence from a list of positive affirmations
    and prints it to encourage and uplift the reader. The sentences are designed
    to bring a smile and boost the mood of the recipient.

    Example:
        behappy()  # This will print a random happy sentence.
    """
    happy_sentences = [
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

    # Select and print a random sentence from the list
    print(random.choice(happy_sentences))

# Example usage
# behappy()
