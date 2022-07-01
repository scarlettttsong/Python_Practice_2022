"""
Week 3 Session 1 - Intro to Lists Pt 1
Goal: Create a program that manages song requests for a DJ.
The program should:
Print instructions at the beginning.
Continuously ask the user to enter a song title.
Exit the program if the user types “Quit.”
If the song title was previously requested, notify the user and share
the song position.
Otherwise, add the song to the request list, notify the user and share
the song position.
Challenge: Remove a song the user wants removed.
"""

print("Welcome to DJ Pythonic's Song Request Manager!")
print("🗳  Enter the song title to make a song request.")
print("✌️  To exit, enter Quit.")
print("- - - - - - - - - - - - - - - - - - - - - - - -")

song_list = []

while True:
    song_title = input("\nEnter a song title: ")
    if song_title == "Quit":
        print("Thank you for your requests. Enjoy the show!")
        break
    if song_title in song_list:
        print(f"The song {song_title} has been added to the list. \nIt is song"
              f" number {(song_list.index(song_title))+1} on the list!")
    else:
        song_list.append(song_title)
        print(f"✅ The song {song_title} has been added to the list. \n It is"
              f" song number {song_list.index(song_title)+1} on the list! ")




