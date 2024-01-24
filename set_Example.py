# 2) fruits={apple,grapes,mango,dragon,orchides,kivi,chiku,leamon}
# 	1) arrange the data in assending order
# 	2) delete middle element
# 	3) replace the fruit leamon with another name
# 	4) count the list data
# 	5) use the join function with *
# 	6) generate another set with categorie indian fruits if={apple,grapes,guava, chiku}
# 	7) match both the set
# 	8) use different operators for matching
#


# fruits={"apple","grapes","mango","dragon","orchides","kivi","chiku","lemon"}
# fruits_list=list(fruits)
# fruits_list.sort()
# print(fruits_list)
#
# print("Deleting middle element..")
# fruits.remove("dragon")
# print(fruits)
#
# fruits.remove("lemon")
# fruits.add("banana")
# print(fruits)
#
# print(len(fruits))
#
#
# print("*".join(fruits))
#
# indianFruits={"apple","grapes","chiku","guava"}
# print(fruits.union(indianFruits))
# print(fruits.intersection(indianFruits))
# print(fruits.difference(indianFruits))



# 3) w=(45,35,25,1,2,3,45,35,25)
# 	1) sort the data
# 	2) remove the duplicate elements
# 	3) replace value 1
# 	4) insert negation value
# 	5) arrange the data in assending
# 	6) delete the last element

w=(45,35,25,1,2,3,45,35,25)
new_w=list(w)
new_w.sort()
print(new_w)

new_w.remove(45)
new_w.remove(35)
new_w.remove(25)

print(new_w)

new_w.remove(1)
new_w.insert(0,5)
print(new_w)

new_w.insert(0,-10)

print(new_w)
new_w.sort()

print(new_w)
last=len(new_w)-1

new_w.remove(new_w[last])
print(new_w)












