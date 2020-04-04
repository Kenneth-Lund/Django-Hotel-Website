// This function responds to any of the clicked hotel room preview images
$(document).on('click', '.preview-cell-outer', function(e) {
    var src = $(this).attr("src");

    // Requests list of preview images for hotel room, updates HTML with new list
    $.ajax({
        type: "GET",
        url: '/home-page/update-large-preview/id=' + id + '/',
        success: function (result) {
            $('.preview_inner_table').html(result);
        },
    });
});