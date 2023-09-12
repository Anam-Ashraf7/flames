name = input("Enter your name: ")
partner = input("Enter your partners name: ")
name = name.replace(" ","")
partner = partner.replace(" ","")


if name.isalpha() and partner.isalpha():
    name = name.lower()
    partner = partner.lower()
    new_name = ""
    new_partner = ""

    for i in name:
        if i not in partner:
            new_name += i

    for j in partner:
        if j not in name:
            new_partner += j
                
    total_letters = len(new_name) + len(new_partner)

    flames = ["F","L","A","M","E","S"]
    index = 0
    while len(flames) > 1:
        index = (index + total_letters - 1) % len(flames)
        flames.pop(index)   

    if flames[0] == "F":
        print("You both are Friends")
    elif flames[0] == "L":
        print("You both are Lovers")
    elif flames[0] == "A":
        print("You both are Attracted towards each other")
    elif flames[0] == "M":
        print("You both are Married")
    elif flames[0] == "E":
        print("You both are Enemies")
    elif flames[0] == "S":
        print("You both are Siblings")

else:
    print("Invalid name")