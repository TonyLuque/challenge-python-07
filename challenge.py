DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Mentor',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Mariandrea',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def homeless(data):
    new_data = dict(data)
    new_data['homeless'] = True if new_data['organization'] == '' else False
    return new_data

def old(data):
    new_data = dict(data)
    new_data['old'] = True if new_data['age'] > 30 else False
    return new_data

def run():

    all_python_devs = filter(lambda x: x['language'] == 'python', DATA) 
    # Using filter, generate a list with all the python devs
    all_Platzi_workers = filter(lambda x: x['organization'] == 'Platzi', DATA) 
    # Using filter, generate a list with all the Platzi workers
    adults =  filter(lambda x: x['age'] >= 18, DATA) 
    # Using filter, generate a list with all people over 18 years old
    workers =  map(homeless, DATA)
    # Using map, generate a new list of people with a key 'homeless' with True or False values, if 'organization' have something or not
    old_people =  map(old, DATA)
    # # Using map, generate a new list of people with a key 'old' with True or False values, if 'age' is greater than 30 or not

    print('Python devs: ')
    for dev in all_python_devs:
        print(dev['name'])
    print('\n\n')

    print('Platzi workers: ')
    for worker in all_Platzi_workers:
        print(worker['name'])
    print('\n\n')

    print('Adults: ')
    for adult in adults:
        print(adult['name'])
    print('\n\n')

    print(list(workers))
    print('\n\n')

    print(list(old_people))
    print('\n\n')

    # Remember: when possible, use lambdas


if __name__ == '__main__':
    run()
