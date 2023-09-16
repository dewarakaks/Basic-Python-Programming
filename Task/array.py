list = [
        ["Dika", 190, 60.5],
        ["Deka", 170, 58.5],
        ['Dimas', 200, 90.5],
        ['Anisa', 155, 70.5],
        ['Thobie', 130, 55.5],
        ]
name = input("Input name: ")
found = False
for i in range(len(list)):
    if list[i][0].lower() == name.lower():
        print(f"{name} found. height is {list[i][1]} cm and weight is {list[i][2]} Kg.")
        found = True
        break
if not found:
    print(f"name is not found")