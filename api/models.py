from django.db import models


class Employee(models.Model):
    """
    таблица сотрудников (ФИО, должность, ...)
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=60)

    @property
    def fullname(self):
        return f'{self.last_name} {self.first_name}'

    def __str__(self):
        return self.fullname


class Task(models.Model):
    """
    таблица задач (наименование, ссылка на родительскую задачу(если есть зависимость), исполнитель, срок, статус, ...)
    """
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    parent_task = models.CharField(default=None)
    contractor = models.IntegerField(default=0)
    period = models.DateField(default=None)
    status = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
