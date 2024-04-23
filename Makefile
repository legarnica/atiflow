dumpdata:
	python manage.py dumpdata auth.user --indent 2 > _backup/auth_user.json
	python manage.py dumpdata atiflow --indent 2 > _backup/atiflow.json

loaddata:
	python manage.py loaddata _backup/auth_user.json
	python manage.py loaddata _backup/atiflow.json