from django.core.management import BaseCommand
from main.models import Category


class Command(BaseCommand):
	def handle (self, *args, **options):
		category_list =[
			{
				'product_category': 'Инструменты ручные',
				'description': 'Пассатижи, отвертки, клещи',
				'is_active': True
			},
			{
				'product_category': 'Письменные принаджежности',
				'description': 'тетрадки, блокноты, бумага',
				'is_active': True
			},
			{
				'product_category': 'Печатная продукция',
				'description': 'Журналы, газеты, книги, энциклопедии',
				'is_active': False
			},
			{
				'product_category': 'Электронные издания',
				'description': 'Художественная литература, Проза, Журналистика, Историчесские эссе',
				'is_active': True
			},

		]
		category_objects =[]
		for category_item in category_list:
			category_objects.append(
				Category(**category_item)
			)
		Category.objects.bulk_create(category_objects)