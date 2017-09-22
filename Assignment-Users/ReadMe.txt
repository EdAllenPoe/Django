(djangoEnv) Bryans-MacBook-Pro:assignment_users bryanlockward$ python manage.py makemigrations
Migrations for 'assignmentuser':
  apps/assignmentuser/migrations/0001_initial.py:
    - Create model User
(djangoEnv) Bryans-MacBook-Pro:assignment_users bryanlockward$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, assignmentuser, auth, contenttypes, sessions
Running migrations:
  Rendering model states... DONE
  Applying assignmentuser.0001_initial... OK
(djangoEnv) Bryans-MacBook-Pro:assignment_users bryanlockward$ python manage.py shell
Python 2.7.13 (default, Jul  6 2017, 09:16:05)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from apps.assignmentuser.models import User

>>> User.objects.create(first_name="Bryan",last_name="Lockward",email="email@aol.com",age=25)
<User: User object>

>>> User.objects.create(first_name="Bryan",last_name="Lockward",email="email@aol.net",age=25)
<User: User object>

>>> User.objects.create(first_name="Brn",last_name="Lock",email="ail@aol.com",age=25)
<User: User object>

>>> User.objects.first()
<User: User object>

>>> User.objects.first().first_name
u'Bryan'

>>> User.objects.last().last_name
u'Lock'

>>> user3=User.objects.get(id=3)
>>> user3.last_name="Changed"
>>> user3.save()
>>> User.objects.last().last_name
u'Changed'

>>> User.objects.get(id=2).delete()
(1, {u'assignmentuser.User': 1})
>>>
