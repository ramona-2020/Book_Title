from django import template

from Book_Talk.web.models import User

register = template.Library()


@register.simple_tag
def user_profile():
    return User.objects.first()
