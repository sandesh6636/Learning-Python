# f = open("test.txt","r")
# inner_text = f.read()
# print(inner_text)
# f.close()

# x = open("txtt2.txt","w")
y = open("test.txt","w")
y.write("HI My name is Sandesh rai")
y.close()

with open("test.txt","a") as f:
    f.write("BIGGGG BIGGG")


# z = open("txtt2.txt","r")
# while True:
#     lines = z.readline()
#     if not lines:
#         break;
#     print(lines)


# f = open("numbers.txt","r")
# i=0
# while True:
#     i+=1
#     lines = f.readline()
#     if not lines:
#         break;
#     m1=int(lines.split(",")[0])
#     m2=int(lines.split(",")[1])
#     m3=int(lines.split(",")[2])
#     print(f"Marks of student {i} in math is {m1}")
#     print(f"Marks of student {i} in math is {m2}")
#     print(f"Marks of student {i} in math is {m3}")
#     print(lines)

u = open("txtt.txt","w")
# u.write("line1 \n lin2 \n line3\n")
lines = ['lines1\nlines2\nlines3\nlines4\n']
u.writelines(lines)
u.close()
