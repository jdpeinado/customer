/* jquery example */
$(function(){
    $('#menu a[href*="' + location.pathname.split("/")[1] + '"][class!="noactive"]').addClass('active');
});