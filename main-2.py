def main():
    number = int(input('Enter your input: '))

    result = number % 2 == 1
    

    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
