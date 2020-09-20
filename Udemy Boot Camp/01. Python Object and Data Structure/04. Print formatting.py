#.format()
print("This is a {} {} {}".format('fox', 'brown', 'quick'))

print("This is a {2} {1} {0}".format('fox', 'brown', 'quick'))

print("This is a {q} {b} {f}".format(f='fox', b='brown', q='quick'))

#how to change precision
res = 100/777
print("The result was {r:1.3f}".format(r=res))
print("The result was {r:10.3f}".format(r=res))

#alligment
#By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a left, center or right alignment:
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))

#You can precede the aligment operator with a padding character
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

# f added in Python 3.6
print(f"The result was {res:1.3f}")
print(f"The result was {res}")

#oldest method: Formatting with placeholders
#You can use %s to inject strings into your print statements.
print("I'm going to inject %s text here, and %s text here." %('some','more'))

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

#The %s operator converts whatever it sees into a string, including integers and floats. The %d operator converts numbers to integers first, without rounding
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)


print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))