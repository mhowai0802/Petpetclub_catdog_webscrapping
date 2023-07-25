from instascrape import *
import instaloader
import glob
import shutil
import os
import glob
from cat_detect import *
from dog_detect import *

class ig_scrapper():

    def __init__(self):
        self.cat_detector = cat_detection()
        self.dog_detector = dog_detection()

    def scrapper(self,detector,tag):
        # download all photos with tag
        bot = instaloader.Instaloader()
        hashtag = instaloader.Hashtag.from_name(bot.context, tag)
        python_posts = hashtag.get_posts()
        counter = 0
        if os.path.exists(f'./{tag}-photos') == False:
            os.mkdir(f'./{tag}-photos')
        for index, post in enumerate(python_posts, 1):
            bot.download_post(post, target=f'{hashtag.name}_{index}')
            images = [f for f in os.listdir(f'{tag}_{index}') if '.jpg' in f.lower()]
            for number,image in enumerate(images):
            # picture filtering
                output = detector.read_face_output(f'./{tag}_{index}/{image}')
                if output == True:
                    new_path = f'./{tag}-photos/' + f'{tag}_{counter}.jpg'
                    shutil.move(f'./{tag}_{index}/' + image, new_path)
                    counter += 1
            # Stop the loop after 100 posts
            if index == 2: break
        # delete all photos with tag
        fileList = glob.glob('./*')
        for filePath in fileList:
            if filePath.find(tag+'_') > 0:
                shutil.rmtree(filePath)

    # Download all photos with catlovers
    def cat(self):
        self.scrapper(self.cat_detector,'catlovers')
    # Download all photos with doglovers
    def dog(self):
        self.scrapper(self.dog_detector,'doglovers')


obj = ig_scrapper()
obj.dog()


