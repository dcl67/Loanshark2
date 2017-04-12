import csv
from django.contrib.auth.models import User
from jack.models import Building, Room, JackType, Jack, Plate, Status, WallplatePort
from location.models import L_Building, L_Room

file_path = 'scripts/files/JackInventory.csv'
rooms_file = 'scripts/files/rooms.csv'
plates_file = 'scripts/files/plates.csv'


def isNull(item):
	if(item == null):
		return "na"
	else:
		return item

def run():
	data_reader = csv.reader(open(file_path, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
	purge_all()
	import_misc()
	#import_rooms()
	import_plates()
	import_jacks()
	print('Import script has completed running, now go away.')

def purge_all():
	print 'Purging all'
	all_jacks = Jack.objects.all()
	all_jacks.delete()
	all_active = Status.objects.all()
	all_active.delete()
	#all_build = Building.objects.all()
	#all_build.delete()
	all_types = JackType.objects.all()
	all_types.delete()
	#all_rooms = Room.objects.all()
	#all_rooms.delete()
	all_plates = Plate.objects.all()
	all_plates.delete()
	all_wallplates = WallplatePort.objects.all()
	all_wallplates.delete()
	print 'Purge Done'

"""
def import_rooms():
	room_count = 0
	data_reader = csv.reader(open(rooms_file, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
	data_reader.next()
	for row in data_reader:
		print row
		room_count += 1
		room = clean(row[0])
		build = get_building(clean(row[1]))
		print(room)
		print(build)
		print('---------------------------------------')
		room_instance = Room.objects.create(
			number=room,
			building=build
		)
	print('Room instances created: %s' % room_count)
	print('Creating rooms complete!')
"""

def import_plates():
	plate_count = 0
	data_reader = csv.reader(open(plates_file, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
	data_reader.next()
	for row in data_reader:
		plate_count +=1
		room = get_room(clean(row[1]))
		plate_num = (clean(row[2]))
		print(room)
		print(plate_num)
		print('---------------------------------------')
		plate_instance = Plate.objects.create(
			room=room,
			number=plate_num
		)

	print('Plate instances created: %s' % plate_count)
	print('Creating plates complete!')


def import_jacks():
	data_reader = csv.reader(open(file_path, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='"')
	count = 0
	data_reader.next() # throw away first line of input
	for row in data_reader:
		count += 1 
		split_plate_data = clean(row[2]).split("-")
		print('this is the split plate data: %s' % split_plate_data)
		plate_id = Plate.objects.get(number=split_plate_data[0])
		port_number = WallplatePort.objects.get(number=split_plate_data[1])
		#data_type = get_plate_type(clean(row[4]))
		print ('Plate number: %s' %plate_id)
		print ('Port number: %s' %port_number)
		data_type = get_jack_type(clean(row[4]))
		print data_type
		display_name = clean(row[6])
		phone_extension = clean(row[7])
		active = get_status(clean(row[5]))
		print(port_number)
		print(data_type)
		print(display_name)
		print(phone_extension)
		print(active)
		print(plate_id)
		print('---------------------------------------')
		entry = Jack.objects.create(
			wallplateport=port_number,
			jack_data_type=data_type,
			display_name=display_name,
			phone_extension=phone_extension,
			port_status=active,
			plate_number=plate_id
		)

		plate_id.jack.add(entry)
		plate_id.save()
		#jack.JackInfo = entry
		#jack.save()
	print(count)


def clean(field):
	if field in ('<null>', 'null', 'None', '', ' ','n/a'):
		return ''
	else:
		return field.strip()


def import_misc():
	"""
	print 'Importing MIsc data'
	InPlateType.objects.create(name="Data")
	InPlateType.objects.create(name="Phone")
	InPlateType.objects.create(name="Unknown")
	print 'plates done'
	"""
	"""
	Building.objects.create(name='Rush')
	Building.objects.create(name='Ucross')
	Building.objects.create(name='SC')
	Building.objects.create(name="Unknown")
	print 'building done'
	"""
	JackType.objects.create(name="Analog")
	JackType.objects.create(name="Data")
	JackType.objects.create(name="VOIP")
	JackType.objects.create(name="Unused")
	print 'jacks done'
	Status.objects.create(name="Unknown")
	Status.objects.create(name="Yes")
	Status.objects.create(name="no")
	print 'active done'
	WallplatePort.objects.create(number='1')
	WallplatePort.objects.create(number='2')
	WallplatePort.objects.create(number='3')
	WallplatePort.objects.create(number='4')
	WallplatePort.objects.create(number='5')
	print 'port numbers done'
"""
def get_building(input):
	try:
		return Building.objects.get(name=input)
	except:
		return Building.objects.get(name='Unknown')
"""
def get_room(input):
	try:
		return L_Room.objects.get(number=input, )
	except:
		print('Room exception raised.')
		return L_Room.objects.get(number=input)

def get_jack_type(input):
	try:
		return JackType.objects.get(name=input)
	except:
		return JackType.objects.get(name='Unused')

def get_status(input):
	try:
		return Status.objects.get(name=input)
	except:
		return Status.objects.get(name='Unknown')

def get_port(input):
	try:
		return WallplatePort.objects.get(number=input)
	except:
		return WallplatePort.objects.create(number=input)
		
def get_plate(input):
	try:
		return Plate.objects.get(number=input)
	except:
		return Plate.objects.create(number=input)
