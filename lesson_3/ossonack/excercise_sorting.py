car_brands = ["volvo", "volkswagen", "toyota", "ford", "mercedes-benz", "bmw", "audi", "kia", "renault", "peugeot"]

print(sorted(car_brands))
car_brands.sort()
print(car_brands)
print(sorted(car_brands, reverse=True))
car_brands.sort(reverse=True)
print(car_brands)

def sortBrand(elem):
    return elem[0]

def sortModel(elem):
    return elem[1]

car_list = [("volvo","xc90"),
            ("volkswagen","golf"),
            ("toyota","corolla"),
            ("ford","ranger"),
            ("mercedes-benz","c-class"),
            ("bmw","x5"),
            ("audi","a3"),
            ("kia","sportage"),
            ("renault","mégane"),
            ("peugeot","308")]

print("Cars sorted by brand:", sorted(car_list, key=sortBrand))
print("Cars sorted by model:", sorted(car_list, key=sortModel))