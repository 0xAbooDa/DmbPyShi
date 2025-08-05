import random
import sys

print('Hell Ya freeeeeee!!!')
choice=input('you wnana free discounts????   [type y/n]  ')
if(choice == 'n'):
  print('Your choice your loss')
  for i in range(1000):
    print('Bye')
  sys.exit()
for i in range(3):
  dis = random.randrange(1, 100)
  print(dis)
print('*******************')
print('choose a discount')
print('*******************')
































































































































