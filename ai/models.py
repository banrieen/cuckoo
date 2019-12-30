from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """ 型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，
        Django 自动生成的 admin 里也使用这个方法来表示对象。 """
        return self.question_text
    


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently ?'