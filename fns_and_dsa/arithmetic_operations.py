def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            print(num1 + num2)
        case "subtract":
            result = num1 - num2
            print(num1 - num2)
        case "multiply":
            result = num1 * num2
            print(num1 * num2)
        case "divide":
            result = num1 / num2
            if num2 == 0:
                print("Cannot be divide by 0")
            elif num2 != 0:
                print(num1 / num2)

    return result
