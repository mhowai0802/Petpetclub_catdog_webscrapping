import instaloader
from instagrapi import Client

# bot = instaloader.Instaloader()
# bot.login('makhowai0802','joniwhfe5A')
# hashtag = instaloader.Hashtag.from_name(bot.context, 'cat')
# python_posts = hashtag.get_posts()
# for post in python_posts:
#     print(post.date, post.owner_username, post.get_is_videos())
#     if post.get_is_videos() == True:
#         print(post.date, post.owner_username, post.get_is_videos())
#         break

cl = Client()
cl.login('makhowai0802', 'joniwhfe5A')
user_id = cl.user_id_from_username("chunbae_gram")
medias = cl.story_download(user_id, 20)
