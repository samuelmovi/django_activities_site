"""
Feed new contacts:

from my_site.models import Contact

all_contacts = [
	{
		'name': 'email',
		'link': '#',
		'text': 'Email',
		'icon': 'fa fa-envelope',
	},
	{
		'name': 'linkedin',
		'link': '#',
		'text': 'LinkedIn',
		'icon': 'fa fa-linkedin-square',
	},
	{
		'name': 'instagram',
		'link': '#',
		'text': 'Instagram',
		'icon': 'fa fa-linkedin',
	},
	{
		'name': 'facebook',
		'link': '#',
		'text': 'Facebook',
		'icon': 'fa fa-facebook-square',
	},
	{
		'name': 'twitter',
		'link': '#',
		'text': 'Twitter',
		'icon': 'fa fa-twitter',
	},
	{
		'name': 'telephone',
		'link': 'tel:#',
		'text': 'Telefono',
		'icon': 'fa fa-phone-square',
	},
	{
		'name': 'whatsapp',
		'link': 'https://wa.me/#',
		'text': 'WhatsApp',
		'icon': 'fa fa-whatsapp',
	},
]

for contact in all_contacts:
	print("[#] Processing: {}".format(contact['name']))
	new_contact = Contact()
	for key in contact.keys():
		new_contact.__dict__[key] = contact[key]
	new_contact.save()
	print("\t> {} saved".format(contact['name']))


"""

"""
Feed new pages:

from my_site.models import Page


all_pages = [
	{
		'name': 'home',
		'title': 'Welcome',
		'text': 'Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, Welcome Text, ',
		'lang': 'en',
	},
	{
		'name': 'Inicio',
		'title': 'Bienvenidos',
		'text': 'Texto de bienvenida, Texto de bienvenida, Texto de bienvenida, Texto de bienvenida, Texto de bienvenida, Texto de bienvenida, Texto de bienvenida, ',
		'lang': 'es',
	},
	{
		'name': 'About me',
		'title': 'About Me',
		'text': 'Me me me me , Me me me me , Me me me me , Me me me me , Me me me me , Me me me me , Me me me me , Me me me me , ',
		'lang': 'en',
	},
	{
		'name': 'Sobre mi',
		'title': 'Sobre mi',
		'text': 'Mi mi mi mi , Mi mi mi mi , Mi mi mi mi , Mi mi mi mi , Mi mi mi mi , Mi mi mi mi , Mi mi mi mi , Mi mi mi mi , ',
		'lang': 'es',
	},

for page in all_pages:
	print("[#] Processing: {}".format(page['name']))
	new_page = Page()
	for key in page.keys():
		new_page.__dict__[key] = page[key]
	new_page.save()
	print("\t> {} saved".format(page['name']))

"""


"""
For new Activities:
"""
from my_site.models import Activity

all_activities = [
    {
        'name': 'activity name',
        'title': 'activity title',
        'type': 'My type',
        'summary': "<p>Summary summ sum,  Summary summ sum,  Summary summ sum,  Summary summ sum,  </p>",
        'details': "<ul><li>Schedule: </li><li>Duration:</li><li>Price: </li><li>Includes:</li><li>Group size: </li><li>Meeting point: </li></ul>",
        'lang': 'en',
    },
        {
        'name': 'nombre de actividad',
        'title': 'título de actividad',
        'type': 'Mi tipo',
        'summary': "<p>Resumen resumen ,  Resumen resumen ,Resumen resumen ,Resumen resumen </p>",
        'details': "<ul><li>Horario: </li><li>Duración:</li><li>Precio: </li><li>Incluido:</li><li>Group size:	</li><li>Punto de encuentro: </li></ul>",
        'lang': 'es',
    },

]

for activity in all_activities:
    print("[#] Processing: {}".format(activity['name']))
    new_activity = Activity()
    for key in activity.keys():
        new_activity.__dict__[key] = activity[key]
    new_activity.save()
    print("\t> {} saved".format(activity['name']))




"""
For new excertps:

from my_site.models import Excerpt

all_excerpts = [
    {
        'name': 'activity name',
        'title': 'excerpt title',
        'text': "<p>Excerpt from the activity</p>",
        'link': "#",
        'lang': 'en',
    },
        {
        'name': 'nombre de actividad',
        'title': 'titulo de extracto',
        'text': "<p>Extracto de la actividad</p>",
        'link': "#",
        'lang': 'es',
    },
]

for excerpt in all_excerpts:
    print("[#] Processing: {}".format(excerpt['name']))
    new_experience = Excerpt()
    for key in excerpt.keys():
        new_experience.__dict__[key] = excerpt[key]
    new_experience.save()
    print("\t> {} saved".format(excerpt['name']))


"""
