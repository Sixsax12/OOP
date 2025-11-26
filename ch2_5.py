print(" *** Number Fun !!! ***")
a,b = input("Enter a b : ").split()
print("a=",a,"\ttype =",type(a))
print("b=",b,"\ttype =",type(b))
print("a+b =>",a,"+",b,"=>",a+b)
print("a/b = {:.2f}".format(int(a)/int(b)))
print("b/a = {:.3f}".format(int(b)/int(a)))
print("a/b =", int(a) // int(b), "r", int(a) % int(b))
print("b/a =", int(b) // int(a), "r", int(b) % int(a))

# convert a to int
# convert b to int
# แสดงผล a/b ทศนิยม 2 ตำแหน่ง
# แสดงผล b/a ทศนิยม 3 ตำแหน่ง
# แสดงผลการหารแบบเหลือเศษของ a และ b
# แสดงผลการหารแบบเหลือเศษของ b และ a