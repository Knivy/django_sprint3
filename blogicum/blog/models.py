from django.db import models  # type: ignore[import-untyped]
from django.contrib.auth import get_user_model  # type: ignore[import-untyped]


User = get_user_model()


class BaseModel(models.Model):
    """
    Базовая модель.

    is_published - флаг Опубликовано.
    created_at - дата создания записи в БД.
    """

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    """
    Категория поста.
    title - название категории.
    description - описание категории.
    slug - слаг категории.
    """

    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Location(BaseModel):
    """
    Место, связанное с постом.

    name - название места.
    """

    name = models.CharField(max_length=256)


class Post(BaseModel):
    """
    Модель поста.

    title - название поста.
    text - текст поста.
    pub_date - дата публикации.
    author - автор поста.
    location - связанное место.
    category - категория поста.
    """

    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts_for_location',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts_for_category',
    )
