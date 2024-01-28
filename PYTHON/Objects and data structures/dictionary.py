# key -value

# 54 => sakarya 34 => istanbul

# sehirler = ['sakarya','istanbul']
# plakalar = [54,34]

# print(plakalar[sehirler.index('istanbul')])

# print(plakalar['sakarya'])  => 54
# print(plakalar['istanbul'])  => 34

# plakalar = { 'sakarya' : 54, 'istanbul': 34}

# print(plakalar['sakarya'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['sakarya'] = 'new value'

# print(plakalar)

users = {
    'Ali': {
    'age': 16,
    'roles':['user'],
    'email': 'testali@gmail.com',
    'address':'sakarya',
    'phone':'5535145'
    },
    'Aydın':  {
    'age': 1,
    'roles': ['admin','user'],
    'email': 'testaydın@gmail.com',
    'address':'kocaeli',
    'phone':'5363824'
    }
}

print(users['hacısamet']['roles'][0])
