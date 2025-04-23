names=['Harry Potter','Ron Weasley','Hermione Granger']
print(names[0])
print(names[1])
print(names[2])
print(names[0]+',have a nice day today!')
print(names[1]+',have a nice day today!')
print(names[2]+',have a nice day today!')
vehicles=['car','bycicle','broomstick','underground','bus']
print('I think the most comfortable vehicle is a '+vehicles[-1]+' with empty seats.')

guests=['McGonagall','Harry Potter','Severus Snape','Sirius Black']
for guest in guests:
    print("\n\tDear "+guest+",I'd be honored if you could join me for dinner!")
print(guests[0]+' is not going to make it.')
del guests[0]
guests.insert(0,'Hagrid')
for guest in guests:
    print("\n\tDear "+guest+",I'd be honored if you could join me for dinner!")
print('I have found a bigger table just now.')
guests.insert(0,'Albus Dembledor')
guests.insert(3,'Ron Weasley')
guests.append('Hermione Granger')
for guest in guests:
    print("\n\tDear "+guest+",I'd be honored if you could join me for dinner!")
print(len(guests))
print('Sorry,the big table was stolen by Monkston.I could only invite two guests.')
removed_guest=guests.pop(0)
print(removed_guest+" Sorry,can't have dinner with you this time.")
removed_guest1=guests.pop(2)
print(removed_guest1+" Sorry,can't have dinner with you this time.")
removed_guest2=guests.pop(3)
print(removed_guest2+" Sorry,can't have dinner with you this time.")
removed_guest3=guests.pop(1)
print(removed_guest3+" Sorry,can't have dinner with you this time.")
removed_guest4=guests.pop(2)
print(removed_guest4+" Sorry,can't have dinner with you this time.")
print(guests)
print(guests[0]+",You are still invited.")
print(guests[1]+",You are still invited.")
del guests[0]
del guests[0]
print(guests)