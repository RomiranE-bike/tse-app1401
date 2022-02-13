//-------------------------donut Chart-------------------------------
function donutChart(list,id) {

    var labels = [" نماد های مثبت", " نماد های  منفی"];
    /*var values = [100, 235];*/
    var values = list;

    var layout = {
        title: "  ",
        font: {
            size: 14,
            family:"iranyekan",
            color:"gray",
        },
        // legend:{
        //     xanchor:"center",
        //     yanchor:"center",
        //     y:0, // play with it
        //     x:0.5 , // play with it
        //     orientation: 'h'
        // }
    };

    // var layout = {
    //     showlegend: true,
    //     legend: {
    //         x: 1,
    //         xanchor: 'right',
    //         y: 30
    //     }
    // };
    // var layout = {
    //         showlegend: true,
    //         legend: {
    //              xanchor: 'center',
    //              x: 0.5,
    //              orientation: 'h'
    //     }
    //    legend: {orientation: 'v', side: 'top'}
    // };

    var data = [{
        labels: labels,
        values: values,
        hole: 0.7,
        type: "pie",
        marker: {colors: ['rgba(5,170,100,1)', 'rgba(250,80,80,1)']},
        textinfo: 'values',
        textposition: 'outside'


    }];

    var config = {

        responsive: true,
        /* maintainAspectRatio: true*/
    }

    /*Plotly.newPlot("myPlot1", data, layout);*/
    return Plotly.newPlot(id, data, layout,config,{scrollZoom: true});
}


