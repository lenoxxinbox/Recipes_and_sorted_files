import pprint

# ЗАДАЧА С РЕЦЕПТАМИ


def create_cook_book_from_file(recipes):
    cook_book = {}
    keys = ['ingredient_name', 'quantity', 'measure']
    with open('recipes.txt', encoding='UTF-8') as f:
        for line in f:
            dish = line.strip()
            amount_ingridients = int(f.readline())
            ingridient_of_list = []
            for ingridient in range(amount_ingridients):
                internal_dict = (dict(zip(keys, f.readline().strip().split('|'))))
                internal_dict['quantity'] = int(internal_dict['quantity'])
                ingridient_of_list.append(internal_dict)
            cook_book[dish] = ingridient_of_list
            f.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    list_by_dishes = {}
    for dish in dishes:
        for value in cook_book[dish]:
            value['quantity'] *= person_count
            keys = value['ingredient_name']
            values = {'measure': value['measure'], 'quantity': value['quantity']}
            if keys in list_by_dishes:
                list_by_dishes[keys]['quantity'] += value['quantity']
            else:
                list_by_dishes.update({keys: values})
    return list_by_dishes


pprint.pprint(get_shop_list_by_dishes(create_cook_book_from_file('recipes.txt'), ['Фахитос', 'Омлет'], 2))

# ЗАДАЧА С СОРТИРОВКОЙ ФАЙЛОВ


file_list = ['1.txt', '2.txt', '3.txt']


def read_file(files):
    res_dict = {}
    i = 0
    for fi in files:
        f = open(fi, encoding='utf-8')
        res = f.readlines()
        obj = [fi, i, res]
        res_dict[len(res)] = obj
        f.close()
        i += 1

    return res_dict


def write_file(pup, file_name):
    li = []
    for k in pup.keys():
        li.append(k)
    li.sort()

    with open(file_name, 'w', encoding='utf-8') as fin:
        for ix in li:
            fin.write(pup[ix][0] + '\n')
            fin.write(str(ix) + '\n')
            for line in pup[ix][2]:
                fin.write(line)
            fin.write('\n')


write_file(read_file(file_list), 'final.txt')
