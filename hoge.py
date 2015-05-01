msg = "hello world"
print msg

s = "abcdefghi"
print len(s)
print s.find("h")
print s[2:5]

print 5 + int("5")

a = (2, 5, 8)
print len(a)

b = set([1, 2, 3, 1])

print b


a = {"hoge":50, "hage": 30}
print a["hoge"]
a["hage"] = 800
print a

print "hoge" in a
print a.keys()


users = {"taguchi":200, "fkoji":300, "doto":500}
for key, value in users.iteritems():
        print "key: %s value: %d" % (key, value)

