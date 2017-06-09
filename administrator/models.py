from __future__ import unicode_literals

from django.db import models

# class Adopt(models.Model):
#     description = models.TextField(blank=True, null=True)
#     user = models.IntegerField(blank=True, null=True)
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'adopt'
#
#
# class AdoptComment(models.Model):
#     comment = models.TextField(blank=True, null=True)
#     adopt = models.IntegerField(blank=True, null=True)
#     user = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'adopt_comment'
#
#
# class AdoptImage(models.Model):
#     src = models.TextField(blank=True, null=True)
#     adopt = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'adopt_image'
#
#
# class AuthProvider(models.Model):
#     user = models.IntegerField(blank=True, null=True)
#     type = models.TextField(blank=True, null=True)
#     externalid = models.TextField(db_column='externalId', unique=True, blank=True, null=True)  # Field name made lowercase.
#     accesstoken = models.TextField(db_column='accessToken', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'auth_provider'


class Blog(models.Model):
    source = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    sourcecreatedat = models.DateTimeField(db_column='sourceCreatedAt', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    link = models.TextField(unique=True, blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blog'
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.source + ' / ' + self.link


class Category(models.Model):
    name = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        managed = False
        db_table = 'category'
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    categories = models.ManyToManyField(Category, through='CategoryLocationsLocationCategories')

    class Meta:
        verbose_name = 'Location'
        managed = False
        db_table = 'location'
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.name


class CategoryLocationsLocationCategories(models.Model):
    location_categories = models.ForeignKey(Location, on_delete=models.CASCADE, db_column='location_categories', verbose_name='Location')
    category_locations = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_locations', verbose_name='Category')

    class Meta:
        verbose_name = 'Category Mapping'
        verbose_name_plural = 'Category Mappings'
        managed = False
        auto_created = Location
        db_table = 'category_locations__location_categories'

    def __str__(self):
        return self.category_locations.name + '/' + self.location_categories.name

# class Notification(models.Model):
#     from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
#     to = models.IntegerField(blank=True, null=True)
#     roomapplicationcreate = models.IntegerField(db_column='roomApplicationCreate', blank=True, null=True)  # Field name made lowercase.
#     roomapplicationstatusupdate = models.IntegerField(db_column='roomApplicationStatusUpdate', blank=True, null=True)  # Field name made lowercase.
#     roomapplicationmessagecreate = models.IntegerField(db_column='roomApplicationMessageCreate', blank=True, null=True)  # Field name made lowercase.
#     walkerapplicationcreate = models.IntegerField(db_column='walkerApplicationCreate', blank=True, null=True)  # Field name made lowercase.
#     walkerapplicationstatusupdate = models.IntegerField(db_column='walkerApplicationStatusUpdate', blank=True, null=True)  # Field name made lowercase.
#     walkerapplicationmessagecreate = models.IntegerField(db_column='walkerApplicationMessageCreate', blank=True, null=True)  # Field name made lowercase.
#     adoptcommentcreate = models.IntegerField(db_column='adoptCommentCreate', blank=True, null=True)  # Field name made lowercase.
#     seen = models.NullBooleanField()
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification'
#
#
# class NotificationAdoptCommentCreate(models.Model):
#     adopt = models.IntegerField(blank=True, null=True)
#     comment = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_adopt_comment_create'
#
#
# class NotificationRoomApplicationCreate(models.Model):
#     room = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_room_application_create'
#
#
# class NotificationRoomApplicationMessageCreate(models.Model):
#     room = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     message = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_room_application_message_create'
#
#
# class NotificationRoomApplicationStatusUpdate(models.Model):
#     room = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     prevstatus = models.TextField(db_column='prevStatus', blank=True, null=True)  # Field name made lowercase.
#     currentstatus = models.TextField(db_column='currentStatus', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_room_application_status_update'
#
#
# class NotificationWalkerApplicationCreate(models.Model):
#     walker = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_walker_application_create'
#
#
# class NotificationWalkerApplicationMessageCreate(models.Model):
#     walker = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     message = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_walker_application_message_create'
#
#
# class NotificationWalkerApplicationStatusUpdate(models.Model):
#     walker = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     prevstatus = models.TextField(db_column='prevStatus', blank=True, null=True)  # Field name made lowercase.
#     currentstatus = models.TextField(db_column='currentStatus', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'notification_walker_application_status_update'
#
#
# class Pet(models.Model):
#     name = models.TextField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pet'
#
#
# class PetImage(models.Model):
#     src = models.TextField(blank=True, null=True)
#     pet = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'pet_image'
#
#
# class PetPostsPostPets(models.Model):
#     pet_posts = models.IntegerField(blank=True, null=True)
#     post_pets = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pet_posts__post_pets'
#
#
# class PetUsersUserPets(models.Model):
#     pet_users = models.IntegerField(blank=True, null=True)
#     user_pets = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pet_users__user_pets'
#
#
# class Post(models.Model):
#     text = models.TextField(blank=True, null=True)
#     user = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'post'
#
#
# class PostImage(models.Model):
#     src = models.TextField(blank=True, null=True)
#     post = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'post_image'
#
#
# class Room(models.Model):
#     description = models.TextField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True)
#     user = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'room'
#
#
# class RoomApplication(models.Model):
#     rating = models.IntegerField(blank=True, null=True)
#     review = models.TextField(blank=True, null=True)
#     consumer = models.IntegerField(blank=True, null=True)
#     provider = models.IntegerField(blank=True, null=True)
#     room = models.IntegerField(blank=True, null=True)
#     status = models.TextField(blank=True, null=True)
#     finishedat = models.DateTimeField(db_column='finishedAt', blank=True, null=True)  # Field name made lowercase.
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'room_application'
#
#
# class RoomApplicationMessage(models.Model):
#     from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
#     to = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     room = models.IntegerField(blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     seen = models.NullBooleanField()
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'room_application_message'
#
#
# class RoomImage(models.Model):
#     src = models.TextField(blank=True, null=True)
#     room = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'room_image'
#
#
# class User(models.Model):
#     email = models.TextField(unique=True, blank=True, null=True)
#     password = models.TextField(blank=True, null=True)
#     userdata = models.IntegerField(db_column='userData', blank=True, null=True)  # Field name made lowercase.
#     socketid = models.TextField(db_column='socketId', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'user'
#
#
# class UserData(models.Model):
#     user = models.IntegerField(blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)
#     avatar = models.TextField(blank=True, null=True)
#     firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
#     lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'user_data'
#
#
# class Walker(models.Model):
#     description = models.TextField(blank=True, null=True)
#     cost = models.FloatField(blank=True, null=True)
#     user = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'walker'
#
#
# class WalkerApplication(models.Model):
#     rating = models.IntegerField(blank=True, null=True)
#     review = models.TextField(blank=True, null=True)
#     consumer = models.IntegerField(blank=True, null=True)
#     provider = models.IntegerField(blank=True, null=True)
#     walker = models.IntegerField(blank=True, null=True)
#     status = models.TextField(blank=True, null=True)
#     finishedat = models.DateTimeField(db_column='finishedAt', blank=True, null=True)  # Field name made lowercase.
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'walker_application'
#
#
# class WalkerApplicationMessage(models.Model):
#     from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
#     to = models.IntegerField(blank=True, null=True)
#     application = models.IntegerField(blank=True, null=True)
#     walker = models.IntegerField(blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     seen = models.NullBooleanField()
#     deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'walker_application_message'
