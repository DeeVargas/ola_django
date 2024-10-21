import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0004_pessoa_tipo_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='tipo_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='primeiro_app.tipopessoa'),
        ),
    ]