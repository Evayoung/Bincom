import random
import psycopg2

# ======================================================================================================================
#           PRELIMINARY ONLINE INTERVIEW TEST FOR PYTHON
# ======================================================================================================================
color_list = {"GREEN": 1, "YELLOW": 2, "BLUE": 3, "BROWN": 4, "PINK": 5, "ORANGE": 6, "CREAM": 7, "RED": 8, "WHITE": 9, "BLACK": 10, "ARSH": 11}
monday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
tuesday = ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]
wednesday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]
thursday = ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
friday = ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]


# ===================================================================================================================
#       Question 1: Which color of shirt is the mean color?
# ===================================================================================================================
def mean_color():
    """
    Step 1: we'll assign numerical values to each color as in 'color_list' above and calculate the average.

    step 2: For each day, calculate the sum of color values and divide by the total number of colors (19).

    step 3: To get a single mean color for the week, calculate the average of the daily mean colors and round to the
    nearest whole number

    """
    weekdays = [monday, tuesday, wednesday, thursday, friday]

    total_list = []
    for j in weekdays:
        new_data = []
        for i in j:
            new_data.append(color_list[f"{i}"])

        total_list.append(round(sum(new_data)/len(new_data), 2))
        new_data.clear()

    mean = int(round(sum(total_list)/len(total_list), 0))
    for color, count in color_list.items():
        if mean == count:
            print(f'Mean color of shirt is {color}')
            break
# ===================================================================================================================
#       Question 2:  Which color is mostly worn throughout the week?
# ===================================================================================================================
def most_worn_color():
    all_day = monday + tuesday + wednesday + thursday + friday
    color_summary = {}
    for color, counts in color_list.items():
        color_summary[color] = 0
        for i in all_day:
            if color == i:
                color_summary[color] += 1


    highest = max(color_summary.values())
    for color, count in color_summary.items():
        if highest == count:
            print(f'The most worn color is {color} with {highest} appearances')
            break
# ===================================================================================================================
#       Question 3: Which color is the median?
# ===================================================================================================================
def median_color():
    all_day = monday + tuesday + wednesday + thursday + friday
    color_summary = {}
    for color, counts in color_list.items():
        color_summary[color] = 0
        for i in all_day:
            if color == i:
                color_summary[color] += 1

    # sort the dictionary's key and value accordingly
    sort_data = sorted(color_summary.items(), key=lambda x: x[1])

    n = len(sort_data)
    if n % 2 == 1:
        median_index = n // 2
        median_colour = sort_data[median_index][0]
    else:
        median_index1 = n // 2 - 1
        median_index2 = n // 2
        median_color1 = sort_data[median_index1][0]
        median_color2 = sort_data[median_index2][0]
        median_colour = f'{median_color1} and {median_color2}'

    print(f'The median color is {median_colour}')

# ===================================================================================================================
#       Question 4: BONUS Get the variance of the colors?
# ===================================================================================================================
def variance_color():
    all_day = monday + tuesday + wednesday + thursday + friday
    color_summary = {}
    for color, counts in color_list.items():
        color_summary[color] = 0
        for i in all_day:
            if color == i:
                color_summary[color] += 1

    # Calculate the mean
    total_count = sum(color_summary.values())
    mean_count = total_count / len(color_summary)

    # Calculate the variance
    variance = round(sum((count - mean_count) ** 2 for count in color_summary.values()) / len(color_summary), 2)

    print(f'The variance of the colors is {variance}')

# ===================================================================================================================
#       Question 5: if a colour is chosen at random, what is the probability that the color is red?
# ===================================================================================================================
def color_probability(color):
    color_lists = monday + tuesday + wednesday + thursday + friday

    color_appearance = color_lists.count(color)

    probability = round(color_appearance / len(color_lists), 2)
    probability_percent = probability * 100

    print(f'The probability of choosing {color} is {probability} with {probability_percent}%')


# ===================================================================================================================
#       Question 6: Save the colours and their frequencies in postgresql database
# ===================================================================================================================
def use_postgres():
    try:
        conn = psycopg2.connect(database="interview", user="postgres", host='localhost', password="Evayoung@30", port=5432)

        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Execute a command:
        cur.execute("""CREATE TABLE IF NOT EXISTS colors(
                            color_id SERIAL PRIMARY KEY,
                            color_name VARCHAR(10) UNIQUE NOT NULL,
                            color_frequency VARCHAR(10) NOT NULL
                        );
                    """)


        data = proces_data()
        for color, count in data.items():
            cur.execute(
                "INSERT INTO colors(color_name, color_frequency) VALUES(%s, %s)",(color, count))
        # Make the changes to the database persistent
        conn.commit()
        # Close cursor and communication with the database
        cur.close()
        conn.close()
        print("Data Submitted!")
    except Exception as e:
        print(f"An error occurred: {e}")

def proces_data():
    all_day = monday + tuesday + wednesday + thursday + friday
    color_summary = {}
    for color, counts in color_list.items():
        color_summary[color] = 0
        for i in all_day:
            if color == i:
                color_summary[color] += 1

    return color_summary

# ===================================================================================================================
#       Question 7: write a recursive searching algorithm to search for a number entered by user in a list of numbers.
# ===================================================================================================================
def recursive_search(lst, target, index=0):
    # Base case: if the index is beyond the list length, return -1 (not found)
    if index >= len(lst):
        return -1
    # If the target is found, return the index
    if lst[index] == target:
        return index
    # Recur with the next index
    return recursive_search(lst, target, index + 1)

# ===================================================================================================================
#       Question 8: Write a program that generates random 4 digits number of 0s and 1s and convert the generated number
#       to base 10.
# ===================================================================================================================
def random_number_to_decimal():
    # Generate 4-digit binary number
    binary_number = [str(random.randint(0, 1)) for _ in range(4)]
    binary_string = ''.join(binary_number)
    print(f"Binary Number: {binary_string}")

    # Convert binary to decimal
    decimal_number = int(binary_string, 2)
    print(f"Decimal Equivalent: {decimal_number}")

# ===================================================================================================================
#       Question 9: Write a program to sum the first 50 fibonacci sequence.
# ===================================================================================================================
def fibonacci_sum(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    total_sum = 0

    # Generate and sum Fibonacci numbers up to n
    for _ in range(n):
        total_sum += a
        a, b = b, a + b

    return total_sum

# ===================================================================================================================
#                           Application entry point
# ===================================================================================================================
while True:
    print()
    print()
    print("""
        ******* Preliminary Online Interview Test for Python *********
        ===============================================================
        
        Question 1: Which color of shirt is the mean color?
        Question 2:  Which color is mostly worn throughout the week?
        Question 3: Which color is the median?
        Question 4: BONUS Get the variance of the colors?
        Question 5: if a colour is chosen at random, what is the probability that the color is red?
        Question 6: Save the colours and their frequencies in postgresql database
        Question 7: write a recursive searching algorithm to search for a number entered by user in a list of numbers.
        Question 8: Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
        Question 9: Write a program to sum the first 50 fibonacci sequence.
        
        Enter 0 to quit
    """)

    answer = int(input("\tPlease enter 1 to 9 to get the answers: "))
    if answer == 0:
        print("\n\n\t\t\tThank you for checking, Goodbye!")
        break
    elif answer > 9:
        input(" Option not in list, press enter to continue...")
        # os.system("cls")
    elif answer == 1:
        mean_color()

    elif answer == 2:
        most_worn_color()

    elif answer == 3:
        median_color()

    elif answer == 4:
        variance_color()

    elif answer == 5:
        color = input(" Enter Color name: ").upper()
        color_probability(color)

    elif answer == 6:
        use_postgres()

    elif answer == 7:
        # Get user input
        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        target_number = int(input("Enter the number you want to search for: "))

        # Perform the search
        result = recursive_search(numbers, target_number)

        # Print result
        if result != -1:
            print(f"Number found at index {result}")
        else:
            print("Number not found in the list")

    elif answer == 8:
        random_number_to_decimal()

    elif answer == 9:
        # Sum the first 50 Fibonacci numbers
        result = fibonacci_sum(50)

        # Output the result
        print(f"The sum of the first 50 Fibonacci numbers is: {result}")

