import json

counter=0
close=True

with open("sds.json","r",encoding="utf-8") as file:
    cars=json.load(file)

def menu() : 
    print("- Вывести все записи n\n- Вывести запись по полю n\n- Добавить запись n\n- Удалить запись по полю n\n- Выйти из программы")


def all() :   
    global counter
    for car in cars :
        print(f'''
 ____________________________________
                   
 ID : {car["id"]}
 модель : {car["name"]}
 производитель : {car["manufacturer"]}
 заправляется ли бензиноом : {car["is_petrol"]}
 обьем бака : {car["tank_volume"]}
 ____________________________________
''')
    counter+=1

def one_output() :
    global counter
    car_id_choice=int(input("введите ID автомобиля : "))
    for car in cars :
        if car_id_choice==car["id"] :
            print(f'''
 ____________________________________

 ID : {car["id"]}
 модель : {car["name"]}
 производитель : {car["manufacturer"]}
 заправляется ли бензиноом : {car["is_petrol"]}
 обьем бака : {car["tank_volume"]}
 ____________________________________
''')
            button=True
            break
    counter+=1

def new() :
    global counter
    lkl=False
    inp_id=int(input("введите номер автомобиля : "))
    for car in cars:
        if inp_id==car["id"]:
            lkl=True
            break
    if lkl :
        print("под данным id уже зарегеcтрирован автомобиль.")
    else :
        name=input("введите марку автомобиля : ")
        manufacturer=input("введите производителя автомобиля : ")
        is_petrol=input("данный автомобиль заправляется бензином ?")
        tank_volume=input("какой обьем бака у автомобиля(если его нет , ставьте '-') : ")

        new_car={
            "id": inp_id,
            "name": name,
            "manufacturer": manufacturer,
            "is_petrol": True if is_petrol.lower() == 'да' else False,
            "tank_volume": tank_volume
        }

        cars.append(new_car)
        with open("sds.json", 'w', encoding='utf-8') as output_file: 
            json.dump(cars, output_file, ensure_ascii=False, indent=2)
    counter+=1

def delete() :
    global counter
    mkm=False
    choice_car_delete=int(input("введите id автомобиля , который хотите удалить : "))
    for car in cars :
        if choice_car_delete == car["id"] :
            cars.remove(car)
            mkm=True
            break
    if mkm :
        with open("sds.json", 'w', encoding='utf-8') as output_file:
            json.dump(cars, output_file, ensure_ascii=False, indent=2)
        print("запись успешно удалена.")
    else :
        print("автомобиля под данным id не существует.")
    counter+=1

def end() :
    global close
    print(f"количество циклов программы : {counter}\nзавершение работы программы...")
    close = False

    
def main() :
    while close :
        menu()
        choice=int(input("выберите одно из предложенных действий(число от 1 до 5) : "))

        if choice==1 :
            all()
        elif choice==2 :
            one_output()
        elif choice==3 :
            new()
        elif choice==4 :
            delete()
        elif choice==5 :
            end()
        else :print("некорректный ввод , попробуйте еще раз .")

main()  
