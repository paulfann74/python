is_male = True
is_tall = False
if is_male or is_tall:
    print("male, tall, or both")
else:
    print("neither")


is_male2 = False
is_tall2 = False
if is_male2 or is_tall2:
    print("male, tall, or both")
else:
    print("neither")

is_male3 = False #change me
is_tall3 = True #change me
if is_male3 and is_tall3:
    print("tall male")
elif is_male3 and not(is_tall3):
    print("short guy")
elif not(is_male3) and is_tall3:
    print("tall chick")
else:
    print("neither or either")