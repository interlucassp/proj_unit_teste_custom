import faker

fake = faker.Faker()

def generate_user():
    return {
        "username": fake.user_name(),
        "password": fake.password(),
        "email": fake.email()
    }
