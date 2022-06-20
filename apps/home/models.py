from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    def get_absolute_url(self):
        return reverse("category_detail", kwargfs = {'slug':self.slug})


class Genre(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = 'Жанры'

    def get_absolute_url(self):
        return reverse("genre_detail", kwargfs = {'slug':self.slug})


class Product(models.Model):
    CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="product/")
    slug = models.SlugField(unique = True)
    description = models.TextField(verbose_name="описание")
    year_of_create = models.DateField()
    genre = models.ManyToManyField(Genre)
    owner = models.CharField(max_length=150)
    visable = models.BooleanField(default=1)
    treyler = models.CharField(max_length=250)
    day_of_create = models.CharField(choices=CHOICES, default='Monday', max_length=15)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = 'Аниме'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse("product_detail", kwargfs = {'slug':self.slug})


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Аниме')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Фотография к Аниме'
        verbose_name_plural = 'Фотографии к Аниме'


class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.FileField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.video.url}'

    class Meta:
        verbose_name = 'Видео к Аниме'
        verbose_name_plural = 'Видео к Аниме'

    
class Comment(models.Model):
    CHOICES_STAR = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    comm = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True)
    star = models.IntegerField(choices=CHOICES_STAR)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='comm_owner'
        )

    def __str__(self):
        return f'Review by {self.name} on {self.product}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created']


    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    from_email = models.EmailField()