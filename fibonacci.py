def fibonacci(upper_limit):
    fib = [0, 1]
    if upper_limit == 0:
        return 0
    if upper_limit == 1:
        return 1
    else:
        i = 1
        while fib[i] < upper_limit:
            next_fib = fib[i-1] + fib[i]
            if next_fib < upper_limit:
                fib.append(next_fib)
                i += 1
            else:
                return fib
go_again_letter = "Y"
while go_again_letter != "N":
    user_input = int(input("What is the upper limit? "))
    print(fibonacci(user_input))
    go_again_letter = input("Want to go again? Y for yes and N for no: ")
    possible_options = ["Y", "N"]
    while go_again_letter not in possible_options:
        go_again_letter = input("Give me a Y or N: ")

