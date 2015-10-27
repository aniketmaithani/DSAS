from django.db import models


class StudentInfo(models.Model):
    full_name = models.CharField(blank=False, null=False, max_length=256)
    course = models.CharField(blank=False, null=False,
                              max_length=100, help_text='Course Name e.g B.TECH/BCA etc.')
    year = models.CharField(blank=False, null=False,
                            max_length=4, help_text='year e.g 2011 etc.')
    passout_year = models.CharField(blank=False, null=False,
                                    max_length=4, help_text='Enter year e.g 2015 etc.')
    aggregate_percentage = models.IntegerField(blank=False, null=False, help_text='Enter the Percentage s')

    def __str__(self):
        return self.StudentInfo

    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Students Information"
        ordering = ['-full_name']
