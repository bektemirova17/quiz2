# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class PostList(models.Model):
    title= models.CharField(max_length = 300)

    def __str__(self):
        return '{}'.format(self.title)


    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    like_count = models.IntegerField()
    created_at = models.DateTimeField(default = datetime.now, blank = 'true')
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return '{}' .format(self.title)

    def to_json_for_c(self):
        return{
            'id': self.id,
            'title': self.title,
            'like_count': self.like_count,
      }

      def to_json_for_d(self):
          return{
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at,
            'like_count': self.like_count,
            'body': self.body,
            'created_by': self.created_by,

          }
# Create your models here.
