from django.db import models
from django.utils import timezone
from students.models import Student
from enrollment.models import Enrollment


class Payment(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pendente"),
        ("PAID", "Pago"),
        ("OVERDUE", "Vencido"),
        ("CANCELLED", "Cancelado"),
    )

    PAYMENT_METHOD_CHOICES = (
        ("PIX", "Pix"),
        ("CREDIT_CARD", "Cartão de Crédito"),
        ("DEBIT_CARD", "Cartão de Débito"),
        ("CASH", "Dinheiro"),
        ("BANK_TRANSFER", "Transferência"),
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="payments"
    )
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="payments"
    )
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    due_date = models.DateField()
    payment_date = models.DateField(
        null=True,
        blank=True
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default="PENDING"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )
    observations = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        today = timezone.now().date()

        # Se venceu e ainda está pendente
        if (self.status == "PENDING" and self.due_date < today):
            self.status = "OVERDUE"
            self.enrollment.status = "SUSPENDED"
            self.enrollment.save()

        # Se foi pago
        elif self.status == "PAID":
            self.payment_date = today
            self.enrollment.status = "ACTIVE"
            self.enrollment.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.student.name} - {self.amount}'
