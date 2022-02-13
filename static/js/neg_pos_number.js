$('.percent_number').each(function() {
    var cellvalue = $(this).html();
    if ( cellvalue < 0) {
        $(this).wrapInner('<strong class="negetive" dir="ltr"></strong>');
    }
    if ( cellvalue > 0) {
        $(this).wrapInner('<strong class="posetive" dir="ltr"></strong>');
    }
});