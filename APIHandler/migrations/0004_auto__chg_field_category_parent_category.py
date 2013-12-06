# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.parent_category'
        db.alter_column(u'APIHandler_category', 'parent_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['APIHandler.Category'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Category.parent_category'
        raise RuntimeError("Cannot reverse this migration. 'Category.parent_category' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Category.parent_category'
        db.alter_column(u'APIHandler_category', 'parent_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['APIHandler.Category']))

    models = {
        u'APIHandler.caracteristic': {
            'Meta': {'object_name': 'Caracteristic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'APIHandler.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'parent_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['APIHandler.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'APIHandler.product': {
            'Meta': {'object_name': 'Product'},
            'caracteristics': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'products'", 'symmetrical': 'False', 'to': u"orm['APIHandler.Caracteristic']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['APIHandler.Category']"}),
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