from django.views.generic import dates

from .models import Post


class PostMixin(object):
    queryset = Post.objects.public()
    date_field = 'publish'
    navitem = 'blog'


class PostArchive(PostMixin, dates.ArchiveIndexView):
    make_object_list = True
    paginate_by = 10


class PostYearArchive(PostMixin, dates.YearArchiveView):
    pass


class PostMonthArchive(PostMixin, dates.MonthArchiveView):
    pass


class PostDayArchive(PostMixin, dates.DayArchiveView):
    pass


class PostDateDetail(PostMixin, dates.DateDetailView):
    queryset = Post.objects.all()
