import csv

def csv_reader():
    
    animal = input("Animal:")
    
    if animal.lower() == "dog" or animal.lower() == "dogs":
        with open('data/dogs.csv', "r") as dogs_file: 
            for row in dogs_file:
                no_comma_name = str(row.split(' ')[0]).replace(',',"")
                no_comma_age = str(row.split(' ')[1]).replace(',',"")
                no_comma_breed = str(row.split(' ')[2]).replace(',',"").replace('\n',"")
                if row.split(' ')[0] != 'name,' and row.split(' ')[1] != 'age,' and row.split(' ')[2] != 'breed,':
                    print(no_comma_name + " is a " + no_comma_age + " year old " + no_comma_breed + ".")
    
    elif animal.lower() == "cat" or animal.lower() == "cats":
        with open('data/cats.csv', "r") as cats_file: 
            for row in cats_file:
                no_comma_name = str(row.split(' ')[0]).replace(',',"")
                no_comma_age = str(row.split(' ')[1]).replace(',',"")
                no_comma_breed = str(row.split(' ')[2]).replace(',',"").replace('\n',"")
                if row.split(' ')[0] != 'name,' and row.split(' ')[1] != 'age,' and row.split(' ')[2] != 'breed,':
                    print(no_comma_name + " is a " + no_comma_age + " year old " + no_comma_breed + ".")
    
    else: print(f"Sorry, we don't have any {animal}s here")

csv_reader()