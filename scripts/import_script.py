import csv
from django.contrib.auth.models import User
from jack.models import JackInfo, BuildingName, JackType, InPlateType, Active

file_path = '/Users/dannylopez/repos/JackTracking/scripts/files/'

jack_file = "JackInventory.csv"

def run():
    all_jacks = JackInfo.objects.all()
    all_jacks.delete()
    data_reader = csv.reader(open(file_path+jack_file, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
    count = 0
    for row in data_reader:
        if row[0] != 'Building':
            count += 1
            building_name = BuildingName.objects.get_or_create(name=row[0])
            rm_num = row[1]
            prt_num = row[2]
            plate_type = InPlateType.objects.get_or_create(name=row[3])
            jk_type = JackType.objects.get_or_create(name=row[4])
            display_name = row[6]
            phone_extension = row[7]
            active = Active.objects.get_or_create(name=row[5])
            print(building_name)
            print(rm_num)
            print(prt_num)
            print(plate_type)
            print(jk_type)
            print(display_name)
            print(phone_extension)
            print(active)
            JackInfo.objects.create(
                building_name=building_name,
                room_number=rm_num, 
                port_number=prt_num, 
                in_plate_type=plate_type, 
                jack_type=jk_type, 
                display_name=display_name, 
                phone_extension=phone_extension, 
                active=active
                )
