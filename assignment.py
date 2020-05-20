def get_name():
    return input("What is your name? ")


def get_age():
    return input("What age are you? ")


def get_user_info(name=get_name(), age=get_age()):
    decades_lived = int(age) // 10
    print('Your name is ' + name + ' and you are ' + age +
          ' years old.' + ' Wow, you have lived for ' + str(decades_lived) + ' decades!')


get_user_info()
