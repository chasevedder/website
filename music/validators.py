def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.split(value.name)[1]
    valid_extensions = ['jpg', 'jpeg', 'png', 'bmp']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')