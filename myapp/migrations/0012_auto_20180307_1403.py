# Generated by Django 2.0.1 on 2018-03-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20180307_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disabilityinfo',
            old_name='listen_skill',
            new_name='listen_skill1',
        ),
        migrations.RenameField(
            model_name='disabilityinfo',
            old_name='reading_skill',
            new_name='listen_skill2',
        ),
        migrations.RenameField(
            model_name='disabilityinfo',
            old_name='speaking_skill',
            new_name='listen_skill3',
        ),
        migrations.RenameField(
            model_name='disabilityinfo',
            old_name='writing_skill',
            new_name='listen_skill4',
        ),
        migrations.RemoveField(
            model_name='disabilityinfo',
            name='language',
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='agency_honor',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='hobbies',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=2500, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='honor_name',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='honor_year',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='interesting_work_cate',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=2500, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='language1',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='language2',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='language3',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='language4',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='reading_skill1',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='reading_skill2',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='reading_skill3',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='reading_skill4',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='speaking_skill1',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='speaking_skill2',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='speaking_skill3',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='speaking_skill4',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='writing_skill1',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='writing_skill2',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='writing_skill3',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disabilityinfo',
            name='writing_skill4',
            field=models.CharField(blank=True, default='ไม่ระบุ', max_length=50, null=True),
        ),
    ]
