import random
import argparse

import file_operations as f_o

from faker import Faker


def create_parser():
    parser = argparse.ArgumentParser(description='Программа генерирует случайные карточки персонажей в формате .svg. ')
    parser.add_argument('--path', default='new', help='Путь для сохранения карточек. По умолчанию "cards/"')
    parser.add_argument('--minrange', type=int, default=8, help='Минимальное значение диапазона' )
    parser.add_argument('--maxrange', type=int, default=14, help='Максимальное значение диапазона' )
    parser.add_argument('--count', type=int, default=10, help='Количество карточек' )


    args = parser.parse_args()
    return args


def generate_person(skills,alphabet,parser):
    faker = Faker("ru_RU")
    
    person = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "town": faker.city(),
            "job": faker.job(),
            "strength": faker.random_int(parser.minrange, parser.maxrange),
            "endurance": faker.random_int(parser.minrange, parser.maxrange),
            "agility": faker.random_int(parser.minrange, parser.maxrange),
            "intelligence": faker.random_int(parser.minrange, parser.maxrange),
            "luck": faker.random_int(parser.minrange, parser.maxrange),
        }
    person["skill_1"], person["skill_2"], person["skill_3"] = skills
        
    return person
    

def convert_skills(skills, alphabet):
    runnic_skills = []
    for skill in skills:
        for key, val in alphabet.items():
            skill = skill.replace(key, val)
        runnic_skills.append(skill)

    return runnic_skills


def main():
       
    alphabet = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
     }

    skills = [
       'Стремительный прыжок',
       'Электрический выстрел',
       'Ледяной удар',
       'Стремительный удар',
       'Кислотный взгляд',
       'Тайный побег',
       'Ледяной выстрел',
       'Огненный заряд',
     ]

    runnic_skills = random.sample(convert_skills(skills, alphabet),3)
    
    parser = create_parser()
    
    try:
        for number in range(parser.count):
            new_person = generate_person(runnic_skills,alphabet, parser)
            f_o.render_template('charsheet.svg', f'{parser.path}/form-{number}.svg', new_person)
    except ValueError:
        print('Минимальное значение minrange не может быть больше максимального maxrange')
    except FileNotFoundError:
        print(f'Путь для сохранения "{parser.path}/" не найден')
    

if __name__ == "__main__":
    main()
