def linearsearchproduct(productlist, targetProduct):
   indices=[]
   for index,product in enumerate(productlist):
    if product==targetProduct:
       indices.append(index)
   return indices
product=["shoes", "boot","loafer","shoes","sandal","shoes"]
target="shoes"
result=linearsearchproduct(product,target)
print(result)