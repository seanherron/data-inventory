# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'datasets_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'datasets', ['Tag'])

        # Adding model 'Category'
        db.create_table(u'datasets_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'datasets', ['Category'])

        # Adding model 'Dataset'
        db.create_table(u'datasets_dataset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('last_update', self.gf('django.db.models.fields.DateField')()),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publishers.Publisher'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('unique_identifer', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
            ('public_access_level', self.gf('django.db.models.fields.CharField')(default='public', max_length=50)),
            ('bureau_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['omb_codes.Bureau_Code'], null=True, blank=True)),
            ('program_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['omb_codes.Program_Code'], null=True, blank=True)),
            ('access_level_comment', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('endpoint', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('license', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['licenses.License'], null=True, blank=True)),
            ('spatial', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('temporal_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('temporal_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_dictionary', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('data_quality', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('landing_page', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('uii', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('release_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sorn', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'datasets', ['Dataset'])

        # Adding M2M table for field tags on 'Dataset'
        m2m_table_name = db.shorten_name(u'datasets_dataset_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dataset', models.ForeignKey(orm[u'datasets.dataset'], null=False)),
            ('tag', models.ForeignKey(orm[u'datasets.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dataset_id', 'tag_id'])

        # Adding M2M table for field categories on 'Dataset'
        m2m_table_name = db.shorten_name(u'datasets_dataset_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dataset', models.ForeignKey(orm[u'datasets.dataset'], null=False)),
            ('category', models.ForeignKey(orm[u'datasets.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dataset_id', 'category_id'])

        # Adding M2M table for field languages on 'Dataset'
        m2m_table_name = db.shorten_name(u'datasets_dataset_languages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dataset', models.ForeignKey(orm[u'datasets.dataset'], null=False)),
            ('language', models.ForeignKey(orm[u'languages.language'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dataset_id', 'language_id'])

        # Adding model 'RelatedDocuments'
        db.create_table(u'datasets_relateddocuments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasets.Dataset'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'datasets', ['RelatedDocuments'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'datasets_tag')

        # Deleting model 'Category'
        db.delete_table(u'datasets_category')

        # Deleting model 'Dataset'
        db.delete_table(u'datasets_dataset')

        # Removing M2M table for field tags on 'Dataset'
        db.delete_table(db.shorten_name(u'datasets_dataset_tags'))

        # Removing M2M table for field categories on 'Dataset'
        db.delete_table(db.shorten_name(u'datasets_dataset_categories'))

        # Removing M2M table for field languages on 'Dataset'
        db.delete_table(db.shorten_name(u'datasets_dataset_languages'))

        # Deleting model 'RelatedDocuments'
        db.delete_table(u'datasets_relateddocuments')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datasets.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'datasets.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'access_level_comment': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'bureau_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['omb_codes.Bureau_Code']", 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['datasets.Category']", 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'data_dictionary': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'data_quality': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'endpoint': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landing_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['languages.Language']", 'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['licenses.License']", 'null': 'True', 'blank': 'True'}),
            'program_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['omb_codes.Program_Code']", 'null': 'True', 'blank': 'True'}),
            'public_access_level': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '50'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishers.Publisher']"}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sorn': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'spatial': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['datasets.Tag']", 'null': 'True', 'blank': 'True'}),
            'temporal_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'temporal_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uii': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'unique_identifer': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'datasets.relateddocuments': {
            'Meta': {'object_name': 'RelatedDocuments'},
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datasets.Dataset']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'datasets.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'languages.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('languages.fields.LanguageField', [], {'max_length': '7'})
        },
        u'licenses.license': {
            'Meta': {'object_name': 'License'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'omb_codes.bureau_code': {
            'Meta': {'object_name': 'Bureau_Code'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'agency_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'bureau_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'omb_codes.program_code': {
            'Meta': {'object_name': 'Program_Code'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'program_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'publishers.publisher': {
            'Meta': {'object_name': 'Publisher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['datasets']