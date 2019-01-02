import csv

def csv_reading(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        skinny_list = list()
        for aDict in reader:
            skinny_dict = transform_dict(aDict) #this creates a dict with just make,model,year, fuelType, comb08
            skinny_list.append(skinny_dict)
        return skinny_list
            # filter = find_mpg(aDict, 'Volkswagen', 'Jetta', '2008') #this function returns False or the mpg that will be used in the calculation
            # if filter:
            #     return filter
def transform_dict(row):
    aDict = dict()
    aDict['id'] = row['id']
    aDict['make'] = row['make']
    aDict['model'] = row['model']
    aDict['year'] = row['year']
    aDict['fuelType'] = row['fuelType']
    aDict['comb08'] = row['comb08']
    return aDict





def find_mpg(row, make, model, year):
    if row['make'] == make and row['year'] == year and row['model'] == model:
        return row['comb08']
    return False
skinny_list = csv_reading('vehicles.csv')
make_list = []
for aDict in skinny_list:
    if aDict['make'] not in make_list:
        make_list.append(aDict['make'])
tup_list = []
make_list.sort()
for make in make_list:
    tup_list.append((make,make))

print(tup_list)

