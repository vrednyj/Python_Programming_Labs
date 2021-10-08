
def empty_lines(l):
    for i in range(l):
        print("{}".format("<" + " " * 48 + ">"))

print("{}".format("v"*50))
empty_lines(3)
print("<{:^48s}>".format("Title"))
empty_lines(2)
print("<  {0:}  {1:} {2:<36s}>".format("A","Option","a"))
print("<  {0:}  {1:} {2:<36s}>".format("B","Option","b"))
print("<  {0:}  {1:} {2:<36s}>".format("C","Option","c"))
empty_lines(2)
print("{}".format("v"*50))
