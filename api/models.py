from django.db import models


class Service(models.Model):
    ICON_CHOICES = [
        ('code', 'Code'),
        ('mobile', 'Mobile'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('video', 'Video'),
        ('animation', 'Animation'),
        ('shield', 'Shield (Cyber)'),
        ('users', 'Users'),
        ('book', 'Book'),
    ]

    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=300)
    full_desc = models.TextField()
    icon = models.CharField(max_length=30, choices=ICON_CHOICES, default='code')
    features = models.TextField(
        help_text="Comma-separated list of features. Example: React, Django, APIs"
    )
    order = models.PositiveIntegerField(default=0, help_text="Choto number age dekhabe")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    @property
    def feature_list(self):
        return [f.strip() for f in self.features.split(',') if f.strip()]


class Contact(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('spam', 'Spam'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    service = models.CharField(max_length=120, blank=True)
    budget = models.CharField(max_length=60, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.email}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=100)
    year = models.CharField(max_length=10, default='2025')
    description = models.TextField()
    tags = models.CharField(
        max_length=300, blank=True,
        help_text="Comma-separated tags: Web Development, Next.js, E-commerce"
    )
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="Use this if you don't upload an image")
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    category = models.CharField(max_length=80)
    author = models.CharField(max_length=120)
    excerpt = models.TextField()
    content = models.TextField()
    read_time = models.CharField(max_length=30, default='5 min read')
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title