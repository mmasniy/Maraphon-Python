from user import User
import os
import string
from random import randint, choice

if __name__ == '__main__':
    random_values = [''.join([choice(string.ascii_letters) for letter in range(randint(3, 10))]) for value in range(2)]
    filepath1 = 'user1.json'
    filepath2 = 'user2.json'
    if os.path.exists(filepath1):
        os.remove(filepath1)
    if os.path.exists(filepath2):
        os.remove(filepath2)
    user_info1 = {
        'name': 'Test user 1',
        'email': 'test@gmail.com',
        'credit_card_info': {
            'number': '0000-1111-2222-3333',
            'cvv': '123',
            'exp': '04/24'
        },
        'friends': [
            {
                'name': '{}'.format(random_values[0]),
                'email': 'test2@gmail.com',
                'credit_card_info': {
                    'number': '3333-1111-2222-3333',
                    'cvv': '123',
                    'exp': '04/24'
                },
            },
            {
                'name': 'Test user 3',
                'email': 'test3@gmail.com',
                'credit_card_info': {
                    'number': '3333-1111-2222-3333',
                    'cvv': '123',
                    'exp': '04/24'
                },
            }
        ]
    }
    user_info2 = {
        'name': '{}'.format(random_values[1]),
        'email': 'test@gmail.com'
    }

    # creating 3 users
    user1 = User()
    user2 = User()
    user3 = User()
    # assigning dictionaries to the first 2 users
    user1.set_info(**user_info1)
    user2.set_info(**user_info2)
    # serialize user1
    user1.serialize(filepath1)
    # make sure the file was created
    assert os.path.exists(filepath1), 'File \'{}\' was supposed to be created.'.format(filepath1)
    with open(filepath1, 'r') as result_file:
        contents = result_file.read()
    # make sure json contents match expected
    assert contents == \
'''{{
   "name": "Test user 1",
   "email": "test@gmail.com",
   "credit_card_info": {{
      "number": "0000-1111-2222-3333",
      "cvv": "123",
      "exp": "04/24"
   }},
   "friends": [
      {{
         "name": \"{value}\",
         "email": "test2@gmail.com",
         "credit_card_info": {{
            "number": "3333-1111-2222-3333",
            "cvv": "123",
            "exp": "04/24"
         }}
      }},
      {{
         "name": "Test user 3",
         "email": "test3@gmail.com",
         "credit_card_info": {{
            "number": "3333-1111-2222-3333",
            "cvv": "123",
            "exp": "04/24"
         }}
      }}
   ]
}}'''.format(value=random_values[0]), 'Contents of file \'{}\' must match.'.format(filepath1)
    # serialize user2
    user2.serialize(filepath2)
    # make sure the file was created
    assert os.path.exists(filepath2), 'File \'{}\' was supposed to be created.'.format(filepath2)
    with open(filepath2, 'r') as result_file:
        contents = result_file.read()
    # make sure json contents match expected
    assert contents == \
'''{{
   "name": \"{value}\",
   "email": "test@gmail.com"
}}'''.format(value=random_values[1]), 'Contents of file \'{}\' must match.'.format(filepath2)
    print('Serialization test: Success'.center(45, '-'))
    # deserialize user3
    user3.deserialize(filepath1)
    # make sure user3 contents match user1
    assert user3.get_info() == user1.get_info(), 'Contents of user3 must match contents of user1.'
    print('Deserialization test: Success'.center(45, '-'))

