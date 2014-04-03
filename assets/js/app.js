/* LazyLoad instance */
$('img').each(function(){
  $(this).attr('src', $(this).attr('data-src'));
});
