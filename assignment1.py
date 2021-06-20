"""
Replace the contents of this module docstring with your own details
Name: Kaung Khant Naing
Date started: 25/4/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-01-songs-app-kkn27
"""
from operator import itemgetter  # import itemgetter to sort the list

MENU = " MENU: \n L= List Songs \n A= Add new songs \n C= Complete the song \n Q= Quit"
choices = ["l", "a", "c", "q"]


def main():
    """..."""
    print("Songs to Learn 1.0 - by Kaung Khant Naing")
    taken_songs = read_file()
    print(len(taken_songs), "songs loaded")
    while True:
        print(MENU)  # prints out menu which is a constant from above
        menu_choice = input(">>>".lower())
        while menu_choice not in choices:
            print("Invalid Menu Choice.")
            menu_choice = input(">>> ".lower())
        if menu_choice == "l":
            listing_songs(taken_songs)
        elif menu_choice == "a":
            taken_songs.append(add_song())
            taken_songs.sort(key=itemgetter(1,0))
        elif menu_choice == "c":
            complete_songs(taken_songs,learn_all_songs(taken_songs))
        else:
            print(save_file(taken_songs), " saved to songs.csv")
            print("Have a Nice Day :)")
            exit()


def read_file():
    """ read the file and put songs into lists of lists """
    songs = []
    actual = []
    open_file = open("songs.csv", "r")
    for i in open_file:
        songs.append(i.strip("\n"))

    for j in songs:
        actual.append(j.split(','))  # the list that will be used through the program
    actual.sort(key=itemgetter(1, 0))  # sorting the list according to artist and title
    open_file.close()
    return actual


def listing_songs(taken_songs):
    """ function to display movies from the list and decide to put * or not """
    k = -1
    u_count = 0
    l_count = 0
    for m in taken_songs:
        k += 1
        if m[3] == "u":
            u_count += 1
            print(k, ".  * {:40} - {:<30} {:10} ({:<4})".format(m[0], m[1], " ", m[2]))
        else:
            l_count += 1
            print(k, ".    {:40} - {:<30} {:10} ({:<4})".format(m[0], m[1], " ", m[2]))
    print(l_count, "songs learned, ", u_count, "songs still to learn")


def add_song():
    new_song = []
    title = input("Title: ")
    while title == "": # error check so that user canoot input blanks
        print("This cannot be blank.")
        title = input("Title: ")
    new_song.append(title)

    artist = input("Artist: ")
    while artist == "":
        print("Input cannot be blank.")
        artist= input("Artist: ")
    new_song.append(artist)

    year= valid_int("Release Year: ") # calls valid_int function to error check integer input
    while year <=0:
        print ("Number must be >= 0")
        year= valid_int("Release Year: ")
    new_song.append(str(year))
    new_song.append('u')
    print(title, " by ", artist , "({})".format(year), "added to song list")
    return new_song


def valid_int(prompt):
    """to error check the integer input."""
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("PLease enter a valid integer.")


def learn_all_songs(taken_songs):
    """ this function check whether all songs are learned or not."""
    for song in taken_songs:
        if song[3] == "u":
            return False
    return True


def complete_songs(taken_songs,learn_all_songs):
    """ function to complete a song. """
    if learn_all_songs is True:
        print("No more songs to learn!")
    else:
        print ('Enter the number of a song to mark as learned')
        ask_number = valid_int(">>> ")
        while ask_number > len(taken_songs) -1 or ask_number < 0: # error checking user input
            print(" This does not exit. Choose Again.")
            ask_number = valid_int(">>> ")
        if taken_songs[ask_number][3] == "u":
            taken_songs[ask_number][3] = "l"  # changes the 'u' to 'l' to mark as learnt
            print(taken_songs[ask_number][0] + " by " + taken_songs[ask_number][1] + " learned.")
    return taken_songs


def save_file(taken_songs):
    """save the final list into the file"""
    final_count = 0
    open_file=open("songs.csv","w")
    for song in taken_songs:
        open_file.writelines(','.join(song) + "\n")
        final_count +=1
    open_file.close()
    return final_count


if __name__ == '__main__':
    main()
