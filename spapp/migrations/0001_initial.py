# Generated by Django 4.0.3 on 2022-03-14 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=30, null=True)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('verification_status', models.BooleanField(default=False)),
                ('rewarded_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('faculty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spapp.degree')),
            ],
        ),
        migrations.CreateModel(
            name='Validator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('nationality', models.CharField(max_length=10, null=True)),
                ('bio_char', models.CharField(max_length=100, null=True)),
                ('interests', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('website', models.CharField(max_length=12, null=True)),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spapp.major')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_author', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=50)),
                ('published_date', models.DateField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='research', to='spapp.activities')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resonsibility', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='spapp.activities')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internship', to='spapp.activities')),
            ],
        ),
        migrations.CreateModel(
            name='Emphasis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spapp.major')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_service', to='spapp.activities')),
            ],
        ),
        migrations.AddField(
            model_name='activities',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spapp.student'),
        ),
        migrations.AddField(
            model_name='activities',
            name='validator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spapp.validator'),
        ),
        migrations.CreateModel(
            name='AccountRemovalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account_removal_request', to='spapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicRecognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('first_semester', 'First Semester'), ('second_semester', 'Second Semester')], max_length=30)),
                ('gpa', models.FloatField(max_length=3)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_recognition', to='spapp.activities')),
            ],
        ),
    ]
