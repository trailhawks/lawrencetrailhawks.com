
$(document).ready(function() {
    /* LazyLoad instance */
    $('img').each(function(){
      $(this).attr('src', $(this).attr('data-src'));
    });

    $('.show-more a').click(function(){
        $('.past-races .col-md-12').css('max-height', '100%');
        $('.past-races .col-md-12').css('overflow', 'visible');
        $('.show-more').css('display', 'none');
    });
});
