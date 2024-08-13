from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.CharField(max_length=500)


class Article(models.Model):
    Historical = "historical"
    Modern = "modern"
    Article_type_Choice = [
        (Historical, "History"),
        (Modern, "Modern"),
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    article_type = models.CharField(max_length=100, choices=Article_type_Choice)
    publisher_year = models.IntegerField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    publisher_year = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField()
    brand_name = models.CharField(max_length=100)


class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    power = models.IntegerField()
    color = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.IntegerField()


class Application(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_country = models.CharField(max_length=100)
    comment = models.TextField()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    is_confirmed = models.BooleanField()