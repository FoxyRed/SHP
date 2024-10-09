
# Function to plot a vector (currently prints ASCII art)
def plot_vector():
    ascii_art = """
    Time to rotate that sphere, so the print has a stable base                                                                               
                                    .                                          
                                    :   ^.                                     
                                        !:                  /|                 
                                        :               |=-|^.                
                                        :              !|!                     
                                        :             !                        
                                      ..~...         !                         
                                .......:::::^^^:.  !!                          
                              .............:^^^^^^^:                           
                            ...............^:::^^~~~~:                         
                          .......    .......^7~:^^~~~!~                        
                         ....            ....^!^^^^~^~!~                       
                        ....              ....:77~^^^~~!~                      
                        ....               ...:77~:^^^~~7.                     
                       .....               ...::::^^^^~~7^                     
                       .......            ...::::^^^^~~!7^                     
                       .........        ....::::^^^^^~~!7:                     
                        ^^:................::::^^^^^~~!!7                      
                   ......::.............::::::^^^^^~!77?^                      
             .^:..       .:::.......:::::::^^^^^^~~~!!7: ..                    
             .             :^:::::::::::^^^^^^^^~~~!7!.     ....      ^:       
                 .^         .^^^^^^^^^^^^^^^^~~~!!7~.          ::.    .        
                              .:^~~~~~~~~~~~!!!!~^.                            
                                  .::^^~~~~^^:.                                
                                                                               
                                                                               
    """
    print(ascii_art)


# Function to generate a random vector
def generate_vector(dimensions):
    return [randint(-29, 29) for _ in range(dimensions)]


# Function to calculate the dot product of two vectors
def calculate_dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


# Function to calculate and display partial dot products
def display_partial_dot_products(partial_vector, goal_vector):
    display_str = ""
    partial_products = [
        partial_vector[i] * goal_vector[i] for i in range(len(partial_vector))
    ]
    partial_sum = sum(partial_products)
    partial_products_str = [
        f"{partial_vector[i]}*{goal_vector[i]}" for i in range(len(partial_vector))
    ]
    partial_calc_str = " + ".join(partial_products_str)
    display_str = f"{partial_calc_str}"
    return display_str

def hide (vector):
    try:
        hidden_vector=''
        mod=randint(4,10)
        for index,letter in enumerate(str(vector)):
            if not(index % mod ==0 or letter in {',', ' ', ']', '['}):
                letter = '*'
            hidden_vector+=letter
        return hidden_vector
    except:
        print("Not a vector was given:\n",vector)
        return False
def vector_game(dimensions,difficulty,tolerance):
    difficulty = max(min(difficulty,dimensions-1),1)
    start_vector = generate_vector(dimensions)
    goal_vector = generate_vector(dimensions)

    for i in range(dimensions - difficulty):
        goal_vector[i] = start_vector[i]

    print("Start vector:", hide(start_vector)) #need to hide more!
    print("Goal vector:", hide(goal_vector))
    print("Type 'quit' to exit.")

    steps = 0
    while True:
        steps += 1
        while True:
            try:
                print(
                    f"Step {steps}: Provide {difficulty} coordinates to adjust (space-separated):"
                )
                inp=input()
                if inp.lower() == 'quit':
                    return False
                adjustments = list(map(int,inp.split()))
                while len(adjustments) < difficulty:
                    adjustments.append(0)
                break
            except:
                print("you did not enter a valid array")
        partial_vectors = []
        goal_vectors = []
        adjustment_index = 0

        for i in range(dimensions - 1, dimensions - difficulty - 1, -1):
            try:
                start_vector[i] += adjustments[-1 - adjustment_index]
            except IndexError:
                start_vector[i] += 0
            adjustment_index += 1
        for i in range(dimensions - 1, dimensions - difficulty - 1, -1):
            partial_vectors.append(start_vector[: i + 1])
            goal_vectors.append(goal_vector[: i + 1])

        display_str = display_partial_dot_products(partial_vectors[0], goal_vector)

        # Only show the last 3*steps characters
        lengte = len(display_str) - 3 * steps
        done = True
        for i in range(len(partial_vectors)):
            partial_calc_str = display_partial_dot_products(
                partial_vectors[i], goal_vectors[i]
            )
            if partial_calc_str[lengte:] != partial_calc_str:
                partial_calc_str = "..." + partial_calc_str[lengte:]
            if len(partial_calc_str) > 5:
                calc_str = partial_calc_str
            else:
                calc_str = "..."
            dot_product = calculate_dot_product(partial_vectors[i], goal_vectors[i])
            adtext = "within"
            if abs(dot_product) > tolerance:
                done = False
                adtext = f"{abs(dot_product)-tolerance} from"
            print(
                f"Result {i} is {adtext} the goal and equals to: {calc_str} = {dot_product}"
            )

        if done:
            print(f"Congratulations! You found the goal vector in {steps} steps.")
            return True

