count = 0


def parse(position):
    global count
    tag = ''
    # print("Count before" + count)
    for i in range(count, count + position - 1 + 1):
        tag = tag + message[i]
        count += 1
    return tag


def func(tag, tagLen):
    print(tag + ": " + parse(tagLen))


message = input("Enter you FIX message")

print(message.split("|"))


func('account', 6)
func('contrNu', 10)
