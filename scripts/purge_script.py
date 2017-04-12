from jack.models import Building, Room, JackType, Jack, Plate, Status, WallplatePort

def run():
	print 'Purging all'
	all_jacks = Jack.objects.all()
	all_jacks.delete()
	all_active = Status.objects.all()
	all_active.delete()
	all_build = Building.objects.all()
	all_build.delete()
	all_types = JackType.objects.all()
	all_types.delete()
	all_rooms = Room.objects.all()
	all_rooms.delete()
	all_plates = Plate.objects.all()
	all_plates.delete()
	all_wallplates = WallplatePort.objects.all()
	all_wallplates.delete()
	print 'Purge Done'