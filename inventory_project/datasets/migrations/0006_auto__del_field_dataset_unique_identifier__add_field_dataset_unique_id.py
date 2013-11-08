# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Dataset.unique_identifier'
        db.delete_column(u'datasets_dataset', 'unique_identifier')

        # Adding field 'Dataset.unique_identifer'
        db.add_column(u'datasets_dataset', 'unique_identifer',
                      self.gf('uuidfield.fields.UUIDField')(default=1, unique=True, max_length=32, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Dataset.unique_identifier'
        db.add_column(u'datasets_dataset', 'unique_identifier',
                      self.gf('uuidfield.fields.UUIDField')(default=1, max_length=32, unique=True, blank=True),
                      keep_default=False)

        # Deleting field 'Dataset.unique_identifer'
        db.delete_column(u'datasets_dataset', 'unique_identifer')


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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['datasets.Tag']", 'symmetrical': 'False'}),
            'temporal_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'temporal_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uii': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'unique_identifer': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'datasets.relateddocument': {
            'Meta': {'object_name': 'RelatedDocument'},
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
            'department': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
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