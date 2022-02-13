//-----------------------------------------------------------------------------
function bubble_chart_01(b1,b2,id) {
    var trace1 = {
        x: b1,
        y: b2,
        mode: 'markers',
        marker: {
            size: 8
        }
    };

    var data = [trace1];

    var layout = {
        title: 'Marker Size',
        showlegend: false,
    };

    return Plotly.newPlot(id, data, layout);
}

//-----------------------------------------------------------------------------

function bubble_chart_02(xlist,ylist,id) {

    var colors = [];
    for (var i = 0; i < ylist.length; i++) {
        var color = [
            'rgba(1,118,11,0.9)',//green dark
            'rgba(251,3,3,0.9)']; //red dark
        if (ylist[i] > 0) {
            colors[i] = color[0];
        }
        else if (ylist[i] < 0) {
            colors[i] = color[1];
        }
    }
    var data = [{
        x: xlist,
        y: ylist,
        mode: 'markers',
        marker: {
            color: colors,
            opacity: [1, 0.8, 0.6, 0.4],
            size: 8
        }
    }];

    // Define Layout
    // var layout = {
    //     xaxis: {title: "نماد"},
    //     // yaxis: {range: [-10, 10], title: "دامنه"},
    //     yaxis: {title: "دامنه"},
    //     title: "",
    //     font: {size: 12, family: "iranyekan", color: "gray"},
    // };
    var layout = {
        title: 'Marker Size',
        showlegend: false,
        // height: 600,
        // width: 600
    };
    // var config = {
    //     responsive: true,
    //     scrollZoom: true,
    //     // maintainAspectRatio: true
    // };

    return Plotly.newPlot(id, data, layout, config);
}
//--------------------------------------------------------------------------------------

