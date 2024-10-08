# Generated by Django 5.0.4 on 2024-09-16 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('profile', models.ImageField(upload_to='profiles/')),
                ('nationality', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('aadhar', models.CharField(max_length=12)),
                ('aadhar_photo', models.ImageField(upload_to='aadhar_photos/')),
                ('emailid', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('guardian_name', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('guardiancontact', models.CharField(max_length=15)),
                ('agecategory', models.CharField(choices=[('boys_under-15', 'Boys under 15'), ('boys_under-19', 'Boys under 19'), ('men_under-23', 'Men Under 23'), ('men_senior', 'Men Senior')], max_length=20)),
                ('position', models.CharField(choices=[('batsmen', 'Batsmen'), ('bowler', 'Bowler'), ('wicketkeeper', 'Wicketkeeper'), ('all_rounder', 'All Rounder')], max_length=20)),
                ('role', models.CharField(max_length=100)),
                ('handiness', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=100)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.team')),
            ],
        ),
    ]
