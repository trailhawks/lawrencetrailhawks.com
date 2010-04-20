from django.contrib.auth.models import User
import datetime

members = ((User.objects.get(username='nick.lang@gmail.com'), 'Colo Hawk', 7752405717, '833 Indiana St.Lawrence, KS 66044', True, datetime.datetime.now()),
           (User.objects.get(username='unews@ultrastory.com'), 'Story Hawk', 7851234567, '123 Apple St.\nLawrence, KS 66044', True, datetime.datetime.today()),
           (User.objects.get(username='lluhar@gmail.com'), 'Pixie Hawk', 7851234567, '123 Apple St.\nLawrence, KS 66044', True, datetime.datetime.today()),
           (User.objects.get(username='shhenning@gmail.com'), 'Scoop Hawk', 7851234567, '123 Apple St.\nLawrence, KS 66044', True, datetime.datetime.today()),
           (User.objects.get(username='jhhenning@gmail.com'), 'GNT Hawk', 7851234567, '123 Apple St.\nLawrence, KS 66044', True, datetime.datetime.today()),
           (User.objects.get(username='jtripplet@gmail.com'), 'Beatnick Hawk', 7851234567, '123 Apple St.\nLawrence, KS 66044', True, datetime.datetime.today()),
           (User.objects.get(username='kristy.mayo@gmail.com'), 'Black Mamba Hawk', 7851234567, '123 Apple St.\nLawrence, KS 66044', True, datetime.datetime.today()),
           )