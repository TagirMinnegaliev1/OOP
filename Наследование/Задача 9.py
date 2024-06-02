class Profile:
    def __init__(self, profession):
        self.profession = profession

    def info(self):
        return ""

    def describe(self):
        print("Профессия:", self.profession)
        print(self.info())


class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)
        self.salary = salary

    def info(self):
        return "Предлагаемая зарплата: {}".format(self.salary)


class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.experience = experience

    def info(self):
        return "Стаж работы: {}".format(self.experience)
    
vacancy = Vacancy("Python Developer", 100000)
resume = Resume("Data Scientist", "3 years")

vacancy.describe()
resume.describe()
