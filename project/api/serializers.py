from project.models import Project, Stage, Task
from authapp.models import User
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True, allow_empty_file=True, max_length=254)
    url = serializers.HyperlinkedIdentityField(view_name='project:project-detail')
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
        slug_tmp = validated_data.pop('slug')

        project = Project(

            name=validated_data['name'],
            description=validated_data['description'],
            date_end=validated_data['date_end'],
            is_active=validated_data['is_active'],
            image=validated_data['image'],
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
        view_name='project:project-detail'
    )

    class Meta:
        model = Stage
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project:task-detail')
    id_project = serializers.HyperlinkedRelatedField(
        label='Название проекта',
        queryset=Project.objects.all(),
        view_name='project:project-detail'
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
