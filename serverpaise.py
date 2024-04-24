import json
from faker import Faker

def generate_fake_data(num_records, country):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            'ip_address': fake.ipv4(),
            'city': fake.city(),
            'state': fake.state_abbr(),
            'country': country
        }
        data.append(record)
    return data

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    num_records = 100  # Número de registros a serem gerados

    countries = ['Argentina', 'Peru', 'Canada', 'Estados Unidos']
    filenames = ['fake_data_argentina.json', 'fake_data_peru.json', 'fake_data_canada.json', 'fake_data_usa.json']

    for country, filename in zip(countries, filenames):
        fake_data = generate_fake_data(num_records, country)
        save_to_json(fake_data, filename)

        print(f'Dados falsos do país "{country}" foram gerados e salvos em "{filename}".')
