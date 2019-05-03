state = [
    {
        'name' : '106A Copier 1'
        'ip' : '10.99.17.50',
        'status' : '',
        'queue' : [],
        'type' : 'bizhub'
    },
    '106A Copier 2': {
        'ip': 'asdfadsf'
    }
]
len = len(state)
print(state)
for copier in state.values():
    print(copier['ip'])
