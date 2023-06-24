# Generated by Django 3.2 on 2023-06-23 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('path', models.ImageField(upload_to='uploads/Banner')),
                ('url', models.CharField(max_length=200)),
                ('position_x', models.DecimalField(decimal_places=4, max_digits=10)),
                ('position_y', models.DecimalField(decimal_places=4, max_digits=10)),
                ('position_z', models.DecimalField(decimal_places=4, max_digits=10)),
                ('rotation', models.DecimalField(decimal_places=4, max_digits=10)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition_Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False, max_length=40)),
                ('model_link', models.CharField(default='/model/', max_length=100)),
                ('poster', models.FileField(default='uploads/Poster/eyrcs2023.png', upload_to='uploads/Poster')),
                ('exhibition_front_view', models.FileField(default='uploads/Exhibition_front_view/eyrcs2023.png', upload_to='uploads/Exhibition_front_view')),
                ('description', models.TextField()),
                ('explanation_video_link', models.CharField(default='/', max_length=100)),
                ('research_paper', models.FileField(default='uploads/Poster/eyrcs2023.png', upload_to='uploads/Research_Paper')),
                ('animation_video', models.FileField(default='uploads/Poster/eyrcs2023.png', upload_to='uploads/Animation_Video')),
                ('exhibit_model', models.FileField(default='uploads/Poster/eyrcs2023.png', upload_to='uploads/Exhibition_Walls')),
                ('team_members', models.TextField()),
                ('school_name', models.CharField(blank=True, default='', max_length=100)),
                ('category', models.CharField(choices=[('0', 'Country 1'), ('1', 'Country 2'), ('2', 'Country 3'), ('3', 'Country 4'), ('4', 'Country 5')], default='0', max_length=1)),
                ('is_Verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Model_All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(editable=False, max_length=40)),
                ('modellink', models.FileField(upload_to='uploads/Models')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.DecimalField(decimal_places=4, max_digits=10)),
                ('position_y', models.DecimalField(decimal_places=4, max_digits=10)),
                ('position_z', models.DecimalField(decimal_places=4, max_digits=10)),
                ('label', models.IntegerField()),
                ('text', models.CharField(max_length=100)),
                ('audiolink', models.FileField(upload_to='uploads/Models/Points')),
                ('model_link', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='symposium.model_all')),
            ],
        ),
        migrations.CreateModel(
            name='NavLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symposium.event')),
            ],
        ),
    ]