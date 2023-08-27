def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """

    celsius = int(input('Enter a temperature in Celcius: '))

    fahrenheit = 1.8 * celsius + 32

    print (f'Fahrenheit: {fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
