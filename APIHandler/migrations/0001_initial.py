# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Caracteristic'
        db.create_table(u'APIHandler_caracteristic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'APIHandler', ['Caracteristic'])

        # Adding model 'Product'
        db.create_table(u'APIHandler_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'APIHandler', ['Product'])

        # Adding M2M table for field caracteristics on 'Product'
        m2m_table_name = db.shorten_name(u'APIHandler_product_caracteristics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'APIHandler.product'], null=False)),
            ('caracteristic', models.ForeignKey(orm[u'APIHandler.caracteristic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'caracteristic_id'])

        # Adding model 'User'
        db.create_table(u'APIHandler_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'APIHandler', ['User'])

        # Adding M2M table for field boughtProducts on 'User'
        m2m_table_name = db.shorten_name(u'APIHandler_user_boughtProducts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'APIHandler.user'], null=False)),
            ('product', models.ForeignKey(orm[u'APIHandler.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Caracteristic'
        db.delete_table(u'APIHandler_caracteristic')

        # Deleting model 'Product'
        db.delete_table(u'APIHandler_product')

        # Removing M2M table for field caracteristics on 'Product'
        db.delete_table(db.shorten_name(u'APIHandler_product_caracteristics'))

        # Deleting model 'User'
        db.delete_table(u'APIHandler_user')

        # Removing M2M table for field boughtProducts on 'User'
        db.delete_table(db.shorten_name(u'APIHandler_user_boughtProducts'))


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