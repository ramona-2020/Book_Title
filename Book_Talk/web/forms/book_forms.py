import os

from django import forms

from Book_Talk.web.models import Book


class BookBaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'box'

            if _ == 'review':
                field.widget.attrs['rows'] = 0
                field.widget.attrs['cols'] = 0

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'stars', 'image', 'review',)


class BookCreateReviewForm(BookBaseForm):
    pass


class BookEditReviewForm(BookBaseForm):
    pass


class BookDeleteReviewForm(BookBaseForm):

    def __form_fields_disabled(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__form_fields_disabled()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            image_path = self.instance.image.path
            os.remove(image_path)

        return self.instance

