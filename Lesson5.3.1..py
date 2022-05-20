
clothes = ["socks", "shirt", "skirt,""scarf"]

def insert_element(new_cloth, index=0):
     clothes.insert(index, new_cloth)
     print(clothes)

insert_element("T-shirt", 3)
insert_element("shorts", -1)
insert_element("blouse")



