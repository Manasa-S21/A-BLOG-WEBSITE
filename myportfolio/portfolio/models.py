# portfolio/models.py
from django.db import models
from django.utils import timezone
from django.conf import settings # To link to the User model
from django.urls import reverse # To generate URLs for posts
from django.utils.text import slugify # To help generate slugs

# Keep your existing ContactMessage model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.name} ({self.email}) - {self.subject}"

# --- NEW: BlogPost Model ---
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    # Unique slug for URLs (e.g., my-first-post)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # Or models.SET_NULL if posts can remain without author
        related_name='blog_posts'
    )
    # Use TextField for the main content
    content = models.TextField()
    # Optional image - requires Pillow installation
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/', blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish_date',) # Default ordering: newest first

    def __str__(self):
        return self.title

    # Automatically generate slug from title if not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # Helper method to get the absolute URL for a post
    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.publish_date.year,
                                                self.publish_date.month,
                                                self.publish_date.day, self.slug])