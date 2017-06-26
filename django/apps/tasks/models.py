from django.db import models
#from apps.nodes.models import Lesson
from apps.users.models import User
from apps.lessons.models import Lesson

# Tasks
class Task(models.Model):
    """
		Задание для конкретного ученика, связаное с уроком
	"""
    student = models.ForeignKey(User, related_name='task_student')
    teacher = models.ForeignKey(User, related_name='task_teacher')
    lesson = models.ForeignKey(Lesson)
    start_time = models.DateTimeField(null=True, blank=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    is_finished = models.BooleanField('Закончил?', default=False)
    
    class Meta:
        verbose_name = 'Задание для ученика'
        verbose_name_plural = 'Задание для ученика'

    def __str__(self):
        return u'For {}, "{}"'.format(self.student, self.lesson)

