
function build_chart(select_target, bounds) {
  var border_left = 120;
  var border_right = 10;
  var border_top = 10;
  var border_bottom = 40;
  var width = 900;
  var height = 600;

  var x = d3.scale.linear()
    .domain([0,5])
    .range([border_left, width - ( border_left + border_right )]);
  var y = d3.scale.linear()
    .domain([1,30])
    .range([border_top, height - ( border_top + border_bottom )]);

  var svgContainer = d3.select('.chart').append('svg')
    .attr('width', width)
    .attr('height', height);

  var line = d3.svg.line()
    .x(function(d) {return x(d.week);})
    .y(function(d) {return y(d.rank) ;})
    .interpolate('linear');

  var xAxis = d3.svg.axis()
    .ticks(5)
    .scale(x);


  $.getJSON("/nba/api/rankings/2016", function(data) {
    data = data.results;

    var lines = svgContainer.selectAll('path')
      .data(data)
      .enter().append('path')
      .attr('d', function(d) { return line(d.rankings); })
      .attr('stroke', function(d) {return d.color;})
      .attr('fill', 'none')
      .attr('stroke-width', 2);

    var labels = svgContainer.selectAll('text')
      .data(data)
      .enter()
      .append('text')
      .attr('x', function(d) {return border_left - 5;}) // -5 to add margin
      .attr('y', function(d) {
        return y(d.rankings[0].rank) + 5; // +5 to center text
      })
      .style('text-anchor', 'end')
      .text(function(d) {return d.name;});

    svgContainer.append('g')
      .attr('class', 'axis')
      .attr('transform', 'translate(0,' + ( height - border_bottom ) + ')')
      .call(xAxis);

      svgContainer.append('text')
        .attr('x', width/2)
        .attr('y', height - border_bottom + 35)
        .text('Week');
  });

}

