from enemy import Enemy, Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother = Enemy("Urg", 23)
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vamp.alive:
    if not vamp.dodges():
        vamp.take_damage(1)
        print(vamp)
