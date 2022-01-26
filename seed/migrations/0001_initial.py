from django.db import migrations
from user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(u_name="admin",
                            email='admin@gmail.com',
                            is_staff=True,
                            is_superuser=True,
                            phone='9825119218',
                            gender = "Female"

                            )

        user.set_password('12345')
        user.save()


    dependencies = [

    ]
    operations = [
        migrations.RunPython(seed_data),
        
    ]
