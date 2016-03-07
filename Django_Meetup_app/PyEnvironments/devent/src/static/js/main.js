
$(function() {
    // This is for the comment button on the Your list View.
    // It will show and hide the comment and also change the text of the button
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

    // This converts the epoch time stamp to a human readable format
    // Takes the el object and turns it to a string then a number.
    // Sets it to a date and turns the timestamp to human readable.
    $('.datetime small').each(function(index, el) {
        JSON.stringify(el)
        var date = Number(el.innerHTML)
        var myDate = new Date(date);
        $(this).text(myDate.toLocaleString())
    });
});
