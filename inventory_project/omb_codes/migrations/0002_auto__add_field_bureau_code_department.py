# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bureau_Code.department'
        db.add_column(u'omb_codes_bureau_code', 'department',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bureau_Code.department'
        db.delete_column(u'omb_codes_bureau_code', 'department')


    models = {
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
        }
    }

    complete_apps = ['omb_codes']