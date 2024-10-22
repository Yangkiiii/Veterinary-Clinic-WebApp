from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Define the AccountsManager class
class AccountsManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # This will store password in plain text as per the previous override
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

# Define the Accounts model
class Accounts(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    fname = models.CharField(max_length=30, verbose_name='First Name')
    lname = models.CharField(max_length=30, verbose_name='Last Name')
    number = models.CharField(max_length=15, verbose_name='Phone Number')
    address = models.TextField(verbose_name='Address')
    role = models.CharField(max_length=30, default='owner', verbose_name='Role')  # Ensure this line is included
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128, verbose_name='Password')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']

    objects = AccountsManager()

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"

    def set_password(self, raw_password):
        """Override the set_password method to store plain text password."""
        self.password = raw_password

    def check_password(self, raw_password):
        """Override check_password to compare raw password."""
        return self.password == raw_password
    
class Service(models.Model):
    type_of_service = models.CharField(max_length=30, unique=True, verbose_name='Type of Service')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')  # Use DecimalField for monetary values

    def __str__(self):
        return f"Service: {self.type_of_service}, Price: {self.price}"


class Animal(models.Model):  # Keep only one Animal model
    pet_species = models.CharField(max_length=30, unique=True, verbose_name='Pet Species')

    def __str__(self):
        return f"Pet Species: {self.pet_species}"


class AvailableSlot(models.Model):
    available_slot_time = models.DateTimeField(unique=True, verbose_name='Available Slot Time')  # Use DateTimeField for better time handling
    slots_left = models.IntegerField(verbose_name='Slots Left')

    def __str__(self):
        return f"Available Time: {self.available_slot_time}, Slots Left: {self.slots_left}"


class Schedule(models.Model):
    owners_name = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name="Owner's Name")  # Link to Account model
    species = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Species')  # Link to Animal model
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')  # Link to Service model
    date_time = models.DateTimeField(null=True, verbose_name='Date/Time')
    status = models.CharField(max_length=30, verbose_name='Status')
    payment_status = models.CharField(max_length=15, verbose_name='Payment Status')

    def __str__(self):
        return f"Owner: {self.owners_name.fname} {self.owners_name.lname}, Species: {self.species.pet_species}, Date: {self.date_time}"


class TransactionHistory(models.Model):
    date = models.DateField(verbose_name='Date')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name='User')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')
    pet_species = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Pet Species')

    def __str__(self):
        return f"Date: {self.date}, Amount: {self.amount}, User: {self.user.fname} {self.user.lname}, Service: {self.service.type_of_service}, Pet Species: {self.pet_species.pet_species}"
