'''
    Programa para criar dados fakes de usuarios, ips e hostname para inserir no banco
    mongodb
'''

from faker import Faker
from faker.providers import internet


fake = Faker()
#fake.add_provider(internet)
for __ in range(10):
    #print(fake.name())

    for __ in range(10):
        #print(fake.ipv4_private())

        for __ in range(10):
            #print(fake.hostname())

            for __ in range(10):
                #print(fake.administrative_unit())
                #print(fake.city())

                print(f'{fake.name()}, {fake.ipv4_private()} , {fake.administrative_unit()} , {fake.city()}')