from enum import Enum

from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models

from Book_Talk.web.validators import ImageMaxSizeValidator


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class BookGenres(ChoicesEnum):
    FANTASY = 'Fantasy'
    ADVENTURE = 'Adventure'
    HORROR = 'Horror'


class User(models.Model):
    USERNAME_MIN_LENGTH = 3
    USERNAME_MAX_LENGTH = 30

    EMAIL_MIN_LENGTH = 10

    PASSWORD_MIN_LENGTH = 3
    PASSWORD_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(USERNAME_MIN_LENGTH),
        ]
    )

    email = models.EmailField(
        validators=[
            MinLengthValidator(EMAIL_MIN_LENGTH),
        ]
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        validators=[
            MinLengthValidator(PASSWORD_MIN_LENGTH),
        ]
    )

    def __str__(self):
        return self.username


class Book(models.Model):
    TITLE_MIN_LENGTH = 2
    TITLE_MAX_LENGTH = 30

    AUTHOR_MIN_LENGTH = 5
    AUTHOR_MAX_LENGTH = 30

    REVIEW_MAX_LENGTH = 30

    REVIEW_MIN_LENGTH = 10
    GENRE_MAX_LENGTH = 30

    IMAGE_MAX_SIZE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
        ]
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH,
        validators=[
            MinLengthValidator(AUTHOR_MIN_LENGTH),
        ]
    )

    image = models.ImageField(
        upload_to='book_images',
        validators=[
            ImageMaxSizeValidator(IMAGE_MAX_SIZE),
        ]
    )

    review = models.TextField(
        max_length=REVIEW_MAX_LENGTH,
        validators=[
            MinLengthValidator(REVIEW_MIN_LENGTH),
        ]
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=BookGenres.choices(),
    )

    stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    wishing_list = models.ManyToManyField(
        to=User,
        related_name='wishing_list')

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
