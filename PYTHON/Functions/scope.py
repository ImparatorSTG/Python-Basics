# global scope
x = 'global x'

def function():
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)

###########################

# global
name = 'Zümra'

def changeName(new_name):
    # local
    global name
    name = new_name
    print(name)

changeName('Hilal')
print(name)

###########################

name = 'global string'

def greeting():
    # name = 'Hilal'

    def hello():
        # name = 'Zümra'
        print('hello'+ name)

    hello()

greeting()


###########################

x = 50
def test ():
    global x
    print(f'x :{x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)
