
from django.db import models
from django.contrib.auth.models import User
from django_countries import CountryField
from django.db.models.signals import post_save


TITLES = ('Mr', 'Ms', 'Mrs', 'Miss', 'Dr', 'Prof')
SEABIRDS = ('All seabirds', 'Penguins', 'Diving petrels', 'Storm petrels', 'Petrels', 'Pelicans', 'Gannets and boobies', 'Cormorants', 'Frigatebirds', 'Tropicbirds', 'Skuas', 'Gulls and kitttiwakes', 'Terns', 'Skimmers', 'Auks')


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name = 'profile')
    title = models.CharField(max_length=5, choices=zip(TITLES, TITLES), null=True, blank=True)
    webpage = models.URLField(null=True, blank=True)
    institution = models.CharField(max_length=50, null=True, blank=True)
    institution_website = models.URLField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    research = models.TextField(null=True, blank=True)
    photograph = models.ImageField(upload_to='profiles', null=True, blank=True)
    seabirds = models.CharField(max_length=60, choices=zip(SEABIRDS, SEABIRDS), null=True, blank=True)
 

    def __str__(self):
        return "%s %s"%(self.title, self.user.first_name, self.user.last_name)

#    @permalink
#    def get_absolute_url(self):
#        return ('profile', (), {'username': self.user.username})

    def has_link(self):
        linkname = ('%s-%s' % (self.firstname, self.lastname)).lower()
        pages = Page.objects.filter(name = linkname)
        return pages


#Automatically create a profile when a User is created (if one doesn't already exits)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            UserProfile.objects.get(user=instance)
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


