import os
import platform
from time import sleep


#===========================================================================================
#========================================Functions==========================================
#===========================================================================================

def darren_purchase(item):
  global player, darren_stock
  
  player['inventory'].append(item)
  player['money'] -= darren_shop[item]
  darren_stock[f'{item}_stock'] -= 1

def clear():
  if platform.system() == "Linux":
    os.system("clear")
  elif platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")
  
def pause():
  input('Press Enter to continue...')

def darren_gone_caps(text):
  if darren_discount == 0.0:
    print("*darren shouts from the food hall*")
    print(text.upper())
  else:
    print(text)


#===========================================================================================
#=======================================ASCII Storage=======================================
#===========================================================================================

door_art = [
""" ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+-+-| | |
| | |_|_|_|_| | |
| |     ___   | |
| |    /__/   | |
| |   [%==] ()| |
| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|""",

""" ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |
| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|""",


""" ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|"""]


#===========================================================================================
#=======================================Dodgy Darren========================================
#===========================================================================================

dd = """
⣿⣿⣿⡿⠿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⠈⠹⢿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠈⠉⠉⠙⠻⢿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠛⠄⠄⠘⢻⣿⣿⣿
⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⡁⣤⠄⠐⠒⠒⠄⠄⣤⠄⠄⢸⣿⣿⣿
⣿⠟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠘⠛⠛⣿
⣿⠄⢸⣿⣿⣿⣿⡿⠉⠉⠹⠟⠉⠉⠉⠹⣿⣿⣿⣿⣿⣿⠏⠄⠄⢰⣶⣿
⣿⠄⠄⢻⠟⠁⢠⠃⢀⣤⣤⣤⣤⣤⣤⣾⣿⡟⢻⣿⣿⠛⠄⠄⢠⣾⣿⣿
⣿⣄⡀⢸⣇⣼⠉⠄⠙⠋⠉⠻⠿⣿⣛⠛⠛⢿⣧⣿⡿⠄⠄⠄⢸⣿⣿⣿
⣿⣿⡇⠘⢿⣿⣦⠄⠄⠄⢀⣀⣀⡈⠉⠄⣠⣾⣿⡿⠁⠄⢀⣶⣾⣿⣿⣿
⣿⣿⣷⡄⠈⠹⣿⣶⣶⣤⣌⣭⣿⣿⣶⣾⣿⣿⠏⠄⠄⠄⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣷⡄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠄⠄⠄⣤⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣆⠄⠙⢿⣿⣿⣿⣿⣿⣿⡿⠃⠄⠄⠄⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⠄⠈⠉⠉⠉⠉⠉⠉⠁⠄⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣤⡄⠄⠄⠄⠄⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

#===========================================================================================
#=======================================Dictionaries========================================
#===========================================================================================

darren_shop = {
  "pint": 5.0,
  "sunlun_shirt": 500.0,
  "hairpin_darren": 10.0,
  "cheesy_chips": 20.0,
}

darren_stock = {
  "pint_stock": 3,
  "sunlun_shirt_stock": 1,
  "hairpin_darren_stock": 1,
  "cheesy_chips_stock": 2
}
darren_discount = 1.0

player = {
  'health': 100, 
  'money': 1000000000000, 
  'location': 'cell', 
  'inventory': ['hairpin_vikki'], 
  'supports': ".",
  'outfit':"noob",
  'hasVisitedDarren':False
}

vikki_stats = {
  'alive' : True
}

# possible locations
# hallway
# solitary confinment
# warden's office
# darren's coridoor
# food hall
# cell


#===========================================================================================
#=======================================Exposition==========================================
#===========================================================================================


print("""
You have to get out.
You look around. You see a toilet, a bed and a cell door.
A man screams in the next room.
""")
pause()


#===========================================================================================
#========================================The Cell===========================================
#===========================================================================================


while player['health'] > 0:

  while player['location'] == 'cell':
    clear()
    print('You are in a cell.')
    moves = ['1', '2', '3']

    move = input("""
What would you like to do?
  1. Check the bed.
  2. Visit the lavatory.
  3. Leave the cell.
""")

    while move not in moves:
      move = input('Invalid input. Try again.\n')

    if move == '1':
      clear()
      if 'hairpin_bed' in player['inventory']:
        print('\nYou find nothing but crumpled sheets.')
        pause()
      else:
        print('\nYou move the sheets the around and find a hairpin.\n')
        player['inventory'].append('hairpin_bed')
        pause()
    elif move == '2':
      clear()
      print('.')
      sleep(1)
      clear()
      print('..')
      sleep(1)
      clear()
      print('...')
      sleep(1)
      clear()
      print('Business accomplished.')
      pause()
    elif move == '3':
      player['location'] = 'hallway'

  while player['location'] == 'hallway':
    
    clear()
    print("""
You are in a hallway.
There is a light flickering, something seems dodgy.
You can smell the wardens door, it contains a yellow stain.
There is a door where you can smell the faintest scent of grease.
""")

    moves = ['1', '2', '3', '4']

    move = input("""
What would you like to do?
  1. Go to the dodgy coridoor.
  2. Go to the food hall.
  3. Try the wardens door.
  4. Go back to your cell.
""")

    while move not in moves:
      move = input('Invalid input. Try again.\n')

    if move == '1':
      player['location'] = 'coridoor'
    elif move == '2':
      player['location'] = 'food hall'
    elif move == '3':
      clear()
      print('Door is locked.\nDo you want to try and lockpick it?')
      option = input('yes or no?: ').lower()
      if option == 'yes':
        if 'hairpin_bed' in player['inventory'] and 'hairpin_darren' in player[
            'inventory'] and 'hairpin_vikki' in player['inventory']:
          clear()
          print(door_art[0])
          sleep(1)
          clear()
          print(door_art[1])
          sleep(1)
          clear()
          print(door_art[2])
          sleep(1)
          player['location'] = 'wardens office'
          
        else:
          clear()
          print("You haven't got all 3 of the hairpins to make a lockpick.")
          pause()
      elif option == 'no':
        clear()
        print(
            'You stand there for awhile and you decide to go back to the hallway.'
        )
        pause()
    elif move == '4':
      player['location'] = 'cell'


#===========================================================================================
#==================================Dodgy Corridor==========================================
#===========================================================================================


  while player['location'] == 'coridoor':
    player['hasVisitedDarren'] = True
    clear()
    if player['supports'] == ".":
      print("""
The stained walls echo cries of terror. 
Walking further toward the light, a faint sour odour overtakes your senses.
Shadows behind you crawl upon the walls.
The dim light flickers on, the shadow that once grew upon his face is now clear as day.
""")
      pause()
      clear()
      print(dd)
      sleep(2.5)
      print('''
"ya alreet sonna
me names darren, bu thats dodgy darren to yew
a love footy, cheesy chips, and sunlun"
''')
      
      cheesy_chips = False
      player['supports']=input('"who dyew support met": ')
      if player['supports'] == 'newcastle':
        player['health'] = 1
        clear()
        print(dd)
        print("""
*he takes a swing at you*
"you support sunlun now"
""")
      elif player['supports'] == 'sunderland' or player['supports'] == 'sunlun':
        clear()
        print(dd)
        print('"ah love sunlun me, you get a cheeky discount hard lad"')
        darren_discount = 0.8
      elif player['supports'] == 'cheesy chips':
        clear()
        print(dd)
        print("""
"WHERE"  *darren runs to the food hall*
You've never seen a Sunderland supporter run so quick.
""")
        darren_discount = 0.0
      else:
        clear()
        print(dd)
        print('"WHO THAT"')
      if darren_discount != 0:
        print('\n"anyway, what you wanna buy, owt or nowt"\n')
      pause()
      for item in darren_shop:
        darren_shop[item] *= darren_discount
        darren_shop[item] = round(darren_shop[item])
        
    clear()


#===========================================================================================
#=========================================The Shop==========================================
#===========================================================================================

    #dispely shop
    print(f"""        
Dodgy Darren's Shop
You have £{player['money']}.
  1. Pint (Cost: £{darren_shop["pint"]}) (Stock: {darren_stock['pint_stock']})
  2. Sunderland Shirt (Cost: £{darren_shop['sunlun_shirt']}) (Stock: {darren_stock['sunlun_shirt_stock']})
  3. Hairpin (Cost: £{darren_shop["hairpin_darren"]}) (Stock: {darren_stock['hairpin_darren_stock']})
  4. Cheesy Chips (Cost: £{darren_shop["cheesy_chips"]}) (Stock: {darren_stock['cheesy_chips_stock']})
  5. Leave the dodgy corridor
""")


    #tesitntingingint
    # print(player['inventory'])


    
    moves = ['1','2','3','4','5']
    move = input()
    while move not in moves:
      move = input('Invalid input. Try again.\n')

    #buy pint
    if move == '1':
      if darren_stock['pint_stock'] != 0:
        if player['money'] >= darren_shop['pint']:
          darren_purchase('pint')
          darren_gone_caps('"fresh out the oven tha"')
          pause()
        else:
          darren_gone_caps('"its not even on draught man"')
          print('''
*he throws the pint at you*
It smells like urine...''')
                          
          pause()

    #buy pristine football garment
    elif move == '2':
      if darren_stock['sunlun_shirt_stock'] != 0:
        if player['money'] >= darren_shop['sunlun_shirt']:
          darren_purchase('sunlun_shirt')
          if darren_discount == 0.0:
            print('''
*darren shouts from the food hall*
"WARRA STEEL! A LOVE STEEL! LOOKA WHO SINGED THA!"
Upon inspection, it looks like Alan Shearer's signature.
''')
            pause()
          else:
            print('''
"warra steel. a love steel. looka who singed tha"
Upon inspection, it looks like Alan Shearer's signature.
''')
            pause()
        else:
          darren_gone_caps('''"shame you'll never get to see who signed this
a divint nar mesel. cannit reed lad"
''')
          pause()

    #buy hairpin darren
    elif move == '3':
      if darren_stock['hairpin_darren_stock'] != 0:
        if player['money'] >= darren_shop['hairpin_darren']:
          darren_purchase('hairpin_darren')
          darren_gone_caps('''
"best peece of coppa wire tha like"
''')
          pause()
        else:
          print('''
"stole this last week still havent found nay one to buy it like"''')
          pause()
          

    # buy chheeesysy chips
    elif move == '4':
      if darren_stock['cheesy_chips_stock'] != 0:
        if player['money'] >= darren_shop['cheesy_chips']:
          darren_purchase('cheesy_chips')
          darren_gone_caps('''
leeve some for me lyke
  ''')
          pause()
        else:
          darren_gone_caps('''
You divnt like cheesy chips whats wrong with ya''')
          pause()
    elif move == '5':
      player['location'] = 'hallway'



  while player["location"] == "food hall":
    clear()
    print('''
Upon stepping into the food hall, you're blinded by the lights.
The once plain white walls, now stained by the slop of the kitchen.
In the corner of the room you recognise one of the dinner ladies as Vikki, your ex-wife...
The food line is short and they're serving your favourite today... Slop!
Also, to your left there's another prisoner sitting staring at you.
''')
  
  
    moves = ['1', '2', '3', '4']
  
    move = input("""
What would you like to do?
  1. Move to Vikki.
  2. Go to food queue.
  3. Go sit down.
  4. Go back to the hallway.
""")
  
    while move not in moves:
      move = input('Invalid input. Try again.\n')

    if move == '1':    #remove pass and add actions
      clear()
      option = input('''*You walk up to Vikki and she looks at you with a smirk*
      "Hey daniel, how's it going?"
      1. "Good, how about you?"
      2. *Grab her and throw her*
      3. *Walk away*
      ''')
      aa = ['1', '2', '3']
      while option not in aa:
        option = input('Invalid input. Try again.\n')
      if option == '1': 
        print('top text')
        print('bottom text')#have nice convo with vikki
      elif option == '2':
        pass
        
      
    elif move == '2':
      vikki_stats['alive'] = False
      print("*You grab her by the arm and start swinging her round in the air\n Letting go, you send her thundering into the brick wall of the food hall leaving a Vikki-shaped hole as she slowly peels off of the glossy tiles.\nVikki is dead, theres nothing you can do to save her.")

    
    elif move == '3':
      pass
    else:
      player['location'] = 'hallway'


#===========================================================================================
#====================================Warden's Office========================================
#===========================================================================================

  
  while player['location'] == 'wardens office':
    clear()
    print("""You hear the lock click, the door swings open.
You look around. You see a falling apart desk with two drawers,
a wardrobe and a set of keys hanging on the wall.""")
    
    move = input("""
  What would you like to do?
    1. Check the drawers.
    2. Visit the lavatory (on the desk).
    3. Check the wardrobe.
    4. Grab the keys.
    5. Leave the office
    """)
  
    clear()
    if move == '1':#check draws
      if player['hasVisitedDarren']:
        b=("""You open the first drawer, its a photo of none other than Dodgy Darren himself with the warden""")
      else:
        b=("""You open the first drawer, its a photo of a dodgy looking fella standing with the warden""")
      b+=""" and an empty box of tabs.
You open the next drawer it contains a fiver, you pocket it and move on.
      """
      print(b)
      pause()
      player['money']+=5
    elif move == '2':#go toilet on wardens desk
      clear()
      print('.')
      sleep(1)
      clear()
      print('..')
      sleep(1)
      clear()
      print('...')
      sleep(1)
      clear()
      print('Its seeping into the drawers.')
      pause()
      pass
    elif move == '3':#check the wardrobe
      print('You find the wardens garment, its a t-shirt with a sticker reading "Hello my name is warden!" on it.')
      if input('Would you like to put it on?: yes/no\n') == 'yes':
        player['outfit'] = 'wardens garment'
        print('You put on the wardens garment, it touches your toes and feels a bit wet.')
        pause()
    elif move == '4':#nick off with keys
      print('You grab the keys and put them in your pocket.')
      player['inventory'].append('keys')
      pause()
      pass
    elif move == '5':#leave the office
      player['location'] = 'hallway'
    else:
      print('Invalid Input')
    
  

#shop darren cheesy chip shop 
  #pint (damage boost)
  #sunderland shirt (get beat up)
  #hairpin (for master key ending)
  #cheesy chips (summon jonny)

#finished locations
#cell
#wardens door
#hallway
#SHOPPPPP
#warden's office

#in progress
#food hall 
#vikki romance
#master key


#to do
# sort down bomb ending
# solitary
#be able to put sunlun shirt on