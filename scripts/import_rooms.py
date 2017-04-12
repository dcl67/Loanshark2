import csv
from location.models import L_Building, L_Room

rooms_file = 'scripts/files/rooms.csv'

def run():
    purge_rooms()
    import_misc()
    import_rooms()

def purge_rooms():
	print 'Purging rooms'
	all_build = L_Building.objects.all()
	all_build.delete()
	all_rooms = L_Room.objects.all()
	all_rooms.delete()


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
		room_instance = L_Room.objects.create(
			number=room,
			building=build
		)
	print('Room instances created: %s' % room_count)
	print('Creating rooms complete!')


def import_misc():
	L_Building.objects.create(name='Rush')
	L_Building.objects.create(name='Ucross')
	L_Building.objects.create(name='SC')
	L_Building.objects.create(name="Unknown")
	print 'building done'


def clean(field):
	if field in ('<null>', 'null', 'None', '', ' ','n/a'):
		return ''
	else:
		return field.strip()

def get_building(input):
    	try:
		return L_Building.objects.get(name=input)
	except:
		return L_Building.objects.get(name='Unknown')

def get_room(input):
	try:
		return L_Room.objects.get(number=input, )
	except:
		print('Room exception raised.')
		return L_Room.objects.get(number=input)