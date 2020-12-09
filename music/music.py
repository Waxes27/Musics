from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import json

def clear():
    os.system('clear')


def load_json():
    try:
        with open(f"{os.environ['HOME']}/.Music/music/music.json", 'r') as file_:
            open_json = json.load(file_)
    except json.decoder.JSONDecodeError:
        with open(f"{os.environ['HOME']}/.Music/music/music.json", 'w') as temp:
            songs = json.dumps(songs, indent =2)
            temp.write(f"{songs}\n")
    try:
        return open_json
    except NameError:
        with open(f"{os.environ['HOME']}/.Music/music/music.json", 'r') as file_:
            return json.load(file_)



def json_init():
    global open_json
    songs = {
    '1' : ['. A Tale of 2 Citiez - J-cole','https://www.youtube.com/watch?v=PB7gyS1TsYo&list=OLAK5uy_mvsSsaJ7aXJKopbPykpDdG9h0xotLliJE&index=5'],
    '2' : ['. New Light - Justice Der','https://www.youtube.com/watch?v=gl3fQ3MiJS8'],
    '3' : ['. Yonkers - Tyler the Creator','https://www.youtube.com/watch?v=XSbZidsgMfw'],
    '4' : ['. Nymano - beauty','https://www.youtube.com/watch?v=PRZs9LXLy6s'],
    '5' : ['. Juan Rios - Cascada','https://www.youtube.com/watch?v=5ccgR3fyf2g'],
    '6' : ['. Kevin Momo - Lately (feat. Blissful Sax)','https://www.youtube.com/watch?v=sutroWBOis0'],
    '7' : ['. Blue Wednesday - Introvert','https://www.youtube.com/watch?v=GeMRuft1S8Q']

}
    try:
        with open(f"{os.environ['HOME']}/.Music/music/music.json", 'r') as file_:
            open_json = json.load(file_)
    except json.decoder.JSONDecodeError:
        with open(f"{os.environ['HOME']}/.Music/music/music.json", 'w') as temp:
            songs = json.dumps(songs, indent =2)
            temp.write(f"{songs}\n")
    try:
        return open_json
    except NameError:
        with open(f"{os.environ['HOME']}/.Music/music/music.json", 'r') as file_:
            return json.load(file_)



def user_in():
    songs = json_init()

    for i in open_json:
        pass
    header = int(i)+1
    # print(header)

    name = input('\n Song name (Artist - song(feat. Artist) > ')
    link = input('\n Enter Youtube link of song > ')

    body = f'. {name}'
    
    songs.update({header : [body, link]})

    with open(f"{os.environ['HOME']}/.Music/music/music.json", 'w') as temp:
            songs = json.dumps(songs, indent =2)
            temp.write(f"{songs}\n")

    return songs


def song_picker(songs):
    os.system('clear')
    print("Pick your song of the day...\n\n")
    for k,v in songs.items():
        print(f"{k}{v[0]}")

    song_name = input('\nPick a number: \n')
    return song_name


def activation(songs):
    PATH = f"{os.environ['HOME']}/Web_Crawler/.chromedriver"
    song_name = song_picker(songs)
    
    clear()
    driver = webdriver.Chrome(PATH)
    clear()

    driver.get(songs[song_name][1])
    time.sleep(3)
    play = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button')

    play.click()
    driver.minimize_window()
    # clear()
    input('Next? (ENTER or CTRL + c)')
    driver.close()
    


def main():
    json_init()
    # user_in()
    # return
    ver = int(input('1 - adding a song\n\n2 - playing previously saved song\n\n > '))
    while ver == 1:
        user_in()
        ver = int(input('1 - adding a song\n\n2 - playing previously saved song\n\n > '))
    if ver != 1:
        songs = load_json()

    
    activation(songs)

while True:
    main()