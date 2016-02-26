
class Hello:

    def __init__(self, name ):
        self._name = name


    def sayHello(self):
        print('hello {0}'.format(self._name))


h = Hello('RockWang')

h.sayHello()


#extends
class Hi(Hello):

    def __init__(self, name):
        Hello.__init__(self, name)

    def sayHi(self):
        print( 'hi {0}'.format(self._name) )


h1 = Hi('Yock');
h1.sayHi()
