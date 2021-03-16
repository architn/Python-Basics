# You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.


def speedingTicketFine(speed,  is_birthday):
    if is_birthday:
        if speed <= 65:
            print("No Ticket")
        elif (speed >= 66) and (speed <= 85):
            print("Small Ticket")
        else:
            print("Big Ticket")

    else:
        if speed <= 60:
            print("No Ticket")
        elif (speed >= 61) and (speed <= 80):
            print("Small Ticket")
        else:
            print("Big Ticket")


speedingTicketFine(81, True)
speedingTicketFine(81, False)
