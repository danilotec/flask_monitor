from flask import redirect, url_for

# enter_user = input('your user: ')
# enter_password = input('your password: ') #descomentar as entradas


def login_users(users, enter_user, enter_password):
    enter = False
    for u in users:
        try:
            if enter_user == u['user'] and enter_password == u['password']:
                enter = True
                break
        except Exception as e:
            print(f'deu um erro aq, se vira pra descobrir\n {e.__class__}')
            break
    if enter == True:
        return redirect(url_for(u['screen']))
    elif enter == False:
        return 'user not found'


# login(users, enter_user, enter_password) #descomentar isso aq pra executar a função
