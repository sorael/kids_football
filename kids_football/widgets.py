# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage


class DatePickerWidget(forms.DateInput):

    def __init__(self, attrs=None):
        super(DatePickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DatePickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
            <script>
                $('#id_%s').datepicker({
                    dateFormat: 'yyyy-mm-dd',
                    position: 'bottom left',
                });
            </script>
            ''' % name)

    class Media:
        css = {
            'all': (staticfiles_storage.url('css/datepicker.min.css'),)
        }
        js = (
            settings.STATIC_URL + 'js/datepicker.min.js',
        )


class DateTimePickerWidget(forms.DateTimeInput):

    def __init__(self, attrs=None):
        super(DateTimePickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DateTimePickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
            <script type="text/javascript">
                $(function () {
                    $('#id_%s').datetimepicker({
                        locale: 'ru'
                    });
                });
            </script>
            ''' % name)

    # class Media:
    #     css = {
    #         'all': (staticfiles_storage.url('css/bootstrap-datetimepicker.min.css'),)
    #     }
    #     js = (
    #         settings.STATIC_URL + 'js/bootstrap.min.js',
    #         settings.STATIC_URL + 'js/moment-with-locales.js',
    #         settings.STATIC_URL + 'js/transition.js',
    #         settings.STATIC_URL + 'js/collapse.js',
    #         settings.STATIC_URL + 'js/bootstrap-datetimepicker.min.js',
    #     )