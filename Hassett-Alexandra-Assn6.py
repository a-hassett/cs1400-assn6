import random

verbs = ["Drop", "Kick", "Push", "Flick", "Pull", "Knock", "Flip", "Open", "Close", "Wiggle"]
adjectives = ["big", "long", "round", "tiny", "strong", "sturdy", "red", "hidden", "main", "secure"]
nouns = ["ball", "stick", "button", "knob", "lever", "latch", "switch", "hatch", "lid", "trigger"]

print("\n\nReach the Secret Prize Instructions\n")

for i in range(10):
    print(i + 1, end="")
    r = random.randint(0, 9)
    print(" -", verbs[r], "the", end=" ")
    r = random.randint(0, 9)
    print(adjectives[r], end=" ")
    r = random.randint(0, 9)
    print(nouns[r], ".")

print("\n\n")
