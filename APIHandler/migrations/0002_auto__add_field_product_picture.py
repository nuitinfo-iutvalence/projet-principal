# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.picture'
        db.add_column(u'APIHandler_product', 'picture',
                      self.gf('django.db.models.fields.files.ImageField')(default='BOUHAHAH', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.picture'
        db.delete_column(u'APIHandler_product', 'picture')


    models = {
        u'APIHandler.caracteristic': {
            'Meta': {'object_name': 'Caracteristic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'APIHandler.product': {
            'Meta': {'object_name': 'Product'},
            'caracteristics': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'products'", 'symmetrical': 'False', 'to': u"orm['APIHandler.Caracteristic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'APIHandler.user': {
            'Meta': {'object_name': 'User'},
            'boughtProducts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'User'", 'symmetrical': 'False', 'to': u"orm['APIHandler.Product']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['APIHandler']