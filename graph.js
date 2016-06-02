function plotGraph(id, dIdx, xLabel, yLabel, yTick, options){
    var self = this;

    if (options === undefined) options = {};
    if (options.yDomainMod === undefined) options.yDomainMod = 1.1;

   
    
    if(options.yDomain !== undefined){
      boundaries.y = options.yDomain;
    }
   
    
    var wH = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;

    var boxW = parseInt(d3.select('#'+id).style('width'), 10);
    var boxH = wH/3 - 50;

    var margin = {top: 20, right: 50, bottom: 55, left: 50},
        width = boxW - margin.left - margin.right,
        height = boxH - margin.top - margin.bottom;
        

    self.width = width;
    self.height = height;


    xTickCount = width / 100;

    this.axisUpdateFns = [];
    this.updateAxes = function(){
        for(var i = 0; i < self.axisUpdateFns.length; i++){
            self.axisUpdateFns[i].apply(self);
        }
    }
    

   
    
        
    
        var xScaleNum = this.xScaleNum = d3.scale.linear()
            .range([0, width])
            .domain([0, 1]);


        self.x = xScaleNum;

    


    var yDomainMod = options.yDomainMod;

    var y = self.y = d3.scale.linear()
        .domain([-1, 1])
        .range([height, 0]);

    var xAxis = this.xAxis = d3.svg.axis()
        .scale(this.x)
        .orient("bottom")
        
        .ticks(xTickCount);
        //.tickFormat(blockToTime);



    var yAxis = this.yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .tickFormat(yTick)
        .innerTickSize(-width)
        .outerTickSize(0)
        .tickPadding(10);

    
    var line = d3.svg.line()
        .x(function(d) { return self.x(d[0]); })
        .y(function(d) { return self.y(d[dIdx]); });



    /*
    var svg = d3.select("#graphBox").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");*/

    var svgTop = d3.select("#"+id)
       .append("svg")
    .attr("width", width + margin.left + margin.right)
       .attr("height", height + margin.top + margin.bottom)
       .classed("graphSvg", true);
     
    var svg = svgTop.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        

    svg.append("defs").append("clipPath")
    .attr("id", "clip" + id)
  .append("rect")
    .attr("width", width)
    .attr("height", height);


    console.log(this.xAxis)
    var xAxisElem = this.xAxisElem = svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(this.xAxis);

    var xAxisLabel = this.xAxisLabel = xAxisElem.append("text")
      .attr("y", 32)
      .attr("x", width/2)
      .text(xLabel);

    this.axisUpdateFns.push(function(){
       self.xAxisElem.call(self.xAxis);
    });






    var yAxisElem = this.yAxisElem = svg.append("g")
      .attr("class", "y axis")
      .call(yAxis);
    this.axisUpdateFns.push(function(){
       self.yAxisElem.call(self.yAxis);
    });
    
    yAxisElem.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text(yLabel);
      
    

    self.replot = function(line){
      var timeFormat = d3.time.format("%M:%S")
      self.xAxis.tickFormat(function(n){
        n = n - line.data[0][0];
        return timeFormat(new Date(n))
        });
      
      
      self.x.domain([line.data[0][0], line.data[line.data.length-1][0]])
      
      self.y.domain(d3.extent(line.data, function(l){return l[dIdx]}))
      self.updateAxes();
      
      svg.selectAll("path").remove();
      self.drawLines([line]);
    }

    self.drawLines = function(lines){
      lines.forEach(function(thisLine, i){
          
          
          var colourAttrib = "stroke";
          
          if (thisLine.chart == "line"){
              var p =svg.append("path")
                .datum(thisLine.data)
                .attr("class", "line")
                .attr("clip-path", "url(#clip" + id + ")")
                .attr("d", line);
              
          }
          if(thisLine.colour !== undefined){
              p.style(colourAttrib, thisLine.colour);
          }

      });
    };

}



function genLine(data, name, colour, textLabel){

   

    return genLineDict(data, name, colour, textLabel);
}

function genLineDict(data, name, colour, textLabel){

    return {
        data: data,
        name: name,
        colour: colour,
        textLabel: textLabel,
        chart: "line",
        position: "l"
    };
}