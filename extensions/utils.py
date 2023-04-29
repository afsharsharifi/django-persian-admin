import os
import random
import uuid


def get_extension_file(filename):
    return os.path.splitext(filename)[-1]


def create_profile_image_path(instance, filename):
    extension = get_extension_file(filename)
    num_id = uuid.uuid1()
    return f"profiles/{num_id}{extension}"


def create_department_image_path(instance, filename):
    extension = get_extension_file(filename)
    num_id = uuid.uuid1()
    return f"departments/{num_id}{extension}"


def create_attachment_path(instance, filename):
    extension = get_extension_file(filename)
    num_id = uuid.uuid1()
    return f"attachments/{num_id}{extension}"


def generate_otp(length=6):
    result = ""
    for i in range(length):
        result += str(random.randint(1, 9))
    return result
