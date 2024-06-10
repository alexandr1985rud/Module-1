immutable_var = 1, 3, 10, "Laptop", True
print(immutable_var)
# кортеж нельзя изменить, потому что это список защищённый от изменений

mutable_list = [1, 3, 10, "Laptop", True]
print(mutable_list)
mutable_list[1] = 333
mutable_list.remove("Laptop")
mutable_list.extend(["Александр", False])
print(mutable_list)
