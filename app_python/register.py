from data import users



def register(new_user, new_password, new_screen):
    # new_user = input('new user: ')
    # new_password = input('new password: ')
    # new_screen = input('new screen: ')

    users.append({"user": new_user, "password": new_password, "screen": new_screen})

# while True:
#     register()
#     exit = input('[E]xit? ').lower()
#     if exit == 'e':
#         break
    #esse while será necessario na aplicação? sla mas deixa ai, vai q precisa, vou testar dps

# for u in users:
#     print(u)