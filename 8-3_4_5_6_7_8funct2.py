#8-3,4 T-Shirt

def make_tshirt(size, text='I Love Python!'):
    print(f'Made a size "{size.upper()}" T-Shirt with {text} printed on it ')

make_tshirt('M',"I'm the BOSS")
make_tshirt(text="MEOW!",size="XL")
make_tshirt('XS')

#8-5 Cities

def desc_city(city, country="Croatia"):
    print(f'{city.title()} is in {country.title()}.')

desc_city('Reykjavik','icelanD')
desc_city('Zagreb')
desc_city('rijeka')

#8-6 City Names

def format_city_name(city,country):
    f_str = f'{city.title()}, {country.title()}'
    return f_str

print(format_city_name('zagreb','cRoatia'))

#8-7,8 Album / User Albums

def make_album(artist, album_title, songs=None):
    album = {'artist':artist.title(), 'album_title':album_title.title()}
    if songs: album['songs'] = songs
    return album

print(make_album('eminem', "music to be murdered by"))
print(make_album('billie eilish', 'ocean eyes', 5))

while True:
    print("\nIf you want to exit press 'Q'!\n")
    artist_name = input('Name of artist: >')
    if artist_name.lower() == 'q': break
    album_name = input('Name of album: >')
    songs = input('Number of songs \n(Press enter if you dont know): >')
    print(make_album(artist_name, album_name, songs))
