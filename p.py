



productos=[
    {"zandia":{
    "cantidad":12,
    "precio":23.23
    }},
    {"zandia":{
    "cantidad":12,
    "precio":23.23
    }},
    {"zandia":{
    "cantidad":12,
    "precio":23.23
    }},
    {"zandia":{
    "cantidad":12,
    "precio":23.23
    }},
    ]


for i in productos:
    for name,detalles in i.items():
        print(name)
        print(detalles["cantidad"])