f = open("index2.txt","r")
o = open("output.txt","w")
k = 0
somma = 0

for i in f:
    i = float(i)
    somma = somma + i
    k += 1
f.close()
media = somma / k
f = open("index2.txt","r")
for let in f:
    num = float(let)
    o.write("%.2f\n" % num)

o.close()
o = open("output.txt","a")
o.write("MEDIA: %.2f\n" % media)
o.write("SOMMA: %.2f\n" % somma)
o.close()
f.close()
print("fatto")
