items = [ "apple", "bnana","apple"]

u_i = set()

for item in items:
    if item in u_i:
        print("Duplicate: ", item)
        break
    u_i.add(item)