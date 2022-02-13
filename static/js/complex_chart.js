function complexChart(xlist1,ylist1,a,id,mpe,gpe) {
    var market_average_pe = int(mpe);
    var group_average_pe = int(gpe);

    var colors = [];
    for(var i = 0; i < ylist1.length; i++){
        var color=[
            'rgba(1,118,11,0.9)',//green dark
            'rgba(149,225,155,0.5)',//green ligth
            'rgba(77,196,241,0.5)',//blue ligth
            'rgba(254,105,105,0.5)',//red ligth
            'rgba(251,3,3,0.9)',]; //red dark


        if(ylist1[i]>= 1 & ylist1[i]<= 7){colors[i]=color[0];}
        else if (ylist1[i] > 7 & ylist1[i]< market_average_pe ){colors[i]=color[1];}
        else if (ylist1[i]> market_average_pe ){colors[i]=color[3];}
        else if (ylist1[i]< 1 ){colors[i]=color[4];}
    }

    // Generate values
    var ylist2 = [];
    var ylist3 = [];

    for (var i = 0; i <= xlist1.length; i++) {
        ylist2[i]= market_average_pe;
        ylist3[i]= group_average_pe;
    }
    // Define Data
    var data = [
        {x: xlist1, y: ylist1, mode: "markers",name:'نمادp/e',marker:{color:colors,size:8}},
        {x: xlist1, y: ylist2, mode: "lines",name:'بازارp/e',marker:{color:'rgba(254,105,105,0.8)'}},//red ligth
        {x: xlist1, y: ylist3, mode: "lines",name:'گروهp/e',marker:{color:'rgba(77,196,241,0.8)'}}//blue ligth

    ];

    // Define Layout
    var layout = {
        xaxis: { title: "نماد"},
        yaxis: { title: "P/E"},
        title: "پراکندگی p/e",
        font: {size: 12,family: "iranyekan", color: "gray"},
    };
    var config = {
        responsive: true,
        scrollZoom: true,
    }

    // Display using Plotly
    return Plotly.newPlot(id, data, layout,config);
}
var mpe = {{market_average_pe}};
var gpe = {{group_selected_items.get('group_pe_average')}}[a];

var group1_xValues = [{% for i in range(group_selected_items.get('group_sort_list')[0]|length) %}
'{{group_selected_items.get("group_sort_list")[0][i].get("symbol")}}', {% endfor %} ];
var group1_yValues = [{% for i in range(group_selected_items.get('group_sort_list')[0]|length) %}
{{group_selected_items.get("group_sort_list")[0][i].get('pe')}}, {% endfor %} ];
var group2_xValues = [{% for i in range(group_selected_items.get('group_sort_list')[1]|length) %}
'{{group_selected_items.get("group_sort_list")[1][i].get("symbol")}}', {% endfor %} ];
var group2_yValues = [{% for i in range(group_selected_items.get('group_sort_list')[1]|length) %}
{{group_selected_items.get("group_sort_list")[1][i].get('pe')}}, {% endfor %} ];
var group3_xValues = [{% for i in range(group_selected_items.get('group_sort_list')[2]|length) %}
'{{group_selected_items.get("group_sort_list")[2][i].get("symbol")}}', {% endfor %} ];
var group3_yValues = [{% for i in range(group_selected_items.get('group_sort_list')[2]|length) %}
{{group_selected_items.get("group_sort_list")[2][i].get('pe')}}, {% endfor %} ];
var group4_xValues = [{% for i in range(group_selected_items.get('group_sort_list')[3]|length) %}
'{{group_selected_items.get("group_sort_list")[3][i].get("symbol")}}', {% endfor %} ];
var group4_yValues = [{% for i in range(group_selected_items.get('group_sort_list')[3]|length) %}
{{group_selected_items.get("group_sort_list")[3][i].get('pe')}}, {% endfor %} ];
var group5_xValues = [{% for i in range(group_selected_items.get('group_sort_list')[4]|length) %}
'{{group_selected_items.get("group_sort_list")[4][i].get("symbol")}}', {% endfor %} ];
var group5_yValues = [{% for i in range(group_selected_items.get('group_sort_list')[4]|length) %}
{{group_selected_items.get("group_sort_list")[4][i].get('pe')}}, {% endfor %} ];


complexChart(group1_xValues,group1_yValues,0,'myPlot61',mpe,gpe)
complexChart(group2_xValues,group2_yValues,1,'myPlot62',mpe,gpe)
complexChart(group3_xValues,group3_yValues,2,'myPlot63',mpe,gpe)
complexChart(group4_xValues,group4_yValues,3,'myPlot64',mpe,gpe)
complexChart(group5_xValues,group5_yValues,4,'myPlot65',mpe,gpe)