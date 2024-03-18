def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 1
        print("Inner x:", x)

    inner_function()
    print("Outer x:", x)

outer_function()
