var send_data = {}

$(document).ready(function () {
    resetFilters();
    getBuildings();
    getAPIData();

    // on selecting the building option
    $('#search_by_building').on('change', function () {
        // update the selected building
        if(this.value == "all")
            send_data['building'] = "";
        else
            send_data['building'] = this.value;
        getAPIData();
    });

    // on filtering the options input
    $('#search_by_options').on('change', function () {
        // get the api data of updated options
        if(this.value == "all")
            send_data['in_use'] = "";
        else
            send_data['in_use'] = this.value;
        getAPIData();
    });

    $('genipv6').on('click', function () {
        //generate ipv6 string
        //let building = document.getElementById('id_building').value

        //if (building == "")

        console.log("hello")



    })
})


/**
    Function that resets all the filters   
**/
function resetFilters() {
    $("#search_by_building").val("all");
    $("#search_by_options").val("all");

    send_data['building'] = '';
    send_data['in_use'] = '';
    send_data['format'] = 'json';
}

/**.
    Utility function to showcase the api data 
    we got from backend to the table content
**/
function putTableData(result) {
    let row;
    if(result.length > 0){
        $("#list_data").show();
        $("#ip_listing").html(""); 
        $.each(result, function (a, b) {
            row = "<tr> <td>" + b.address + "</td>" +
                "<td>" + b.ip_type + "</td>" +
                "<td title=\"" + b.building + "\">" + b.building + "</td>" +
                "<td title=\"" + b.hostname + "\">" + b.hostname + "</td>" +
                "<td>" + b.in_use + "</td></tr>"
            $("#ip_listing").append(row);   
        });
    }
}

function getAPIData() {
    let url = $('#list_data').attr("url")
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        success: function (result) {
            putTableData(result);
            console.log("in api data")
        },
        error: function (response) {
            $("#list_data").hide();
        }
    });
}

function getBuildings() {
    let url = $("#search_by_building").attr("url");
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            building_option = "<option value='all' selected>All</option>";
            $.each(result["buildings"], function (a, b) {
                building_option += "<option>" + b + "</option>"
            });
            $("#search_by_building").html(building_option)
        },
        error: function(response){
            console.log(response)
        }
    });
}