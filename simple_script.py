if __name__ == "__main__":
    # Print a welcome message
    print("Welcome to the U of A Applied Math programming workshop!")

    # Perform some basic arithmetic
    number1 = 5
    number2 = 3
    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2

    print(f"The sum of {number1} and {number2} is: {sum_result}")
    print(f"The difference between {number1} and {number2} is: {difference}")
    print(f"The product of {number1} and {number2} is: {product}")
    print(f"The quotient of {number1} divided by {number2} is: {quotient}")

    # Use a loop to print numbers 1 through 5
    print("Let's count to 5:")
    for i in range(1, 6):
        print(i)
