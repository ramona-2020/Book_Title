from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

IMAGE_MAX_SIZE_ERROR_MESSAGE = "Image size must be lower than or equal to %s"


@deconstructible
class ImageMaxSizeValidator:
    def __init__(self, image_max_size):
        self.image_max_size = image_max_size

    def __call__(self, image):
        image_file_size_in_bytes = image.size
        max_file_size_in_bytes = self.image_max_size * 1024 * 1024
        if image_file_size_in_bytes > max_file_size_in_bytes:
            raise ValidationError(
                IMAGE_MAX_SIZE_ERROR_MESSAGE % {self.image_max_size}
            )

