from django.db import models
from farms.models import ProducerProfile
from managers.managers import RecordManager


# Create your models here.
class Diary(models.Model):
    TRANSACTION_TYPE = (
        ("G", "Gasto"),
        ("I", "Ingreso"),
    )

    activity_date = models.DateField()
    activity = models.TextField(max_length=255)
    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPE, default=TRANSACTION_TYPE[0][1]
    )
    debit = models.DecimalField(
        max_digits=10, decimal_places=2, default="0.00", null=True, blank=True
    )
    credit = models.DecimalField(
        max_digits=10, decimal_places=2, default="0.00", null=True, blank=True
    )
    reference = models.CharField(max_length=20, default="S/R", null=True, blank=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default="0.00", null=True, blank=True
    )
    farm = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        ordering = ("-activity_date",)

    def save(self, *args, **kwargs):
        same_date_transaction = (
            Diary.objects.filter(activity_date__lte=self.activity_date)
            .exclude(id=self.id)
            .order_by("id")
        )
        other_date_transaction = (
            Diary.objects.filter(activity_date__gt=self.activity_date)
            .exclude(id=self.id)
            .order_by("id")
        )
        print(same_date_transaction)
        if same_date_transaction:
            last_transaction = same_date_transaction.last()
            print("Ultima transaction", last_transaction.balance)
            self.balance = (last_transaction.balance + self.credit) - self.debit
        elif other_date_transaction:
            other_transaction = other_date_transaction.last()
            self.balance = (other_transaction.balance + self.credit) - self.debit
        else:
            self.balance = self.credit - self.debit

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.activity_date} - {self.activity} - Balance: {self.balance}"

    objects = RecordManager()
