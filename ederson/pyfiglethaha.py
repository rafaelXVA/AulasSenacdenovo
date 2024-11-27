import pyfiglet
from colorama import Fore,Style,init
init()
text="braganttino > flamengo"

ascii_art=pyfiglet.figlet_format(text, font='starwars')
print(Fore.LIGHTGREEN_EX+ascii_art)

list=['x','y','z','h','o']
list2=[Fore.BLUE,Fore.WHITE,Fore.GREEN,Fore.CYAN,Fore.LIGHTRED_EX]

for x in list2:
    print(x+'x')