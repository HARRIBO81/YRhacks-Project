$(document).ready(function()
{
    $("#search").click(function()
    {
        var req = $.get("/maps/" + $("#query").val());
        req.done(function(data){
            $("#url").attr("href", data.result);
        })
    })
})