
function pieChart(list1,list2,id) {

    var data = [{
        labels: list1,
        values: list2,
        hole: 0.5,
        type: "pie",
        textinfo: 'values',
        textposition: 'none'
    }];
    var layout = {
        title: "  ",
        font: {
            size: 12,
            family: "iranyekan",
            color: "gray",
        },
        showlegend: true,
    };

    var config = {
        responsive: true,
        scrollZoom: true,
    }
    return Plotly.newPlot(id,data,layout,config);
}









// <!---------------------------------------------group list pie chart-------------------------------------------->

