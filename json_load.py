import json


def read_json():
    file = open("fake.json",'r',encoding='utf-8')
    content=file.readlines()
    for i in content:
        lists=eval(i)
        truck = 0
        suv = 0
        bus = 0
        van = 0
        pickup = 0
        sedan = 0

        for j in lists['preds']:
            if j['label'] == 'truck':
                truck += 1
            elif j['label'] == 'suv':
                suv += 1
            elif j['label'] == 'bus':
                bus += 1
            elif j['label'] == 'van':
                van += 1
            elif j['label'] == 'pickup':
                pickup += 1
            elif j['label'] == 'sedan':
                sedan += 1
        lists['truck']=truck
        lists['suv']=suv
        lists['bus'] =bus
        lists['van'] =van
        lists['pickup'] =pickup
        lists['sedan'] =sedan
        #dicts.pop('preds')
        print(lists)
        #print(json.dumps(i))



if __name__ == '__main__':
    read_json()