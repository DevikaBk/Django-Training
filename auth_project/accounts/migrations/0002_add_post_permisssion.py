from django.db import migrations

def create_permission(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    CustomUser = apps.get_model('accounts', 'CustomUser')
    
    content_type = ContentType.objects.get_for_model(CustomUser)
    Permission.objects.get_or_create(
        codename='add_post',
        name='Can add post',
        content_type=content_type,
    )

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),  # Your initial migration
    ]

    operations = [
        migrations.RunPython(create_permission),
    ]