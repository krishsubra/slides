x = ['abc', 'def', 'ghi', 'jkl']
x[0] = 'qqrq'
print(x)    # ['qqrq', 'def', 'ghi', 'jkl']

x[1:3] = ['xyz', 'dod']
print(x)    #  ['qqrq', 'xyz', 'dod', 'jkl']


x[1:3] = ['bla bla']
print(x)    #  ['qqrq', 'bla bla', 'jkl']

x[1:2] = ['elp', 'free']
print(x)    # ['qqrq', 'elp', 'free', 'jkl']
