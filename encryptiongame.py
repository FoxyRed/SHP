

def generate_decryption_table():
    # Create a list of uppercase alphabet letters
    alphabet = [chr(i) for i in range(65, 91)]

    # Initialize the decryption table
    table = []

    # Generate the table
    for i in range(26):
        row = [chr((i - j) % 26 + 65) for j in range(26)]
        table.append(row)

    return alphabet, table


def print_decryption_table():
    alphabet, table = generate_decryption_table()

    # Print the table header
    header = "    " + " ".join(alphabet)
    print(header)
    print("  " + "-" * len(header))

    # Print the table rows
    for i in range(26):
        row = f"{alphabet[i]} | " + " ".join(table[i])
        print(row)
    print("If you want to stop decryption, type 'quit'")

def decrypt_game(level,diff):
    sentences = [
        "Survival",
        "Prosperity",
        "Rights",
        "Responsibilities",
        "Governance structure",
        "Leaders",
        "Evaluator",
        "Faction Representatives",
        "Diplomaat",
        "Ontwikkelaar",
        "Vredesbewaker",
        "Citizens",
        "Voting",
        "Amendments",
        "Emergency Protocols",
        "Education",
        "Healthcare",
        "Environmental stewardship",
        "Cultural preservation",
        "Decision-making",
        "Citizens must contribute.",
        "Respect the leaders' authority.",
        "Every citizen has rights.",
        "Leaders have full autonomy.",
        "Vote for leadership changes.",
        "Establish healthcare services.",
        "Ensure sustainable growth.",
        "Preserve cultural heritage.",
        "Implement defense strategies.",
        "Foser diplomatic relations.",
        "Evaluate internal conflicts.",
        "Oversee development projects.",
        "Ensure environmental preservation.",
        "Support community wellbeing.",
        "Announce and organize votes.",
        "Adopt amendments democratically.",
        "Participate in decision-making.",
        "Judging citizens fairly.",
        "Follow communal decisions.",
        "Establish emergency protocols.",
        "The Evaluator is always a Koempel.",
        "An amendment is adopted if it receives a two-thirds majority vote.",
        "Each leader has full autonomy within their domain.",
        "Every citizen must respect the authority of the leaders.",
        "Mental health support must be established.",
        "Citizens are encouraged to participate.",
        "Education programs should include knowledge about diplomacy.",
        "Sustainable practices must be integrated.",
        "The colony must provide accessible healthcare services.",
        "This constitution is signed by the elected leader Oliver.",
        "Oversee all development projects.",
        "Develop and implement defense strategies.",
        "The final decision-maker in case of conflicts.",
        "Ensuring leaders act within their domains.",
        "The candidate with the most support will be appointed.",
        "Evaluate internal conflicts.",
        "Every citizen has the right to safety.",
        "The colony must respect cultural heritage.",
        "The Evaluator will announce and organize a vote.",
        "Standing behind a candidate.",
        "Foster cooperation, trade agreements, and alliances.",
        "Each faction has the option to select a Faction Representative.",
        "Every citizen must adhere to the principles of equality.",
        "Gather and analyze data.",
        "Ensure transparency and accessibility of information.",
        "Judging citizens who have not adhered to their responsibilities.",
        "Education and personal development opportunities.",
        "Every citizen has the right to healthcare.",
        "Acting as the final decision-maker in case of conflicts.",
        "Ensuring a future where all humans from the Melolonthe can thrive.",
    ]
    print_decryption_table()
    return run_challenge(sentences, diff)


def get_random_key():
    keys = [
        "NOA",
        "CAPTAIN KOEMPEL",
        "BB",
        "VREEMD",
        "HEALIAN",
        "KOFFIE",
        "BADULF",
        "HENK",
    ]
    return choice(keys)


def vigenere_cipher(text, key, mode="encrypt"):
    result = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        if mode == "encrypt":
            value = (text_as_int[i] + key_as_int[i % key_length] - 2 * 65) % 26
        elif mode == "decrypt":
            value = (text_as_int[i] - key_as_int[i % key_length] + 26) % 26
        result.append(chr(value + 65))  # Assuming uppercase letters only
    return "".join(result)


def get_sentence_by_difficulty(sentences, difficulty):
    # Sort sentences by length
    sorted_sentences = sorted(sentences, key=len)
    # Determine the range of sentences to select from based on difficulty
    total_sentences = len(sorted_sentences)
    range_size = total_sentences // 8  # Assuming 8 difficulty levels (0-7)
    start_index = difficulty * range_size
    end_index = start_index + range_size
    # Pick a random sentence from the specified range
    chosen_sentence = choice(sorted_sentences[start_index:end_index])
    return chosen_sentence


