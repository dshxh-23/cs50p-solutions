def main():
    time = input("What's the current time? ")
    time = convert(time)

    if(7 <= time <= 8):
        print("breakfast time")

    if(12 <= time <= 13):
        print("lunch time")

    if(18 <= time <= 19):
        print("dinner time")


def convert(time):
    hours, mins = time.split(":")
    return (float(hours) + (float(mins)/60))

if __name__ == "__main__":
    main()
