var editor; // use a global for the submit and return data rendering in the examples

$(document).ready(function() {
    editor = new $.fn.dataTable.Editor( {
        ajax: "#",
        table: "#table-new-hire",
        fields: [ {
                label: "New Hire ID:",
                name: "new_hire_id"
            }, {
                label: "New Hire Name:",
                name: "new_hire_name"
            }, {
                label: "Manager ID:",
                name: "manager_id"
            }, {
                label: "Manager Name:",
                name: "manager_name"
            }, {
                label: "Onboard Time:",
                name: "onboard_time",
                type: "datetime"
            }, {
                label: "Created Time:",
                name: "created_time",
                type: "datetime"
            },
        ]
    } );

    // Activate an inline edit on click of a table cell
    $('#table-new-hire').on( 'click', 'tbody td:not(:first-child)', function (e) {
        editor.inline( this );
    } );

    $('#table-new-hire').DataTable( {
//        dom: "Bfrtip",
        ajax: "#",
        columns: [
            { data: "DT_RowId"},
            { data: "new_hire_id" },
            { data: "new_hire_name" },
            { data: "manager_id" },
            { data: "manager_name" },
            { data: "onboard_time" },
            { data: "created_time" },
            { data: "age" },
            { data: "status" },
        ],
        select: {
            style:    'os',
            selector: 'td:first-child'
        },
        buttons: [
            { extend: "create", editor: editor },
            { extend: "edit",   editor: editor },
            { extend: "remove", editor: editor }
        ]
    } );
} );