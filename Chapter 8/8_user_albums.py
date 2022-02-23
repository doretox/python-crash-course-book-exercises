"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album's artist and title. Once you have that
information, call make_album() with the user's input and print the dictionary
that's created. Be sure to include a quit value in the while loop.
"""

def make_album(artist, album, tracks = 0):
    """Build a dictionary containing information about a music album."""
    album_dic = {
        'artist': artist.title(),
        'album': album.title(),
    }
    if tracks:
        album_dic['tracks'] = tracks
    return album_dic

# Prompts mesages
album_prompt = "\nType a music album title: "
artist_prompt = "Type the artist name: "

# Quit prompt
print("Type 'q' to quit.")

while True:
    album = input(album_prompt)
    if album == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    new_album = make_album(album, artist)
    print (new_album)
