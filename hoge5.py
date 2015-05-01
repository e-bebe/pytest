class User(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print "hoge"

class SuperUser(User):
    def shout(self):
        print "hoge"

bob = User("Bob")
tom = SuperUser("Tom")
tom.shout()
