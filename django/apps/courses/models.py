from django.db import models
from apps.lessons.models import Lesson
from apps.tags.models import SubjectTag

def sortByOrder(rel):
    return rel.order


class Course(models.Model):
    title = models.CharField('Название курса', max_length=300)
    subject_tag = models.ForeignKey(SubjectTag)
    teacher = models.ForeignKey('auth.User', related_name='course_teacher')
    about = models.TextField('Описание курса')
    

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title

    @property
    def course_lesson_relations(self):
        return CourseLessonRelation.objects.filter(course=self)

    @property
    def lessons_of_course(self):
        relations = self.course_lesson_relations
        relations.sort(key=sortByOrder) 
        return [rel.lesson for rel in relations]


class CourseLessonRelation(models.Model):
    course = models.ForeignKey(Course)
    lesson = models.ForeignKey(Lesson)
    order = models.IntegerField('Порядковый номер урока в курсе', default=0)

    class Meta:
        verbose_name = 'включение урока в курс'
        verbose_name_plural = 'включения урока в курс'

    def __str__(self):
        return "{} in {}".format(self.lesson, self.course)


