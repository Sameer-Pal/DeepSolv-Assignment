from facebook_scraper import get_posts
from .models import *
import os
import environ
env = environ.Env()
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def fetch_groups():
    groups = Group.objects.all()
    return groups


def get_group_posts(group_id):
    posts = get_posts(group=group_id, credentials=(env('FACEBOOK_USERNAME'), env('FACEBOOK_PASSWORD')), pages=100,
                      timeout=60,
                      options={"allow_extra_requests": False})
    final = []
    for post in posts:
        if post['listing_title'] and post['listing_location'] and post['listing_price'] \
                and post['post_text'] and post['image_lowquality'] and post['username'] and post['user_url']:
            exists = post_exist(post)
            if not exists:
                final.append(post)
    print('post fetched from fb')
    return final


def save_to_db(post, group):
    new_post = Post(post_text=post['post_text'], username=post['username'], user_url=post['user_url'],
                    title=post['listing_title'], location=post['listing_location'], price=post['listing_price'], group=group)
    new_post.save()

    print('post created and saved to db')

    for image in post['images_lowquality']:
        image = Image(url=image, post=new_post)
        image.save()
        print('post images saved to db')


def post_exist(post):
    print('checking if post exists')
    return Post.objects.filter(title=post['listing_title']).exists()


def fetch_and_save():
    groups = fetch_groups()
    for group in groups:
        posts = get_group_posts(group.group_id)
        for post in posts:
            save_to_db(post, group)
