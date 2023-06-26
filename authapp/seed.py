# from django_seed import Seed    
# from authapp.models import Class
# import random

# def run_authapp():
#     seeder = Seed.seeder()

#     # Seed pour le modèle President
#     seeder.add_entity(President, 5, {
#         'nom': lambda x: seeder.faker.name(),
#         'age': lambda x: seeder.faker.random_int(min=30, max=80),
#         'genre': lambda x: seeder.faker.random_element(['M', 'F']),
#     })

#     print(seeder.execute())
