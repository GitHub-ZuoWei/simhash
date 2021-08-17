from simhash import SimhashIndexWithMongo

data = {
    1: 'How are you? I Am fine. blar blar blar blar blar Thanks.',
    2: 'How are you i am fine. blar blar blar blar blar than',
    3: 'This is simhash test.',
    4: 'How are you i am fine. blar blar blar blar blar thank1',
}

objs = [(str(k), v) for k, v in data.items()]
index = SimhashIndexWithMongo(objs, k=10)