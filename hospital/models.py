from django.db import models


# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(null=True)


class Department(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    speciality = models.ForeignKey("Speciality", on_delete=models.CASCADE, related_name="doctors")
    photo = models.ImageField(null=True)
    about = models.TextField()
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="doctors")


class Price(models.Model):
    title = models.CharField(max_length=255)
    annual_price = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    photo = models.ImageField(null=True)


class FeedBack(models.Model):
    author = models.CharField(max_length=255)
    profession = models.CharField(max_length=255, null=True)
    content = models.TextField()
    photo = models.ImageField()


class SocialLink(models.Model):
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True)


class DoctorContact(models.Model):
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="doctorContacts")
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True)


class Speciality(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, related_name="appointments")
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    appointment_time = models.DateTimeField("appointment time")


class Blog(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="blogs")
    viewers = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE, related_name="blogs")


class Comment(models.Model):
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    content = models.TextField()


class BlogCategory(models.Model):
    title = models.TextField()


class User(models.Model):
    first_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
