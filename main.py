from random import randint
import replit
import time
import sys
#Phases:
phase1 = True
phase2 = False
#Actions:
insulted = False
#Damages:
yDMG = 0
bDMG = 0
DMGDealt = 0
DMGReceived = 0
#Needed:
sleep = time.sleep
#HP system:
yHP = 99
maxyHP = 99
bHP = 500
maxbHP = 500
#Turns:
turns = 0
#Healing Items:
sHealItem = 5
mHealItem = 3
lHealItem = 1
#Healing:
sHeal = 20
mHeal = 50
lHeal = 99
healed = 0
def scrollTxt(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.01)
  sys.stdout.write("\n")
def scrollTxtslow(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.03)
  sys.stdout.write("\n")
def menu():
  replit.clear()
  scrollTxt('Your HP: {}/{}'.format(yHP,maxyHP))
  scrollTxt('Boss HP: ??/??')
  print('\n')
  scrollTxt('[1]: Fight.')
  scrollTxt('[2]: Act.')
  scrollTxt('[3]: Item.')
  scrollTxt('[4]: Flee.')
  print("\n")
  sys.stdout.write("\n")
def othermenu():
  replit.clear()
  scrollTxt('Your HP: {}/{}'.format(yHP,maxyHP))
  scrollTxt('Boss HP: {}/{}'.format(bHP,maxbHP))
  print('\n')
  scrollTxt('[1]: Fight.')
  scrollTxt('[2]: Act.')
  scrollTxt('[3]: Item.')
  scrollTxt('[4]: Flee.')
  print("\n")
def ATK():
  replit.clear()
  scrollTxt('You attack the enemy...')
  scrollTxt('But he dodged.')
  sleep(.5)
def realATK():
  replit.clear()
  scrollTxt('You attack the enemy...')
  scrollTxt('You dealt {} damage.'.format(yDMG))
  return yDMG
def bATK():
  replit.clear()
  scrollTxt('The Boss attacks you...')
  scrollTxt("You've taken {} damage.".format(bDMG))
  sleep(.5)
  return bDMG
def act():
  replit.clear()
  scrollTxt('List of actions:')
  scrollTxt('1: Be nice.')
  scrollTxt('2: Insult.')
  scrollTxt('3: Check.')
def item():
  replit.clear()
  scrollTxt('Current items:')
  scrollTxt('1: Small Potion(Have: {})'.format(sHealItem))
  scrollTxt('2: Sweet Bread(Have: {})'.format(mHealItem))
  scrollTxt('3: Heart(Have: {})'.format(lHealItem))
def useitem():
  scrollTxt('You used the item.')
  scrollTxt('You gained {} HP.'.format(healed))
  sleep(.5)
def run():
  scrollTxt("You can't run, nor you can hide.")
  sleep(.5)
  scrollTxtslow('Keep going.')
  sleep(.5)
#Story:
scrollTxtslow('You wake up in a weird dimension.')
scrollTxtslow('There is nothing around you.')
scrollTxtslow('You see a person approaching you.')
scrollTxtslow('Scared, you immediately grab your weapon, ready to fight.')
scrollTxtslow('...')
scrollTxt('Phase 1 begin.')
sleep(2)
replit.clear()

#Phase 1:
while turns < 10 and phase1 == True:
  if yHP > 0:
    if insulted == False:
      bDMG = randint(10,15)
    elif insulted == True:
      bDMG = randint(20,25)
    menu()
    you = input('Your choice: ')
    if you == '1':
      ATK()
      yHP -= bATK()
      DMGReceived += bDMG
      turns += 1
    if you == '2':
      act()
      you2 = input('Your choice: ')
      if you2 == '1':
        scrollTxt('You tried to be nice...')
        scrollTxt("The boss doesn't care at all.")
      if you2 == '2':
        if insulted == False:
          insulted = True
          scrollTxt('You insulted him.')
          scrollTxtslow('Why?')
          scrollTxt('(Boss DMG greatly increased.)')
          sleep(.5)
        else:
          scrollTxt('You insulted him...')
          scrollTxt("He doesn't care.")
          sleep(.5)
      if you2 == '3':
        scrollTxt('BOSS:')
        scrollTxt('ATK:18; DEF:???')
        scrollTxt('You feel immense pressure...')
        sleep(.5)
      yHP -= bATK()
    if you == '3':
      item()
      you3 = input('Your choice: ')
      if you3 == '1':
        if sHealItem > 0:
          healed = sHeal
          yHP += sHeal
          sHealItem -= 1
          useitem()
        else:
          scrollTxt("You don't have that!")
      if you3 == '2':
        if mHealItem > 0:
          healed = mHeal
          yHP += mHeal
          mHealItem -= 1
          useitem()
        else:
          scrollTxt("You don't have that!")
      if you3 == '3':
        if lHealItem > 0:
          healed = lHeal
          yHP += lHeal
          lHealItem -= 1
          useitem()
        else:
          scrollTxt("You don't have that!")
      if yHP > maxyHP:
        yHP = maxyHP
      yHP -= bATK()
    if you == '4':
      run()
      yHP -= bATK()
  else:
    replit.clear()
    scrollTxt('Lose...')
    scrollTxt('Damage dealt: {}'.format(DMGDealt))
    scrollTxt('Damage received: {}'.format(DMGReceived))
    scrollTxt('On phase 1/2 at turn {}'.format(turns))
    break
if yHP > 0:
  replit.clear()
  scrollTxt('You feel weird...')
  scrollTxt('Is this a dream...?')
  scrollTxtslow('......')
  scrollTxtslow('You tried.')
  scrollTxtslow('Can not wake up.')
  sleep(.5)
  replit.clear()
  scrollTxt("???: Why do you keep fighting?")
  scrollTxt("???: You know it's useless, right?")
  sleep(.5)
  sHealItem = 5
  mHealItem = 3
  lHealItem = 1
  yHP = maxyHP
  replit.clear()
  scrollTxt('Phase 2 begin.')
  scrollTxt('HP Restored!\nITEM Restored!')
  sleep(2)
  phase2 = True
else:
  pass
  
#Phase 2:
while phase2 == True:
  if yHP > 0 and bHP > 0:
    if insulted == False:
      bDMG = randint(10,15)
    elif insulted == True:
      bDMG = randint(20,25)
    yDMG = randint(12,30)
    othermenu()
    you = input('Your choice: ')
    if you == '1':
      bHP -= realATK()
      yHP -= bATK()
      turns += 1
    if you == '2':
      act()
      you2 = input('Your choice: ')
      if you2 == '1':
        scrollTxt('You tried to be nice...')
        scrollTxt("The boss doesn't care at all.")
      if you2 == '2':
        scrollTxt('You insulted him...')
        scrollTxt("He doesn't care.")
        sleep(.5)
      if you2 == '3':
        scrollTxt('BOSS:')
        scrollTxt('ATK:18; DEF:???')
        scrollTxt('You have to fight.')
        sleep(.5)
      yHP -= bATK()
    if you == '3':
      item()
      you3 = input('Your choice: ')
      if you3 == '1':
        if sHealItem > 0:
          healed = sHeal
          yHP += sHeal
          sHealItem -= 1
          useitem()
        else:
          scrollTxt("You don't have that!")
      if you3 == '2':
        if mHealItem > 0:
          healed = mHeal
          yHP += mHeal
          mHealItem -= 1
          useitem()
        else:
          scrollTxt("You don't have that!")
      if you3 == '3':
        if lHealItem > 0:
          healed = lHeal
          yHP += lHeal
          lHealItem -= 1
          useitem()
        else:
          scrollTxt("You don't have that!")
      if yHP > maxyHP:
        yHP = maxyHP
      yHP -= bATK()
    if you == '4':
      run()
      yHP -= bATK()
  else:
    if yHP < 0:
      replit.clear()
      scrollTxt('Lose...')
      scrollTxt('Damage dealt: {}'.format(DMGDealt))
      scrollTxt('Damage received: {}'.format(DMGReceived))
      scrollTxt('On phase 2/2 at turn {}'.format(turns))
      break
    else:
      replit.clear()
      scrollTxt("???: Well done, #%@*^.")
      scrollTxt("???: We'll see eachother again.")
      sleep(1)
      replit.clear()
      scrollTxtslow('To be continued...')
      sleep(2)
      replit.clear()
      scrollTxt('Victory!')
      scrollTxt('Damage dealt: {}'.format(DMGDealt))
      scrollTxt('Damage received: {}'.format(DMGReceived))
      break