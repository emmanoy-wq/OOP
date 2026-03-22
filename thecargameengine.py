while True:
    command = input("pass your command:").lower()
    if command == "start":
        print("car started...")
    elif command == "stop":
        print("car stopped ...")
    elif command == "acelerate":
        print("car at 100 miles an hour")
    elif command == "drift":
        print("car drifting")
    elif command == "quit":
        break
    else:
        print("i dont understand the command")
