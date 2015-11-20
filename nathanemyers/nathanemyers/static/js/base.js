$(document).ready(function() {
  var header = $('.header');
  var header_perm = $('.header-perm');
  var header_pos = header_perm.position().top;

  $(window).scroll(function() {
    var window_pos = $(window).scrollTop();
    if (window_pos >= header_pos) {
      header.addClass('stick');
    } else {
      header.removeClass('stick');
    }
  });

});
