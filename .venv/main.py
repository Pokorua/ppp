import requests
import random
def check_steam(accountname : str):
  count = str(random.randint(1, 11))
  
  param = {'accountname' : accountname, 'count' : count}
  url =  f'https://store.steampowered.com/join/checkavail/'
  return requests.post(url, data=param).json()['bAvailable']
  

check = check_steam(input('Введите имя аккаунта: ')) 
if check == False:
    print('Логин существует, оплата возможна')
elif check == True:
    print('Логин не существует, оплата не проходит')    
