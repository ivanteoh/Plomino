# -*- coding: utf-8 -*-
#
# File: PlominoColumn.py
#
# Copyright (c) 2008 by ['Eric BREHAULT']
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# Zope Public License (ZPL)
#

__author__ = """Eric BREHAULT <eric.brehault@makina-corpus.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.CMFPlomino.config import PROJECTNAME
from validator import isValidPlominoId

schema = Schema((

    StringField(
        name='id',
        widget=StringField._properties['widget'](
            label="Id",
            description="Column id",
            label_msgid='CMFPlomino_label_column_id',
            description_msgid='CMFPlomino_help_column_id',
            i18n_domain='CMFPlomino',
        ),
        validators=("isValidId", isValidPlominoId),
    ),
    StringField(
        name='SelectedField',
        widget=SelectionWidget(
            label="Fields list",
            description=("Field value to display in the column. "
                "(It does not apply if Formula is provided)."),
#            label_msgid='CMFPlomino_label_FieldType',
#            description_msgid='CMFPlomino_help_FieldType',
#            i18n_domain='CMFPlomino',
        ),
        vocabulary='getFormFields',
    ),
    TextField(
        name='Formula',
        widget=TextAreaWidget(
            label="Formula",
            description="Python code returning the column value.",
            label_msgid='CMFPlomino_label_ColumnFormula',
            description_msgid='CMFPlomino_help_ColumnFormula',
            i18n_domain='CMFPlomino',
        ),
    ),
#    IntegerField(
#        name='Position',
#        widget=IntegerField._properties['widget'](
#            label="Position",
#            description="Position in view",
#            label_msgid='CMFPlomino_label_ColumnPosition',
#            description_msgid='CMFPlomino_help_ColumnPosition',
#            i18n_domain='CMFPlomino',
#        ),
#    ),
    BooleanField(
        name='HiddenColumn',
        default="0",
        widget=BooleanField._properties['widget'](
            label="Hidden column",
            label_msgid='CMFPlomino_label_HiddenColumn',
            i18n_domain='CMFPlomino',
        ),
    ),
    BooleanField(
        name='DisplaySum',
        default="0",
        widget=BooleanField._properties['widget'](
            label="Display column sum",
            label_msgid='CMFPlomino_label_DisplaySum',
            i18n_domain='CMFPlomino',
        ),
    ),
),
)

PlominoColumn_schema = BaseSchema.copy() + \
    schema.copy()


class PlominoColumn(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IPlominoColumn)

    meta_type = 'PlominoColumn'
    _at_rename_after_creation = False

    schema = PlominoColumn_schema

    # Methods
    security.declarePublic('getFormFields')
    def getFormFields(self):
        """ Get a list of all the fields in the database
        """
        fields = []
        for form in self.getParentView().getParentDatabase().getForms():
            fields.append([form.id, '=== ' + form.id + ' ==='])
            fields.extend(
                    [(form.id + '/' + field.id, field.id)
                        for field in form.getFormFields()])
        return fields

    security.declarePublic('getColumnName')
    def getColumnName(self):
        """ Get column name
        """
        return self.id

    security.declarePublic('getParentView')
    def getParentView(self):
        """ Get parent view
        """
        return self.getParentNode()

    security.declarePublic('at_post_edit_script')
    def at_post_edit_script(self):
        """post edit
        """
        v = self.getParentView()
        v.declareColumn(self.getColumnName(), self)
        self.cleanFormulaScripts('column_%s_%s' % (v.id, self.id))
        db = self.getParentDatabase()
        if not db.DoNotReindex:
            db.getIndex().refresh()

    security.declarePublic('at_post_create_script')
    def at_post_create_script(self):
        """ Standard AT post create hook.
        """
        v = self.getParentView()
        v.declareColumn(self.getColumnName(), self)
        db = self.getParentDatabase()
        if not db.DoNotReindex:
            db.getIndex().refresh()

    security.declarePublic('post_validate')
    def post_validate(self, REQUEST=None, errors=None):
        """Ensure a field, not a form is selected"""
        form = REQUEST.form
        if errors is None:
            errors = {}
        SelectedField = form.get('SelectedField', None)
        fieldpath = SelectedField.split('/')
        if len(fieldpath) != 2:
            errors['SelectedField'] = u'You must select a field, and not a form'
        return errors

registerType(PlominoColumn, PROJECTNAME)
# end of class PlominoColumn
