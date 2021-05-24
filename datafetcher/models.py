from django.db import models

class SheetTracker(models.Model):
    # 证券代码
    code = models.CharField(max_length=64, primary_key=True)
    # 最后更新时间
    last_update = models.DateTimeField(null=True)
    # 最近会计期间
    last_accounting_period = models.DateField(null=True)

    def __str__(self):
        return self.code + "@" + str(self.last_accounting_period) + ", updated at " + str(self.last_update)
