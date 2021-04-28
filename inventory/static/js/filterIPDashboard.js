// var send_data = {}

// $(document).ready(function () {
//     resetFilters();
//     getBuildings();
//     getAPIData();

//     // on selecting the building option
//     $('#search_by_building').on('change', function () {
//         // update the selected building
//         if(this.value == "all")
//             send_data['building'] = "";
//         else
//             send_data['building'] = this.value;
//         getAPIData();
//     });

//     // on filtering the options input
//     $('#search_by_options').on('change', function () {
//         // get the api data of updated options
//         if(this.value == "all")
//             send_data['in_use'] = "";
//         else
//             send_data['in_use'] = this.value;
//         getAPIData();
//     });

//     $('#searchField').on('change', function () {
//         send_data['search'] = this.value;
//         getAPIData();
//     });
// })


// /**
//     Function that resets all the filters   
// **/
// function resetFilters() {
//     $("#search_by_building").val("all");
//     $("#search_by_options").val("all");

//     send_data['building'] = '';
//     send_data['in_use'] = '';
//     send_data['format'] = 'json';
// }

// /**.
//     Utility function to showcase the api data 
//     we got from backend to the table content
// **/
// function putTableData(result) {
//     let row;
//     let in_use_value;
//     if(result.length > 0){
//         $("#list_data").show();
//         $("#ip_listing").html(""); 
//         $.each(result, function (a, b) {
//             if( b.in_use ) { in_use_value = "Assigned"} 
//             else { in_use_value = "Unassigned" } 
//             row = "<tr> <td>" + b.address + "</td>" +
//                 "<td>" + b.ip_type + "</td>" +
//                 "<td title=\"" + b.building + "\">" + b.building.name + "</td>" +
//                 "<td title=\"" + b.hostname + "\">" + b.hostname + "</td>" +
//                 "<td>" + in_use_value + "</td></tr>" +
//                 "<a href=\"" + /itemdetails/{{equipment.id}}/ + "\"><button>" + View +  "</button></a>"
//             $("#ip_listing").append(row);   
//         });
//     }
//     else{
//         console.log("here")
//         $("#list_data").hide();
//     }
// }

// function getAPIData() {
//     let url = $('#list_data').attr("url")
//     $.ajax({
//         method: 'GET',
//         url: url,
//         data: send_data,
//         success: function (result) {
//             putTableData(result);
//         },
//         error: function (response) {
//             $("#list_data").hide();
//         }
//     });
// }

// function getBuildings() {
//     let url = $("#search_by_building").attr("url");
//     $.ajax({
//         method: 'GET',
//         url: url,
//         data: {},
//         success: function (result) {
//             building_option = "<option value='all' selected>All</option>";
//             $.each(result["buildings"], function (a, b) {
//                 building_option += "<option>" + b + "</option>"
//             });
//             $("#search_by_building").html(building_option)
//         },
//         error: function(response){
//             console.log(response)
//         }
//     });
// }

function openRegisterEditModal(event, register_id) {
        var modal = $('#modal_register_edit');
        // var url = $(event.target).closest('a').attr('href');
        var url = $("#link").attr("href")
        modal.find('.modal-body').html('').load(url, function() {
            modal.modal('show');
            formAjaxSubmit(popup, url);
        });
    }