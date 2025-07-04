# Generated by Django 5.2.3 on 2025-06-14 15:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('montant', models.FloatField(default=0.0)),
                ('montant_initial', models.FloatField(default=0.0)),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actif', models.BooleanField(default=True)),
                ('type_budget', models.CharField(choices=[('D', 'Durée determiner'), ('I', 'Durée non determiner')], default='D', max_length=3)),
                ('bilan_fait', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategorieDepense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('montant', models.FloatField(default=0.0)),
                ('montant_initial', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetManager.budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conseil',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.TextField(default='conseil')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('viewed', models.BooleanField(default=False)),
                ('id_budget', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budgetManager.budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('montant', models.FloatField(default=0.0)),
                ('type_depense', models.CharField(choices=[('DP', 'depense'), ('SL', 'salaires')], default='DP', max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetManager.budget')),
                ('id_cat_depense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='budgetManager.categoriedepense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('adresse', models.TextField(blank=True, null=True)),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('type_employe', models.CharField(choices=[('DIR', 'Direction'), ('CAD', 'Cadre'), ('EMP', 'Employé'), ('OUV', 'Ouvrier'), ('CON', 'Consultant/Freelance'), ('STA', 'Stagiaire/Alternant'), ('INT', 'Intérimaire'), ('AUT', 'Autre')], default='AUT', max_length=3)),
                ('poste', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prise_service', models.DateTimeField(blank=True, null=True)),
                ('img_profil', models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/', verbose_name='Image de profil')),
                ('actif', models.CharField(choices=[('ES', 'En service'), ('EC', 'En congé'), ('ER', 'Retraité'), ('LC', 'Licencié'), ('HS', 'Hors service'), ('DM', 'Démissionné')], default='ES', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entree',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('montant', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetManager.budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MontantSalaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaire_direction', models.FloatField(default=0.0)),
                ('bonus_direction', models.FloatField(default=0.0)),
                ('indemnite_direction', models.FloatField(default=0.0)),
                ('avance_direction', models.FloatField(default=0.0)),
                ('salaire_cadre', models.FloatField(default=0.0)),
                ('bonus_cadre', models.FloatField(default=0.0)),
                ('indemnite_cadre', models.FloatField(default=0.0)),
                ('avance_cadre', models.FloatField(default=0.0)),
                ('salaire_employe', models.FloatField(default=0.0)),
                ('bonus_employe', models.FloatField(default=0.0)),
                ('indemnite_employe', models.FloatField(default=0.0)),
                ('avance_employe', models.FloatField(default=0.0)),
                ('salaire_ouvrier', models.FloatField(default=0.0)),
                ('bonus_ouvrier', models.FloatField(default=0.0)),
                ('indemnite_ouvrier', models.FloatField(default=0.0)),
                ('avance_ouvrier', models.FloatField(default=0.0)),
                ('salaire_cf', models.FloatField(default=0.0)),
                ('bonus_cf', models.FloatField(default=0.0)),
                ('indemnite_cf', models.FloatField(default=0.0)),
                ('avance_cf', models.FloatField(default=0.0)),
                ('salaire_stagiaire', models.FloatField(default=0.0)),
                ('bonus_stagiaire', models.FloatField(default=0.0)),
                ('indemnite_stagiaire', models.FloatField(default=0.0)),
                ('avance_stagiaire', models.FloatField(default=0.0)),
                ('salaire_intermediaire', models.FloatField(default=0.0)),
                ('bonus_intermediaire', models.FloatField(default=0.0)),
                ('indemnite_intermediaire', models.FloatField(default=0.0)),
                ('avance_intermediaire', models.FloatField(default=0.0)),
                ('salaire_autre', models.FloatField(default=0.0)),
                ('bonus_autre', models.FloatField(default=0.0)),
                ('indemnite_autre', models.FloatField(default=0.0)),
                ('avance_autre', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('viewed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaiementEmploye',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('montant', models.FloatField(default=0.0)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('type_paiement', models.CharField(choices=[('SALAIRE', 'Salaire')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetManager.budget')),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgetManager.employe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
