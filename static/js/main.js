$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")
    
    create_item();
});

function create_item() {
    console.log("create_item is working!")

    $.ajax({
        url : "create_item/",
        type : "POST",
        data : { item_title : $('#input-title').val() },

        success : function(json) {
            $('#post-text').val('');
            console.log(json);
            console.log("success");
            location.reload(true);

        },
    })

    console.log($('#input-title').val())
};

function delete_function(item_title){
    console.log("DELETE FUNCTION")

    $.ajax({
        url : "delete_item/",
        type : "POST",
        data : { item_title : item_title },

        success : function(json) {
            $('#post-text').val('');
            console.log(json);
            console.log("success");
            location.reload(true);
        },
    })

    console.log(item_title)
}

function check_function(item_title){
    console.log("CHECK FUNCTION")
    if ($('input.form-check-input').is(':checked')) {
        $.ajax({
            url : "update_item/",
            type : "POST",
            data : { item_title : item_title },
    
            success : function(json) {
                $('#post-text').val('');
                console.log(json);
                console.log("success");
            },
        })
    }
}