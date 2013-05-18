from django.db import models

import os

class AutoDeleteFileField(models.FileField):
    """
        A FileField with additional functionality to remove the file on
        update/remove of the file from the database.
    """
    def save_form_data(self, instance, data):
        old_data = getattr(instance,self.attname)
        # Delete the file if updated
        if (data == False and old_data != False) or \
                (data != old_data and old_data != ''):
            file_name = settings.STATIC_ROOT + str(getattr(
                                getattr(instance,self.name),'name'))
            if os.path.exists(file_name):
                os.remove(file_name)
        super(AutoDeleteFileField, self).save_form_data(instance, data)


