from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(name='Address'),
                migrations.DeleteModel(name='Letting'),
                migrations.DeleteModel(name='Profile'),
            ],
        ),
    ]
