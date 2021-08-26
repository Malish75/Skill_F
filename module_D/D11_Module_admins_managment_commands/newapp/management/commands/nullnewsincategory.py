from django.core.management.base import BaseCommand, CommandError
from newapp.models import Category, Post, PostCategory

# py manage.py nullnewsincategory здоровье
class Command(BaseCommand):
    help = 'Удаляет все новости из указанной категории. Пример ввода: py manage.py nullnewsincategory здоровье погода'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    missing_args_message = 'Недостаточно аргументов'
    requires_migrations_checks = False # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('categories_for_delete',
                            nargs='+',
                            type=str,
                            )

    def handle(self, *args, **options):
        # код, который выполняется при вызове команды
        self.stdout.readable()
        self.stdout.write('Действительно удалить все публикации в категории? yes/no')
        answer = input()  # считываем подтверждение

        if answer == 'yes':  # в случае подтверждения действительно удаляем все товары
            allcategories = Category.objects.all()                 # {'id': 1, 'category_name': 'здоровье'}
            allpostcategory = PostCategory.objects.all().values()  # {'id': 216, 'post_id': 458, 'category_id': 1}
            # allposts = Post.objects.all()                          # {'id': 458, 'new_post': 'PO', .......
            for c_f_d in options['categories_for_delete']:
                for item in allcategories.values():
                    if item['category_name'] == c_f_d:  # c_f_d - то что идет аргументом в команде - здоровье, спорт
                        pk_categ = item['id']                 # берем id указаной категории

                        # далее из PostCategory по ид категории узнаем ид поста для удаления
                        for item in allpostcategory:
                            if item['category_id'] == pk_categ:
                                pk_post = item['post_id'] # узнали ид поста для удаления, через PostCategory

                                # удаление
                                Post.objects.get(id=pk_post).delete()
                                print(f'пост с ид={pk_post} удален')

                self.stdout.write(self.style.SUCCESS(f"Публикации в категории {c_f_d} удалены успешно!"))
            return

        self.stdout.write(self.style.ERROR('Ошибка ввода или отмена удаления публикаций.'))  # в случае неправильного подтверждения, говорим что в доступе отказано





'''

def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')
 
        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
 
        try:
            category = Category.get(name=options['category'])
            Article.objects.filter(category__name==category.name).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}')) # в случае неправильного подтверждения, говорим что в доступе отказано
        except Article.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {}'))



>>> posts_category = PostCategory.objects.all().values()
>>> posts_category
<QuerySet [{'id': 216, 'post_id': 434, 'category_id': 8}, {'id': 217, 'post_id': 435, 'category_id': 8}, {'id': 218, 'post_id': 436, 'category_id': 8}, {'id': 219, 'post_id': 437, '
category_id': 2}, {'id': 220, 'post_id': 438, 'category_id': 1}, {'id': 221, 'post_id': 439, 'category_id': 6}, {'id': 238, 'post_id': 457, 'category_id': 1}, {'id': 239, 'post_id':
 458, 'category_id': 3}]>

>>> name_cat = Category.objects.all().values()
>>> name_cat
<QuerySet [{'id': 1, 'category_name': 'здоровье'}, {'id': 2, 'category_name': 'спорт'}, {'id': 3, 'category_name': 'интересное'}, {'id': 4, 'category_name': 'в мире'}, {'id': 5, 'ca
tegory_name': 'наука'}, {'id': 6, 'category_name': 'кино'}, {'id': 7, 'category_name': 'погода'}, {'id': 8, 'category_name': 'IT'}]>
>>>

'''
