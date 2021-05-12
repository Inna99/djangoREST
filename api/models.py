from django.db import models


class Position(models.Model):
    """ должность """
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Employee(models.Model):
    """
    таблица сотрудников (ФИО, должность, ...)
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL)

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
    description = models.TextField(blank=True, default=None)
    parent = models.ForeignKey('self', default=None, on_delete=models.CASCADE)
    period = models.DateField(default=None)
    status = models.SmallIntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.status} {self.name} {self.parent or "not parent"} {self.employee or "not employee"}'
