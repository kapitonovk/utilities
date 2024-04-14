import csv

mp = open('m_m_houses.csv').read().split('\n')
bs = open('77houses.csv').read().split('\n')

result = []

street_index = bs[0].split(';').index('formalname_street')
house_index = bs[0].split(';').index('house_number')
building_index = bs[0].split(';').index('building')
block_index = bs[0].split(';').index('block')
letter_index = bs[0].split(';').index('letter')
year_index = bs[0].split(';').index('built_year')
project_index = bs[0].split(';').index('project_type')
floor_index = bs[0].split(';').index('floor_count_max')
residarea_index = bs[0].split(';').index('area_residential')

print(street_index)

for j in mp[1::]:
##    print(j.split(',')[2].replace('"', ''))
    for i in bs[1::]:
        if len(i.split(';')) == len(bs[0].split(';')):
            street = i.split(';')[street_index]
            house = i.split(';')[house_index]
            building = i.split(';')[building_index]
            block = i.split(';')[block_index]
            letter = i.split(';')[letter_index]
            year = i.split(';')[year_index]
            project = i.split(';')[project_index]
            floor = i.split(';')[floor_index]
            residarea = i.split(';')[residarea_index]

            if letter:
                house = house + letter

            if block:
                house = house + "к" + block

            if building:
                house = house + 'с' + building

##            print(house)

            if len(j.split(';')) == 3 and len(street) > 3:
                id1 = j.split(';')[0]
                str1 = j.split(';')[1]
                house1 = str(j.split(';')[2]).replace('"', '')
                house1 = house1.replace(' ','')

                if (street in str1) and (str(house) == str(house1)):
                    result.append([id1.replace('"', ''), year, project, floor, residarea])
                    print(street, str1, house, house1)

with open(input('save as filename?.. '), 'w') as c:
    writer = csv.writer(c, delimiter=';')
    writer.writerows(result)
