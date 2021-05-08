import hashlib


def md5_hash(str):
    hash_object = hashlib.md5(bytes(str, 'utf-8'))
    print(f'Original string: {str}')
    print('md5 hash generated is')
    print(hash_object.hexdigest())


def sha1_hash(str):
    hash_object = hashlib.sha1(bytes(str, 'utf-8'))
    print(f'Original string: {str}')
    print('sha1 hash generated is')
    print(hash_object.hexdigest())


# if __name__ == "__main__":
#     md5_hash("My hovercraft is full of eels")
#     sha1_hash("My hovercraft is full of eels")
