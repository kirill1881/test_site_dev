from unidecode import unidecode
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    user_email = models.EmailField(max_length=150)
    oblast = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    GENDER_CHOICE = [
            ('M', 'Мужчина'),
            ('F', 'Женщина')
        ]
    gender = models.CharField(choices=GENDER_CHOICE)
    age = models.IntegerField()
    organization = models.CharField(blank=True)


class Test(models.Model):
    TEST_TYPE_CHOICE = [
        ('1', 'Пользовательский'),
        ('2', 'Контрольный')
    ]
    test_subject = models.ForeignKey('Subject', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=150)
    test_type = models.CharField(max_length=300, choices=TEST_TYPE_CHOICE)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('test_view', kwargs={'test_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # Используем unidecode для преобразования русского текста в ASCII
            ascii_title = unidecode(self.title)
            self.slug = slugify(ascii_title)
        super().save(*args, **kwargs)


class Subject(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subject_view', kwargs={'subject_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # Используем unidecode для преобразования русского текста в ASCII
            ascii_title = unidecode(self.title)
            self.slug = slugify(ascii_title)
        super().save(*args, **kwargs)


class Question(models.Model):
    test_title = models.ForeignKey('Test', on_delete=models.CASCADE, null=True)
    question_title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=300)
    answer1 = models.CharField(max_length=150)
    answer2 = models.CharField(max_length=150)
    answer3 = models.CharField(max_length=150)
    answer4 = models.CharField(max_length=150)
    ANSWERS_CHOICE = [
        ('1', answer1),
        ('2', answer2),
        ('3', answer3),
        ('4', answer4)
    ]
    is_correct = models.CharField(max_length=150, choices=ANSWERS_CHOICE)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=150)
