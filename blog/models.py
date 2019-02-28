from django.db import models
from django.utils import timezone


class Post(models.Model) :

    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self) :

        self.published_date = timezone.now()
        self.save()

    def __str__(self) :

        return self.title

class Category(models.Model) :

    '''
    Category : table format category of this board
    * board_type : kind of board
    * board_admin : administrator of this board
    * board_url : url of this board
    '''
    
    board_type = models.CharField(null = False, blank = False, max_length = 20)
    board_admin = models.CharField(null = False, blank = False, max_length = 20)
    board_url = models.CharField(null = False, blank = False, max_length = 200)

class Board(models.Model) :

    '''
    Board - table for cashing board
    * board_number : number of board
    * title : title of post
    * url : link to post
    * category : category of this board
    * admin_post : administrator of this post
    * description : descripttion of post 
    * updated_at : updated date
    '''

    board_number = models.IntegerField(null = False, blank = False)

    title = models.CharField(blank = False, null = False, max_length = 100)
    url = models.CharField(blank = False, null = False, max_length = 200)  
    category = models.CharField(blank = False, null = False, max_length = 20)
    admin_post = models.CharField(null = False, blank = False, max_length = 20)

    description = models.TextField(null = False, blank = False)

    updated_at = models.DateTimeField(auto_now_add = True)