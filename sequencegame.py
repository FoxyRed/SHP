from oeis import (
    A000004,
    A000005,
    A000010,
    A000032,
    A000037,
    A000040,
    A000041,
    A000045,
    A000079,
    A000108,
    A000110,
    A000119,
    A000120,
    A000121,
    A000142,
    A000203,
    A000217,
    A000290,
    A000326,
    A001220,
    A001221,
    A001223,
    A001246,
    A001247,
    A001462,
    A001622,
    A001969,
    A002182,
    A002275,
    A004086,
    A004767,
    A006577,
    A007089,
    A007947,
    A007953,
    A008587,
    A008588,
    A008589,
    A008592,
    A023811,
    A064367,
    A070939,
    A115020,
    A133058,
    A133613,
    A181391,
    A183613,
    A265326,
)

# List of available sequences
oeis_sequences = [
    A000004,
    A000005,
    A000010,
    A000032,
    A000037,
    A000040,
    A000041,
    A000045,
    A000079,
    A000108,
    A000110,
    A000119,
    A000120,
    A000121,
    A000142,
    A000203,
    A000217,
    A000290,
    A000326,
    A001220,
    A001221,
    A001223,
    A001246,
    A001247,
    A001462,
    A001622,
    A001969,
    A002182,
    A002275,
    A004086,
    A004767,
    A006577,
    A007089,
    A007947,
    A007953,
    A008587,
    A008588,
    A008589,
    A008592,
    A023811,
    A064367,
    A070939,
    A115020,
    A133058,
    A133613,
    A181391,
    A183613,
    A265326,
]


# Function to get a random OEIS sequence
def get_random_oeis_sequence(n):
    sequence_module = choice(oeis_sequences)
    try:
        sequence = sequence_module[: n + 10]
    except Exception as e:
        sequence = []
    return sequence


# Function to ask for user's prediction
def ask_for_prediction(sequence, visible, goal):
    #five is hard coded here, if changed add extra sequence
    attempts = 5
    base = choice([0, 0,0, 1, 1, 2, 3, 4])
    for attempt in range(attempts):
        print(f"Attempt {attempt + 1} of {attempts}")
        print("Given sequence:", sequence[base : base + visible-attempts+attempt])
        correct = True
        for i in range(goal):
            try:
                user_input = int(input(f"Enter the next number (#{i + 1} of {goal}): "))
            except ValueError:
                print("Invalid input, please enter an integer.")
                correct = False
                break

            if user_input == sequence[base + visible -attempts+attempt+ i]:
                print("Correct!")
            else:
                print("Incorrect, try again.")
                correct = False
                break

        if correct:
            print("You completed the sequence correctly!")
            return 5-attempt
    print("Out of attempts. Restarting sequence.")
    return 0


# Main function for sequence prediction game
def sequence_prediction_game(goal,replay):
    visible = 10
    success =0
    print(f"We need to correct {replay} positions")
    while True:
        sequence = []
        while len(sequence) < visible + goal+5:
            sequence = get_random_oeis_sequence(visible + goal+5)

        success += ask_for_prediction(sequence, visible, goal)
        if success>replay:
            return True
        else:
            print(f"Only {success} of the {replay} positions adjusted. Need more sequences...")
