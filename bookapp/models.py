from django.db import models

from django.utils.translation import gettext_lazy as _ # remind me later

from django.contrib.auth.models import User

class Category(models.Model):
    cat = models.CharField(max_length=100,
                           verbose_name = _("Book Category"))
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.cat
    class Meta:
        pass

class Book(models.Model):

    author = models.CharField(
        max_length=20000,
        help_text="Name of Author to avoid Plagiarisation",
        verbose_name="Book Author",
        blank=True,
        default='Unknown'
        )
    category = models.ManyToManyField(Category)

    title = models.CharField(
        max_length=2000,
    ) # Introduction to computer science

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name=_("Upload by"))

    slug = models.SlugField(
        max_length=2000
    ) # freebook.com/introduction-to-computer-science

    summary = models.TextField() # 3 == "3"
    isbn = models.PositiveIntegerField() # positive values only

    image = models.ImageField(upload_to='images', blank=True,
                              verbose_name=_("upload")) # add Verbose name
    docs = models.FileField(upload_to='docs', blank=True,
                            verbose_name=_("Upload document")) # add Verbose name

    created = models.DateTimeField(auto_now_add=True) # First entry only 7:19
    updated = models.DateTimeField(auto_now=True) # auto save the time of update 7:29
    author_web = models.URLField(blank=True) # www.google.com # Not required

    def __str__(self) -> str:
        return f'Author is {self.author} and isbn number is {self.isbn}'