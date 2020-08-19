
def greet(name):
    print("hello " + name + "!")

    greet2(name)
    print("getting ready to say bye...")
    bye()
    return


def greet2(name):
    print("how are you, " + name + "?")
    return


def bye():
    print("See you!")


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == "__main__":
    """
    By calling the function "greet", try to think about how the "calling stack" works in the memory.
    """
    greet("Allan")

    """
    Also try to think about how "calling stack works" during recursion!
    """
    result = factorial(6)
    print(result)
