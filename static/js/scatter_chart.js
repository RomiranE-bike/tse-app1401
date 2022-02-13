
function scatterChart(xlist,ylist,id) {

    var colors = [];
    for(var i = 0; i < ylist.length; i++){
        var color=[
            'rgba(1,118,11,0.9)',//green dark
            'rgba(149,225,155,0.5)',//green ligth
            'rgba(77,196,241,0.5)',//blue ligth
            'rgba(254,105,105,0.5)',//red ligth
            'rgba(251,3,3,0.9)',]; //red dark
        if (ylist[i] >= 3){colors[i]=color[0];}
        else if (ylist[i]> 0 & ylist[i]< 3){colors[i]=color[1];}
        else if(ylist[i] == 0){colors[i]=color[2];}
        else if (ylist[i]<0 & ylist[i]> -3){colors[i]=color[3];}
        else if (ylist[i]<= -3){colors[i]=color[4];}
    }

    // Define Data
    var data = [
        {x: xlist, y: ylist, mode: "markers",name:'قیمت پایانی%',marker:{color:colors,size:8}},
        // {x: xlist, y: ylist, mode: "lines"}
    ];

    // Define Layout
    var layout = {
        xaxis: { title: "نماد"},
        // yaxis: {range: [-10, 10], title: "دامنه"},
        yaxis: { title: "دامنه"},
        title: "",
        font: {size: 12 ,family: "iranyekan", color: "gray"},
    };
    var config = {
        responsive: true,
        scrollZoom: true,
        // maintainAspectRatio: true
    };

    // Display using Plotly
    return Plotly.newPlot(id, data, layout,config);
}

