function check_nav(){
    if (nav_div){
        document.getElementById(nav_div).className = 'active';
    }
}

changes_list = new Array();
changes = 0;

function stage_for_changes(pk){
    if ($.inArray(pk, changes_list) == -1){
        changes_list[changes] = pk;
        changes++;
    }
    document.getElementById('btn-save').style.display='block';
}

var data = {
        messages: []
    };


function make_changes(){
    
    if (changes == 0){
            return 0;
    }

    document.getElementById('btn-save').style.display='';
    document.getElementById('status-messages').innerHTML = "Preparing Data for transmission...";

    for (var i = 0; i < changes; i++){
        pk = changes_list[i];
        data.messages.push({ 
            "pk": pk,
            "location"  : document.getElementById('location'+pk).innerHTML,
            "source"  : document.getElementById('source'+pk).innerHTML,
            "target"  : document.getElementById('target'+pk).innerHTML,
            });
    }

    document.getElementById('status-messages').innerHTML = "Sending Ajax Request...";

    $.ajaxSetup({ 
        beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
        } 
    });   
 
    $.ajax({
            url: '/poeditor/update/',
            type: 'post',
            dataType: 'json',
            data: JSON.stringify(data),
    });

    $('#status-messages').html('Successfully Updated Databse');

}
