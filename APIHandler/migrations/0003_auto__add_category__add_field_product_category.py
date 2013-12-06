# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'APIHandler_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('parent_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['APIHandler.Category'])),
        ))
        db.send_create_signal(u'APIHandler', ['Category'])

        # Adding field 'Product.category'
        db.add_column(u'APIHandler_product', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='0', to=orm['APIHandler.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'APIHandler_category')

        # Deleting field 'Product.category'
        db.delete_column(u'APIHandler_product', 'category_id')


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
            'parent_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['APIHandler.Category']"})
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
