import copy
import json

from itertools import groupby


def group_list(data, key):
    res = {}
    for k, g in groupby(data, lambda x: x[key]):
        for e in g:
            del e[key]
            # print(e)
            if k not in res:
                res[k] = []
            res[k].append(e)

    # print(res)
    return res

def group_dict(data, key):
    for k in data:
        v = data[k]
        if isinstance(v, dict):
            data[k] = group_dict(v, key)
        else:
            data[k] = group_list(v, key)
    return data

def group(data, keys):
    shim_d = {0: copy.deepcopy(data)}
    for key in keys:
        group_dict(shim_d, key)

    print(shim_d)
    return shim_d[0]


if __name__ == '__main__':
    test_case_data = [
        {
            'name': 'Alex',
            'gender': 'male',
            'species': 'human',
            'job': 'bicycle repair man',
        },
        {
            'name': 'Monika',
            'gender': 'female',
            'species': 'human',
            'job': 'stockbroker'
        },
        {
            'name': 'Bob',
            'gender': 'male',
            'species': 'human',
            'job': 'quantity surveyor'
        },
        {
            'name': 'Veronika',
            'gender': 'female',
            'species': 'human',
            'job': 'church warden'
        },
        {
            'name': 'George',
            'gender': 'male',
            'species': 'human',
            'job': 'bicycle repair man'
        },
    ]
    test_case_data_group_fields_1 = ['gender']
    test_case_data_group_fields_2 = ['species', 'gender', 'job']

    res_1 = group(test_case_data, test_case_data_group_fields_1)
    res_2 = group(test_case_data, test_case_data_group_fields_2)

    print(json.dumps(res_1, indent=2))
    print()
    print(json.dumps(res_2, indent=2))
