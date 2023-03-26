# This exercise covers lists: creating and modifying. NOTE: Loop will not be used in this exercise since I haven't gotten to that topic yet in this training.
# A quick summary of code will proceed each output to illustrate changes/updates. (Personal touch for this exercise! Not required!)

#Creating a Guest List:
Guests_List = ['Michael Jackson', 'Whitney Houston', 'Oprah Winfrey']
invite_msg = "you are cordinally invited to the once in a lifetime self-exploratory funfest night at the Garden of Eden."


# To print out the invite to each guest, call the index position of the guest on the lits. 
print('Invitation sent to guests:') 
print(f"{Guests_List[0]}, {invite_msg}")
print(f"{Guests_List[1]}, {invite_msg}")
print(f"{Guests_List[2]}, {invite_msg}\n")


# Identifying the guest who cannot attend the funfest:

print("Update from guest: ")  
print(f"{Guests_List[1]} cannot make the funfest as she does not want to be in the realm as {Guests_List[2]}. All other guests RSVP'd \n")


# Modifying guestslist to replace Whitney with Ellen DeGeneres:
Guests_List[1] = "Ellen DeGeneres"


# Words have spread about this funfest, I need a bigger table for the dinner/funfest. Some guests are demanding seating arrangement. 
# Updating list to insert new guests per the seating arrangement:
Guests_List.insert(0, 'Albert Einstein')
Guests_List.insert(2, 'Elon Musk')


# Last minute request to invite Former President Obama. He will have to seat whereever is available.
Guests_List.append('Barack Obama')


# To view the current seating arrangement/list
print("Updated guest list showing replacements and added guests:")
print(f'{Guests_List}\n')


# God damn! My bigger table is not available till 2024 and my house is flooded. I have to take only 2 persons to Eggspections.
# Message that will be sent out. 
# Remember to identify the index position in the Guestlist before printing:
sry_msg = 'my sincere apologies for the turn of events as I have been met with some devasting news. However, the show must go on. I can only invite 2 guests to attend my spectacular funfest. You will recieve an invite if you are one of said guests.'

print("Apology memo sent to guests:")
print(f"Dear {Guests_List[0]}, {sry_msg}\n") #repeat for all guests.


# when using the .pop() method, note that once a pop occurs, the list index position changes so you cannot use the same position from the original list. 
Guests_List.pop(0)
Guests_List.pop(0)
Guests_List.pop(0)
Guests_List.pop(2)
#Checking for remaining guest
print("Updated guest list for the 2 winners: ")
print(f'{Guests_List}\n')

# Sending out new invite to the 2 remaining guests:
new_msg = 'Congratulations, you are the chosen one. Come and face the ultimate funfest challenge. You cannot buy your way out of this one.'
print("Memo sent to 2 winners: ")
print(f'Dear {Guests_List[0]}, {new_msg}')
print(f'Dear {Guests_List[1]}, {new_msg}')

# This was a fun exercise


