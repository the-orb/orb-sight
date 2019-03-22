from django.db import models


class Family(models.Model):
      name = models.CharField(max_length=80)
      description = models.TextField()
      
      def _str_(self):
        return self.name


class Individual(models.Model):
      name = models.CharField(max_length=40)
      fore_name = models.CharField(max_length=40)
      last_name = models.CharField(max_length=40)
      description = models.TextField()
      
      def _str_(self):
        return self.name


class Member(models.Model):
      name = models.CharField(max_length=40)
      user_name = models.CharField(max_length=40)
      
      def _str_(self):
        return self.name


class Network(models.Model):
      title = models.CharField(max_length=80)
      description = models.TextField()
      
      def _str_(self):
        return self.title


class Orb(models.Model):
      title = models.CharField(max_length=80)
      description = models.TextField()
      
      def _str_(self):
        return self.title


class Request(models.Model):
      title = models.CharField(max_length=80)
      description = models.TextField()
      
      def _str_(self):
        return self.title


class Response(models.Model):
      title = models.CharField(max_length=80)
      description = models.TextField()
      
      def _str_(self):
        return self.title