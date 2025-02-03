from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from topshiriq.choices import TopshiriqTuriChoice, MajburiyTopshiriqTuriChoice, QoshimchaTopshiriqTuriChoice
from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq 

@receiver(m2m_changed, sender=SuperAdminTopshiriq.users.through)
def task_users_added(sender, instance, action, **kwargs):
    if action == "post_add":

        if instance.topshiriq_turi == TopshiriqTuriChoice.MAJBURIY:
            for user in instance.users.all():
                for _ in range(int(instance.urinishlar_soni)):
                    SuperAdminMajburiyTopshiriq.objects.create(
                        user=user,  # user ni obyekt sifatida beramiz
                        topshiriq=instance,  # instance.id emas, obyektning o‘zi kerak
                        tur=MajburiyTopshiriqTuriChoice.TTJGA_TASHRIF
                    )

        if instance.topshiriq_turi == TopshiriqTuriChoice.QOSHIMCHA:
            for user in instance.users.all():
                for _ in range(int(instance.urinishlar_soni)):
                    SuperAdminQoshimchaTopshiriq.objects.create(
                        user=user,  # user ni obyekt sifatida beramiz
                        topshiriq=instance,  # instance.id emas, obyektning o‘zi kerak
                        tur=QoshimchaTopshiriqTuriChoice.TTJGA_TASHRIF
                    )