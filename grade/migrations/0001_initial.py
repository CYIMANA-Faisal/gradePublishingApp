# Generated by Django 3.2 on 2021-12-10 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(choices=[('cat', 'cat'), ('exam', 'quiz')], default='cat', max_length=50)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]