# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class UserProfileInfo(models.Model):
  
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


	def __str__(self):
		return self.user.username

	# def get_absolute_url(self):
	# 	return reverse('profile', args=[str(self.id)])

class Subject(models.Model):
    """Model representing the subject of the article."""
    name = models.CharField(max_length=200, help_text='Enter the article subject (e.g. Data Science)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Article(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    abstract = models.TextField(max_length=1000, help_text='Enter the abstract of the article')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    subject = models.ManyToManyField(Subject, help_text='Select the subject of the article')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('article-detail', args=[str(self.id)])

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
