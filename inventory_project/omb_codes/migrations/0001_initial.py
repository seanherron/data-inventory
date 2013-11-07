# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bureau_Code'
        db.create_table(u'omb_codes_bureau_code', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('agency', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('agency_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bureau_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'omb_codes', ['Bureau_Code'])

        # Adding model 'Program_Code'
        db.create_table(u'omb_codes_program_code', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('program_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('program_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal(u'omb_codes', ['Program_Code'])


    def backwards(self, orm):
        # Deleting model 'Bureau_Code'
        db.delete_table(u'omb_codes_bureau_code')

        # Deleting model 'Program_Code'
        db.delete_table(u'omb_codes_program_code')


    models = {
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
        }
    }

    complete_apps = ['omb_codes']