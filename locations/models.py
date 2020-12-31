# from django.db import models
# from django.db.models.signals import post_save
# from .utils import uniqueSlugGenerator
# # Create your models here.
# # locations models here Provinces , Centers , DMAS

# class Province(models.Model):
#     name = models.CharField(max_length=50,unique=True)
#     longitude = models.FloatField() 
#     latitude = models.FloatField() 
#     created = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField()

#     def __str__(self):
#         return self.name + 'longitude' + self.longitude + 'latitude' + self.latitude

# class Center(models.Model):
#     name = models.CharField(max_length=50,unique=True)
#     longitude = models.FloatField() 
#     latitude = models.FloatField() 
#     created = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField()
#     province = models.ForeignKey('Province',on_delete=models.CASCADE,related_name='centers',null=True,blank=True)



#     def __str__(self):
#         return self.name + 'longitude' + self.longitude + 'latitude' + self.latitude


# STATUS_CHOICES=(('active',"نشط"),('disabled','معطل'))


# class DMA(models.Model):
#     name = models.CharField(max_length=50,unique=True)
#     longitude = models.FloatField() 
#     latitude = models.FloatField() 
#     date = models.DateField(null=True,blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='active')
#     slug = models.SlugField()
#     center = models.ForeignKey('Center',on_delete=models.CASCADE,related_name='center_dmas',null=True,blank=True)
    

#     def __str__(self):
#         return self.name + 'longitude' + self.longitude + 'latitude' + self.latitude

# class Point(models.Model):
#     dma = models.ForeignKey('DMA',on_delete=models.CASCADE,related_name='dma_points',null=True,blank=True)
#     name = models.CharField(max_length=50,unique=True)
#     longitude = models.FloatField() 
#     latitude = models.FloatField() 
#     code = models.CharField(null=True,blank=True)
#     serial_number = models.IntegerField(null=True,blank=True)
#     sms_number = models.IntegerField(null=True,blank=True)
#     valid_days = models.IntegerField(null=True,blank=True)
#     installation_date = models.DateField(null=True,blank=True)
#     created = models.DateTimeField(auto_now_add=True) 
#     type = models.ForeignKey('type',on_delete=models.CASCADE,related_name='type_points',null=True,blank=True)
#     # flow = models.FloatField(null=True,blank=True)
#     # pressure = models.FloatField(null=True,blank=True)
#     # flow_from = models.IntegerField(null=True,blank=True)
#     # flow_to = models.IntegerField(null=True,blank=True)
#     # pressure_from = models.IntegerField(null=True,blank=True)
#     # pressure_to = models.IntegerField(null=True,blank=True)
    

# def save_location(sender,**kwargs):
#     if not kwargs['slug']:
#         kwargs['slug']=uniqueSlugGenerator(kwargs['instance'])
#         kwargs['instance'].save()


# post_save.connect(save_location,sender=DMA)
# post_save.connect(save_location,sender=Center)
# post_save.connect(save_location,sender=Province)