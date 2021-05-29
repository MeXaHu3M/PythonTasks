import re

reg = re.compile('\\w\\w\\d{7}')
regS = re.compile('a\\w\\d\\d55661')

input()
tickets = input().split(' ')
for ticket in tickets:
    if not reg.fullmatch(ticket):
        print(ticket, '-1')
        continue
    if regS.fullmatch(ticket):
        print(ticket)
    