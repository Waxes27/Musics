import os
import subprocess
import time

zsh = open(f"{os.environ['HOME']}/.zshrc", 'a+')
bashrc = open(f"{os.environ['HOME']}/.bashrc", 'a+')
bashrc1 = open(f"{os.environ['HOME']}/.bashrc", 'r')

print('Starting... Do not interrupt process')
value = subprocess.getoutput("""
pip install selenium
rm -rf ~/.Music
mkdir ~/.Music
git clone https://github.com/Waxes27/Musics.git ~/.Music
"""
)

    
if "alias music" not in bashrc1.read():
    bashrc.write("\nalias music='python3 ~/.Music/music/music.py'\n")
    zsh.write("\nalias music='python3 ~/.Music/music/music.py'\n")


# os.system("""mkdir ~/.config/.clinic

# cp ~/.WTC-GROUP-PROJECT/main/code/codebase/credentials.json ~/.config/.clinic
# cp -r ~/.WTC-GROUP-PROJECT/main/.tokens/ ~/.config/.clinic
# rm -rf ~/.config/.clinic/.tokens/t
# """)



print('SETUP COMPLETE')
