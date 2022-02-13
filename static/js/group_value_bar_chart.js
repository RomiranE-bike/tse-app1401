function barChart(group_lables,group_values,group_percent,id) {

    var colors = [];
    for(var i = 0; i < group_percent.length; i++){
        var color=['rgba(5,170,100,0.6)', 'rgba(250,80,80,0.6)'];
        if(group_percent[i]>0){colors[i]=color[0];}
        else if (group_percent[i]<=0){colors[i]=color[1];group_values[i]=group_values[i]*-1}
    }
    var data = [{
        x: group_lables,
        y: group_values,
        /*hole:0.7,*/
        type: "bar",
        // orientation:"h",
        marker: {color:colors},
        // marker:{color: ['rgba(4,170,109,0.5)']},
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
    };
    return Plotly.newPlot(id, data, layout, config);
}
