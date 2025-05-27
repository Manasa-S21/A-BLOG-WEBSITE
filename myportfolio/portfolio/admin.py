# portfolio/admin.py
from django.contrib import admin
from .models import ContactMessage, BlogPost # Import BlogPost

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp') # Removed message for brevity
    list_filter = ('timestamp',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('timestamp',)

# --- NEW: Register BlogPost ---
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_date', 'status')
    list_filter = ('status', 'created_date', 'publish_date', 'author')
    search_fields = ('title', 'content')
    # Automatically create slug based on title (requires title field in the form)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',) # Better UI for selecting author if many users
    date_hierarchy = 'publish_date'
    ordering = ('status', 'publish_date')
# --- End NEW ---