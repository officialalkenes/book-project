from django.db import models



# Create your models here.
class Book(models.Model):
    author = models.CharField(
        max_length=20000,
        help_text="Name of Author to avoid Plagiarisation",
        verbose_name="Book Author",
        blank=True,
        default='Unknown'
        )
    title = models.CharField(
        max_length=2000,
    ) # Introduction to computer science
    slug = models.SlugField(
        max_length=2000
    ) # freebook.com/introduction-to-computer-science
    summary = models.TextField() # 3 == "3"
    isbn = models.PositiveIntegerField() # positive values only
    # neg_isbn = models.PositiveIntegerField() # Only Positive values
    # big_isbn = models.PositiveBigIntegerField()
    # decimal_isbn = models.DecimalField(max_digits=14, decimal_places=2) # 2.00 2.213
    created = models.DateTimeField(auto_now_add=True) # First entry only 7:19
    updated = models.DateTimeField(auto_now=True) # auto save the time of update 7:29
    birthday = models.DateField()
    # book_image = models.ImageField()
    # pdf_files = models.FileField()
    author_web = models.URLField() # www.google.com

    def __str__(self) -> str:
        return f'Author is {self.author} and isbn number is {self.isbn}'