from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

USER_TYPES = (
    ("CUSTOMER", "CUSTOMER"),
    ("STAFF", "STAFF"),
)

ATTEND_STATS = (
    ("YET", "YET"),
    ("YES", "YES"),
    ("NO","NO"),
)

phone_number_regex = RegexValidator(
    regex=r"^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$",
    message="Please enter a valid 10/11 digit mobile number.",
    code="invalid_mobile",
)


class User(AbstractUser):
    role = models.CharField(max_length=50, choices=USER_TYPES, default=USER_TYPES[0][0])
    email = models.EmailField("email address", unique=True)
    phone = models.CharField(
        max_length=14, validators=[phone_number_regex], null=True, blank=True
    )
    date_of_birth = models.DateField(editable=True, null=True, blank=True)
    aadhaar_no = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.username}"


class Site(models.Model):
    name = models.CharField(max_length=150)
    crowd_status = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=300)
    open_time = models.TimeField()
    close_time = models.TimeField()
    max_tickets = models.IntegerField()
    phone = models.CharField(
        max_length=14, validators=[phone_number_regex], null=True, blank=True
    )
    ticket_price_per_head = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    # email = models.EmailField("email address", unique=True)
    # time_per_visit = models.TimeField()


class Ticket(models.Model):
    ticket_str = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, blank=True)
    booked_date = models.DateTimeField(auto_now=True)
    visit_date = models.DateField(null=True, blank=True)
    attend_status = models.CharField(max_length=10, choices=ATTEND_STATS, default=ATTEND_STATS[0][0])
    count = models.IntegerField(null=True, blank=True)
