from django.contrib import admin
from users.models import News, Car, Comment, Product, Article, Application, Blog
from django.contrib.auth.models import Group, User

# admin.site.unregister(Group)
# admin.site.unregister(User)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "description")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "body", "article_type", "publisher_year")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "author_name", "publisher_year")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "qty", "price", "brand_name")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "brand", "name", "power", "color", "country", "year")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "middle_name", "birth_date", "birth_country", "comment")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_confirmed")