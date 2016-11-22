import csv
from django.contrib.auth.models import User
from jack.models import JackInfo, BuildingName, JackType, InPlateType, Active

file_path = 'scripts/files/JackInventory.csv'

def isNull(item):
	if(item == null):
		return "na"
	else:
		return item

def run():
	all_jacks = JackInfo.objects.all()
	all_jacks.delete()
	data_reader = csv.reader(open(file_path, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
	count = 0
	data_reader.next() # throw away fist line of input
	for row in data_reader:
		count += 1
		lbuilding_name = BuildingName.objects.get_or_create(name=row[0])
		rm_num = row[1]
		prt_num = row[2]
		plate_type = InPlateType.objects.get_or_create(name=row[4])
		ldisplay_name = row[6]
		lphone_extension = row[7]
		lactive = Active.objects.get_or_create(name=row[5])
		JackInfo.objects.create(
			building_name=lbuilding_name,
			room_number=rm_num, 
			port_number=prt_num, 
			in_plate_type=plate_type, 
			jack_type=jk_type, 
			display_name=ldisplay_name, 
			phone_extension=lphone_extension, 
			active=lactive
		)

		
	print(count)
	
# What follows is Danny's original implementation
        '''if row[0] != 'Building': #replaced by data_reader.next() to get rid of header.
            count += 1              #intended to show how many records have been read.
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
         '''   
