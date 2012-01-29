from syncr.twitter.models import Tweet


def get_latest():
    tweets = Tweet.objects.all().order_by('-pub_time')

    return {
        'tweets': tweets,
    }
