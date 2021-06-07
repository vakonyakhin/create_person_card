import random

from faker import Faker
import file_operations as f_o


def main():
    faker = Faker("ru_RU")
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
       "Стремительный прыжок",
       "Электрический выстрел",
       "Ледяной удар",
       "Стремительный удар",
       "Кислотный взгляд",
       "Тайный побег",
       "Ледяной выстрел",
       "Огненный заряд",
     ]


    def generic_person(skills):
        person = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "city": faker.city(),
            "job": faker.job(),
            "strenght": faker.random_int(8, 14),
            "endurance": faker.random_int(8, 14),
            "agility": faker.random_int(8, 14),
            "intelligence": faker.random_int(8, 14),
            "luck": faker.random_int(8, 14),
        }

        person_skills = random.sample(skills, 3)
        runnic_skills = []


        for skill in person_skills:
            for key, val in alphabet.items():
                skill = skill.replace(key, val)
            runnic_skills.append(skill)

        person["skill_1"] = runnic_skills[0].replace('е', 'е͠')
        person["skill_2"] = runnic_skills[1].replace('е', 'е͠')
        person["skill_3"] = runnic_skills[2].replace('е', 'е͠')
    
        return person


    for i in range(10):
        new_person = generic_person(skills)
        f_o.render_template("template.txt", f"cards/result-{i}.txt", new_person)

if __name__ == "__main__":
    main()
