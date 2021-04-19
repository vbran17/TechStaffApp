$(document).ready(function() {
    $('#example').DataTable( {
        "order": [[ 3, "desc" ]],
        "info": false,
        "language": {
            "search": "",
            "searchBuilder": {
                button: 'searchBuilder'
            }
        },
        "buttons":[
            'SearchBuilder'
        ],
        "paging": false
    } );
} );
