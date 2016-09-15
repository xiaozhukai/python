# for i in range(1025):
#     f = open('html.htm', 'w')
#     print "%d : %d" % (i, f.fileno())

list_f = []

for i in range(1025):
    list_f.append(open('html.htm', 'w'))
    print "%d : %d" % (i, list_f[i].fileno())
