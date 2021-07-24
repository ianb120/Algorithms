def card_checker(card_num):
    
    """
        Simple function that verifies a card number, using the Luhn
        algorithnm will return a True if the card is valid or False if not.
    """
    
    # transform int into a list
    card_list = [int(x) for x in str(card_num)]
    
    # grab the check sum digit
    checksum = card_list[-1]

    # reverse the order
    card_list.reverse()
    
    # empty list to store the transformed values
    total = []
    
    for num in range(1, len(card_list)):
        # odd numbers then multiply x 2
        if num % 2 == 1 and card_list[num] <= 4:
            total = total + [card_list[num] * 2]
        
        # odd numbers and greater than 5, minus 9 after multiplying
        elif num % 2 == 1 and card_list[num] >= 5:
            total = total + [card_list[num] * 2 - 9]
        
        # otherwise add the number to total
        else:
            total = total + [card_list[num]]
    
    # calculate total with the check sum
    total_sum = sum(total) + (checksum)
    
    # verify mod 10 == 0, then its a valid number
    if total_sum % 10 == 0:
        return True
    else:
        return False
    
card_numbers = {
    "card_one": card_checker(5266509258235496), # total = 60
    "card_two": card_checker(2720999985645912), # total = 84
    "card_three": card_checker(5266590258235496), # total = 60
    "card_four": card_checker(79927398713) # total = 70
}

for card_number in card_numbers:
    if card_numbers[card_number] == True:
        print(card_number, 'is a valid card number')
    else:
        print(card_number, 'is NOT a valid card number')
