class Human(object):
    def __init__(self, name, surname, birthday, phone, city, country):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.phone = phone
        self.city = city
        self.country = country

    def get_data_dict(self):
        dict_ = {
            'name': self.name,
            'surname': self.surname,
            'birthday': self.birthday,
            'phone': self.phone,
            'city': self.city,
            'country': self.country
        }
        return dict_

    def change_data(self, **kwargs):
        data_dict = self.get_data_dict()
        data_dict.update(kwargs)
        return data_dict



if __name__ == '__main__':
    human = Human(name='name', surname='surname', birthday='12.01.2025', phone='+71234567890', city='city', country='country')
    print(human.get_data_dict())
    human_2 = Human(name='name', surname='surname', birthday='12.01.2025', phone='+71234567890', city='city',
                  country='country')
    print(human_2.change_data(name='try', surname='python'))

