import faker


def generate_random_user():
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    telephone = fake.phone_number()
    password = fake.password()

    user_data = {
        'First Name': first_name,
        'Last Name': last_name,
        'E-Mail': email,
        'Telephone': telephone,
        'Password': password
    }

    return user_data


def random_product(test_pattern: str):
    fake = faker.Faker()

    product_name = 'AaA' + test_pattern + fake.text(max_nb_chars=10)  # Генерируем название продукта с ограничением в 10 символов
    meta_title = fake.sentence(nb_words=4)  # Генерируем Meta title
    model = fake.bothify(text="??#??#")  # Генерируем модель товара с добавлением букв

    product_data_dict = {
        'product_name': product_name,
        'meta_title': meta_title,
        'model': model
    }

    return product_data_dict


if __name__ == "__main__":
    user_data = generate_random_user()
    product_data = random_product()
