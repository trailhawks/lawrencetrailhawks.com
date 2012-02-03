
django-admin.py dumpdata -n --format=json --indent=2 auth.user > fixtures/auth.user.json
django-admin.py dumpdata -n --format=json --indent=2 hawknews > fixtures/hawknews.json
django-admin.py dumpdata -n --format=json --indent=2 lth > fixtures/lth.json
django-admin.py dumpdata -n --format=json --indent=2 faq > fixtures/faq.json
django-admin.py dumpdata -n --format=json --indent=2 blog > fixtures/blog.json
django-admin.py dumpdata -n --format=json --indent=2 photos > fixtures/photos.json
django-admin.py dumpdata -n --format=json --indent=2 links > fixtures/links.json
django-admin.py dumpdata -n --format=json --indent=2 members > fixtures/members.json
django-admin.py dumpdata -n --format=json --indent=2 runs > fixtures/runs.json
django-admin.py dumpdata -n --format=json --indent=2 sponsors > fixtures/sponsors.json
django-admin.py dumpdata -n --format=json --indent=2 races > fixtures/races.json

django-admin.py dumpdata -n --format=json --indent=2 flickr > fixtures/flickr.json
django-admin.py dumpdata -n --format=json --indent=2 twitter > fixtures/twitter.json

django-admin.py dumpdata -n --format=json --indent=2 races.race > fixtures/races.race.json
django-admin.py dumpdata -n --format=json --indent=2 races.news > fixtures/races.news.json
