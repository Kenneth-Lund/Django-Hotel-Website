// This function responds to any of the clicked hotel room listings
$(document).on('click', '.room-cell-outer', function(e) {
    var id = $(this).attr("id");

    // Requests list of preview images for hotel room, updates HTML with new list
    $.ajax({
        type: "GET",
        url: '/home-page/update-preview-list/id=' + id + '/',
        success: function (result) {
            $('.preview_inner_table').html(result);
        },
    });
});