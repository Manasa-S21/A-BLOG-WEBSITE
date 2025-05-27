from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ContactForm
from .models import BlogPost, ContactMessage  # Make sure ContactMessage is imported if used elsewhere
from django.contrib import messages
from django.utils import timezone # Import timezone if needed directly, otherwise model handles it

# --- Core Page Views ---

def home_view(request):
    """
    Renders the home page.
    """
    context = {
        'page_title': 'Home',
    }
    return render(request, 'portfolio/home.html', context) # Ensure template path is correct

def about_view(request):
    """
    Renders the about page.
    """
    context = {
        'page_title': 'About Me',
    }
    return render(request, 'portfolio/about.html', context) # Ensure template path is correct

# --- Blog Views ---

def blog_view(request):
    """
    Displays a list of published blog posts.
    """
    # Fetch only published posts from the database, ordered by publish date
    published_posts = BlogPost.objects.filter(status='published').order_by('-publish_date')

    context = {
        'page_title': 'Blog',
        'posts': published_posts # Pass the queryset to the template
    }
    return render(request, 'portfolio/blog.html', context) # Ensure template path is correct

def blog_post_detail_view(request, year, month, day, slug):
    """
    Displays a single blog post identified by its publication date and slug.
    """
    post = get_object_or_404(BlogPost,
                             status='published',
                             publish_date__year=year,
                             publish_date__month=month,
                             publish_date__day=day,
                             slug=slug)
    context = {
        'page_title': post.title, # Use post title for the page title
        'post': post
    }
    return render(request, 'portfolio/blog_post_detail.html', context) # Ensure template path is correct

# --- Contact Views ---

def contact_view(request):
    """
    Handles displaying the contact form (GET) and processing submissions (POST).
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Saves the valid form data to the ContactMessage model
            messages.success(request, 'Your message has been sent successfully! Thank you.')
            # Redirect to the success page using the URL name
            return redirect(reverse('success'))
        else:
            # Form is invalid, re-render the page with the form containing errors
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request: Create a blank form instance
        form = ContactForm()

    context = {
        'page_title': 'Contact Me',
        'form': form
    }
    return render(request, 'portfolio/contact.html', context) # Ensure template path is correct

def success_view(request):
    """
    Displays the success page after contact form submission.
    """
    context = {
        'page_title': 'Message Sent!',
    }
    return render(request, 'portfolio/success.html', context) # Ensure template path is correct