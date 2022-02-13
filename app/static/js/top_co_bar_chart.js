function top_co_barChart(list1,list2,id) {


    var colors = [];
    for(var i = 0; i < list2.length; i++){
        var color=['rgba(5,170,100,0.6)', 'rgba(250,80,80,0.6)'];
        if(list2[i]>0){colors[i]=color[0];}
        else if (list2[i]<=0){colors[i]=color[1];}
    }
    var data = [{
        x: list1,
        y: list2,
        /*hole:0.7,*/
        type: "bar",
        marker: {color:colors},
        // // orientation:"h",
        // // marker:{color: ['rgba(4,170,109,0.5)']},
        // marker: {color: 'rgba(26,111,185,0.6)', line: {color: 'rgba(26,111,185,0.6)', width: 1}},
    }];
    var layout = {
        title: "  ",
        font: {size: 12,family: "iranyekan", color: "gray"},
    };
    var config = {
        responsive: true,
        scrollZoom: true,
        // maintainAspectRatio: true
    }
    return Plotly.newPlot(id, data, layout, config);
}

