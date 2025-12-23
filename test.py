for i in range(1, 101):
    print(f"Current value: {i}")

    if i == 24:
        result = i / 0

    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")