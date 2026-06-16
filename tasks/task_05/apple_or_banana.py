def classify_fruit(shape, color):
    if shape == "round" and (color == "red" or color == "green"):
        return "apple"
    elif shape == "arc" and color == "yellow":
        return "banana"
    else:
        return "unknown fruit"


def main():
    print("Task 5.2: Apple or Banana?")

    shape = input("Enter the fruit shape: ")
    color = input("Enter the fruit color: ")

    fruit = classify_fruit(shape, color)

    print("The fruit is:", fruit)


if __name__ == "__main__":
    main()
