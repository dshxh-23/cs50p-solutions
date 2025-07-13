grt = input("Greeting: ").casefold().strip()


if(grt[:5] == 'hello'):
    print("$0")

elif(grt[0] == "h"):
    print("$20")

else:
    print("$100")
