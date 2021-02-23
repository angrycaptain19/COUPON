import random #to shufle
# input has no use yet, code generates 2.18B codes
# coupons have form [A-Z,0-9]**6
# to add more codes an addition can be created

BASIS = ["0","1","2","3","4","5","6","7","8","9","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
Gen = []
f = open("Codes.txt","w")
for i in BASIS:
    for j in BASIS:
        for k in BASIS:
            for l in BASIS:
                for m in BASIS:
                    for n in BASIS:
                        code = i+j+k+l+m+n
                        Gen.append(code)
print(len(Gen))
random.shuffle(Gen)
for i in Gen:
    f.write(i)
f.close()