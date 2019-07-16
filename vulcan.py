with open(r"C:\Users\86158\Desktop\mbc.txt","r",encoding="UTF-8-sig") as f:
    a = f.readlines()

b=[]
for i in a:
    i=i.strip()
    b.append(i)
print(b)
