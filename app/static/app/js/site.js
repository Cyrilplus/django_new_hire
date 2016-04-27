$(function(){
    $('#table-new-hire').DataTable({
    "processing": true,
    "ajax": "/get-new-hire/",
    "columns":[
        {"data":"pk"},
        {"data":"fields.new_hire_id"},
        {"data":"fields.new_hire_name"},
        {"data":"fields.manager_id"},
        {"data":"fields.manager_name"},
    ]
    });
//    $.ajax({
//        type: 'POST',
//        url:'/get-new-hire/',
//        dataType: 'json',
//        success: function(data){
//            $.each(data,function(key,value){
//                alert(key + ':' + value);
//            });
//        },
//        error: function(){
//            alert("error")
//        }
//    });
});