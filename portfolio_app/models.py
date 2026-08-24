import typing
import uuid

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise ValueError("Superusers must have a password.")

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with this email already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether this user can log into the admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    objects = CustomAccountManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"


class Technology(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class KeyFeature(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()

    def __str__(self):
        return self.title


class Challenge(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()

    def __str__(self):
        return self.title


class Impact(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()

    def __str__(self):
        return self.title


class Industry(models.Model):
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.name


class Project(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    name = models.CharField(max_length=100, unique=True)
    short_description = models.CharField(max_length=160)
    long_description = models.TextField()
    snapshot = CloudinaryField(
        "image",
        overwrite=True,
        format="jpg",
        transformation=[{"quality": "auto", "fetch_format": "auto"}],
    )
    industry = models.ForeignKey(
        Industry,
        on_delete=models.PROTECT,
    )
    technologies = models.ManyToManyField(
        Technology,
    )
    features = models.ManyToManyField(
        Feature,
    )
    is_featured = models.BooleanField(default=False)
    live_site = models.URLField()
    github_url = models.URLField()
    first_created = models.DateField(
        _("First created"),
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: typing.ClassVar = ["name"]

        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["is_featured"],
                condition=models.Q(is_featured=True),
                name="only_one_featured_project",
            ),
        ]

    def __str__(self):
        return self.name


class Detail(models.Model):
    problem = models.TextField()
    solution = models.TextField()
    front_end_techs = models.CharField(max_length=160)
    back_end_techs = models.CharField(max_length=160)
    other_techs = models.CharField(max_length=160)
    key_features = models.ManyToManyField(
        KeyFeature,
    )
    challenges = models.ManyToManyField(
        Challenge,
    )
    impacts = models.ManyToManyField(
        Impact,
    )
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="details",
    )


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=500)
    message = models.TextField(max_length=10000)
    date_added = models.DateTimeField(default=timezone.now)
