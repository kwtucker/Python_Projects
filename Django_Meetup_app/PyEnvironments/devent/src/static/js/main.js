
$(function() {
    $('.btn').addClass('comShow')
    $('.comShow').click(function(e) {
        e.preventDefault();
        $(this).toggleClass('comShow comHide');
        if($(this).hasClass('comHide')) {

            $(this).text('Hide Comment');
        } else {
            $(this).text('Show Comment');
        }
    });

    $('.datetime small').each(function(index, el) {
        JSON.stringify(el)
        var date = Number(el.innerHTML)
        var myDate = new Date(date);
        $(this).text(myDate.toLocaleString())
    });
});
