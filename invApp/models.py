from django.db import models

# Create your models here.
class BookModel(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200, unique=True)
    book_author = models.CharField(max_length=200)
    publication_date = models.DateField()
    book_category = models.CharField(max_length=200)
    book_description = models.CharField(max_length=200)
    book_status = models.CharField(max_length=200)
    book_score = models.IntegerField()

    def __str__(self):
        return self.bookk_title

class BookImage(models.Model):
    book = models.ForeignKey(BookModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return f"Image for {self.book.book_title}"
