from project.models import Project, Stage, Task
from authapp.models import User
from rest_framework import serializers
from django.utils.text import slugify


def transliterate_ru_en(string):
    ru_en_alphabet = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sh',
        'ы': 'y',
        'э': 'e',
        'ю': 'u',
        'я': 'ya',
        'ь': '',
        'ъ': ''
    }
    symbols_ru = list(string.lower())
    symbols_en = []
    for symbol in symbols_ru:
        if symbol in ru_en_alphabet:
            symbols_en.append(ru_en_alphabet[symbol])
        else:
            symbols_en.append(symbol)
    return ''.join(symbols_en)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True, allow_empty_file=True, max_length=None, required=False)
    url = serializers.HyperlinkedIdentityField(view_name='project:project-detail', lookup_field='slug')
    users = serializers.HyperlinkedRelatedField(
        label='Ползователи',
        queryset=User.objects.all(),
        view_name='api:user-detail',
        many=True
    )

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('slug')
        slug_tmp = slugify(transliterate_ru_en(validated_data['name']), allow_unicode=True)

        project = Project(

            name=validated_data['name'],
            description=validated_data['description'],
            date_end=validated_data['date_end'],
            is_active=validated_data['is_active'],
        )

        slug_tmp_num = slug_tmp + '_'
        if Project.objects.filter(slug=slug_tmp):

            if Project.objects.filter(slug__iregex=slug_tmp_num + r'[0-9]'):
                last_slug = Project.objects.filter(slug__iregex=slug_tmp_num + r'[0-9]').order_by('-id')[:1][0]
                last_slug_name = last_slug.slug
                last_digits_in_last_slag_name = ''.join(list(last_slug_name)[len(list(slug_tmp_num)):])
                new_slug_digit = int(last_digits_in_last_slag_name) + 1
                project.slug = (slug_tmp_num + str(new_slug_digit))

            else:
                project.slug = slug_tmp_num + '1'

        else:
            project.slug = slug_tmp

        try:
            project.image = validated_data['image']
        except KeyError:
            pass

        project.save()

        many_to_many = {'users': validated_data['users']}
        for field_name, value in many_to_many.items():
            field = getattr(project, field_name)
            field.set(value)
        return project


class StageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project:stage-detail')
    id_project = serializers.HyperlinkedRelatedField(
        label='Название проекта',
        queryset=Project.objects.all(),
        view_name='project:project-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Stage
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project:task-detail')
    id_project = serializers.HyperlinkedRelatedField(
        label='Название проекта',
        queryset=Project.objects.all(),
        view_name='project:project-detail',
        lookup_field='slug'
    )

    id_stage = serializers.HyperlinkedRelatedField(
        label='Название этапа',
        queryset=Stage.objects.all(),
        view_name='project:stage-detail'
    )

    id_user = serializers.HyperlinkedRelatedField(
        label='Ползователи',
        queryset=User.objects.all(),
        view_name='api:user-detail'
    )

    class Meta:
        model = Task
        fields = '__all__'
