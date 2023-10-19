# Generated by Django 3.2.16 on 2023-10-18 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(help_text='Relative url of documentation base url that will be used to autofetch the content and also will be used as "Visit our documentation" button.', max_length=128, verbose_name='Relative Documentation Url')),
                ('anchor', models.CharField(blank=True, help_text='Anchor of block on the page on the documentation. This will be used as a start or the content.If the anchor is not provided, it will use whole content.', max_length=128, null=True)),
                ('thumbnail', models.ImageField(blank=True, help_text='If no thumbnail is provided, it will use the first image in the help page under the anchor specified above will be used. We recommend to normally leave this blank', null=True, upload_to='docs/icons')),
                ('title', models.CharField(blank=True, help_text='If no title is provided, it will use the title of the anchor on documentation page.', max_length=512, null=True)),
                ('description', models.TextField(blank=True, help_text='If no description is provided, it will use the first paragraph from the help center under the anchor specified above will be used. We recommend to normally leave this blank', null=True)),
            ],
            options={
                'ordering': ('anchor',),
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Page name that will be used for frontend help center.', max_length=512, unique=True)),
                ('relative_url', models.CharField(blank=True, help_text='Relative page url as identifier to be matched for the page that are opened. Example: put `/project`, it will use this page as help center when we are in /project.', max_length=128, null=True, verbose_name='Relative Page Url')),
                ('url', models.CharField(help_text='Relative url of documentation base url that will be used as "Visit our documentation" button.', max_length=128, verbose_name='Relative Documentation Url')),
                ('title', models.CharField(help_text='Title that will be used on the page help center.', max_length=512)),
                ('intro', models.TextField(blank=True, help_text='Help intro for this page help center, below title and upper of blocks.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentation_base_url', models.CharField(default='https://documentation/', max_length=512)),
            ],
            options={
                'verbose_name_plural': 'preferences',
            },
        ),
        migrations.CreateModel(
            name='PageBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs_crawler.block')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs_crawler.page')),
            ],
        ),
        migrations.CreateModel(
            name='BlockChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_children', to='docs_crawler.block')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs_crawler.block')),
            ],
        ),
    ]
