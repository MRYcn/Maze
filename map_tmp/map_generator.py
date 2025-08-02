import json


def x_loc(n):
    return int(n) * 100


def y_loc(n):
    return int(n) * 100 + 55


def a(n):
    return int(n) * 90


els = ['impasse', 'straight', 'turn', 'three', 'four', 'floor']
while True:
    map_dict = {}
    try:
        print('start')
        map_dict['start'] = [x_loc(input('x:')), y_loc(input('y:'))]
        print('end')
        map_dict['end'] = [x_loc(input('x:')), y_loc(input('y:'))]
    except:
        break
    for i in els:
        print(i + ':')
        add = True
        map_dict[i] = []
        while add:
            try:
                x = x_loc(input('x:'))
                y = y_loc(input('y:'))
                ang = a(input('a:'))
                el = [x, y, ang]
                map_dict[i].append(el)
            except:
                add = False
                continue
    print('arrow')
    add = True
    map_dict['arrow'] = []
    while add:
        try:
            x = x_loc(input('x:'))
            y = y_loc(input('y:'))
            ang = a(input('a:'))
            el = [x, y, ang]
            t = input('type:')
            el.append(t)
            if 'turn' in t:
                el.append(bool(input('bool:')))
            map_dict['arrow'].append(el)
        except:
            add = False
            continue
    print('map:', map_dict)
    with open('map.json', 'w') as f:
        json.dump(map_dict, f)
    print('written')
    print('---------------------------------------------------------')
