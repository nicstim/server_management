import uuid

from django.db import models


class VPS(models.Model):
    uid = models.UUIDField(verbose_name="UID сервера", default=uuid.uuid4, unique=True)
    cpu = models.PositiveIntegerField(verbose_name="Количество ядер", default=1)
    ram = models.PositiveIntegerField(verbose_name="Объем ОЗУ", default=1024)
    hdd = models.PositiveIntegerField(verbose_name="Объем HDD", default=1024)
    status = models.CharField(verbose_name="Статус сервера", choices=(
        ("started", "Запущен"),
        ("stopped", "Остановлен"),
        ("blocked", "Заблокирован"),
    ), max_length=7)

    class Meta:
        verbose_name = "Сервер"
        verbose_name_plural = "Сервера"

    def __str__(self):
        status = "✅" if self.status == "started" else "🛑" if self.status == "stopped" else "⛔️"
        return f"Server {self.uid} | Статус: {status}"

