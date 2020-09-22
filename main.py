user_in = input('Please enter a physical constant:').lower()

def physconst(user_in):

    """ Returns the numerical value for constants. 

    user_in = input('their chosen physical constant')

    returned is constant"""

    if user_in == 'speed of light':
        print('2.99792458e8')

    if user_in == 'plancks constant':
        print('6.62606896e−34')      

    if user_in == 'boltzmanns constant':
        print('1.3806504e−23')

    if user_in == 'electron mass':
        print('9.10938215e−31')

    if user_in == 'atomic mass unit':
        print('1.660538782e−27')   

    if user_in == 'electron charge':
        print('1.602176487e−19')

    if user_in == 'bohr radius':
        print('5.2917720859e−11')

    if user_in == 'gravitational constant':
        print('6.67428e−11')

    if user_in == 'stefan-boltzmann constant':
        print('2.9979245e8')
physconst(user_in)