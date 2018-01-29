# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 06:20
from __future__ import unicode_literals

import ckeditor.fields
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
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('th_name', models.CharField(max_length=100)),
                ('en_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(default='ไม่ระบุ', max_length=20)),
                ('address', models.CharField(default='ไม่ระบุ', max_length=5000)),
                ('info', models.CharField(default='ไม่ระบุ', max_length=5000)),
                ('website', models.CharField(default='ไม่ระบุ', max_length=50)),
                ('fax', models.CharField(max_length=30)),
                ('company_type', models.CharField(max_length=100)),
                ('get_more_info', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DisabilityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.CharField(default='ไม่ระบุ', max_length=20)),
                ('address', models.CharField(blank=True, default='ไม่ระบุ', max_length=5000, null=True)),
                ('disability_cate', models.CharField(max_length=100)),
                ('job_interest', models.CharField(max_length=100)),
                ('job_exp', models.CharField(default='', max_length=5000)),
                ('expected_salary1', models.IntegerField(blank=True, null=True)),
                ('expected_salary2', models.IntegerField(blank=True, null=True)),
                ('expected_welfare', models.CharField(max_length=1000)),
                ('talent', models.CharField(max_length=1000)),
                ('talent2', models.CharField(default='', max_length=1000)),
                ('talent3', models.CharField(default='', max_length=1000)),
                ('province', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('more_resume', models.FileField(blank=True, default=None, null=True, upload_to='resume/')),
                ('get_more_info', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InviteProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ยังไม่ส่งคำเชิญ', 'ยังไม่ส่งคำเชิญ'), ('ส่งคำเชิญ', 'ส่งคำเชิญ'), ('ตอบรับคำเชิญ', 'ตอบรับคำเชิญ'), ('สมัครงาน', 'สมัครงาน')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('disability', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.DisabilityInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_th', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('age1', models.IntegerField(blank=True, null=True)),
                ('age2', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('detail', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('phone_no', models.CharField(default='ไม่ระบุ', max_length=20)),
                ('disability_cate', models.CharField(max_length=100)),
                ('salary1', models.IntegerField(blank=True, null=True)),
                ('salary2', models.IntegerField(blank=True, null=True)),
                ('qualification', models.CharField(blank=True, max_length=5000, null=True)),
                ('province', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('address', models.CharField(default='ไม่ระบุ', max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.CompanyInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=20)),
                ('obj', models.CharField(blank=True, max_length=200, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('message', models.CharField(blank=True, max_length=5000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='', upload_to='profilePicture/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('tarket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Profile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='tarket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Profile'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inviteprocess',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Job'),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Profile'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Profile'),
        ),
    ]