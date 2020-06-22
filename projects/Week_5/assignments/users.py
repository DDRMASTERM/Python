banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user in banned_users:
    print(user.title() + ", you have been banned.")
else:
    print(user.title() + ", you can post a response if you wish.")
