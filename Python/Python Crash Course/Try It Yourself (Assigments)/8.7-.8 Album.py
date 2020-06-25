
def make_album(artist_name, album_title, num_tracks =''):
    music_album = {'artist name': artist_name.title(),
               'album title': album_title.title(),
               'number of tracks': num_tracks,
               }
    return music_album

print(make_album('pillar', 'for the love of the game', '12'))

while True:
    print("\nPlease, enter your favorite band and album.")
    print("(Enter 'q' at any time to quit.)")

    art_name = input("Artist name: ")
    if art_name == 'q':
        break

    alb_name = input("Album name: ")
    if alb_name == 'q':
        break

band = make_album(art_name, alb_name)

print(band)