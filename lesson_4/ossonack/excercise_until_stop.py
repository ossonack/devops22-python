while(True):
    text = input("Enter text, enter 'stop' to quit: ")
    if text == "stop":
        break
    print(f"{text} has length {len(text)}")