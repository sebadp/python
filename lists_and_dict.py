def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Sebastián", "lastname": "Dávila"} 

    my_superlist = [
        {"firstname": "Sebastián", "lastname": "Dávila"},
        {"firstname": "Josela", "lastname": "Martín"},
        {"firstname": "Lucio Sirio", "lastname": "Dávila Martín"},
        {"firstname": "Héctor Oscar", "lastname": "Dávila"},
        {"firstname": "Miguel", "lastname": "Martín"},
        {"firstname": "Manuel", "lastname": "Martín"}
    ]

    my_superdict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [0.1, 1.5, 2.5, 6.55]
    }

    # for key, value in my_superdict.items():
    #     print(key, "-", value)

    # for values in my_superlist:
    #     for key, value in values.items():
    #         print(f'{key} - {value}')
    #     print('-----------------------------------')
            
    for value in my_superdict.items():
        print(value)

if __name__ == '__main__':
    run()