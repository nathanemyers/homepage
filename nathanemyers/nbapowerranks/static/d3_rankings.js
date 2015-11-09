

function build_chart(select_target, bounds) {

  var x = d3.scale.linear()
    .range([0, bounds.plot.width]);
  var y = d3.scale.linear()
    .range([0, bounds.plot.height]);

  var svgContainer = d3.select('.chart').append('svg')
    .attr('width', bounds.plot.width)
    .attr('height', bounds.plot.height);

  var lineFunction = d3.svg.line()
    .x(function(d) {return x(d.week/10);})
    .y(function(d) {return y(d.rank/30) ;})
    .interpolate('linear');

  function draw_line(team) {
    svgContainer.append('path')
      .attr('d', lineFunction(team.rankings))
      .attr('stroke', 'blue')
      .attr('stroke-width', 2)
      .attr('fill', 'none');
  }

  function draw_labels(teams) {
    text = svgContainer.selectAll('text')
      .data(teams)
      .enter()
      .append('text');

    text
      .attr('x', function(d) {return 0;})
      .attr('y', function(d) {
        return y(d.rankings[0].rank/30);
      })
      .text(function(d) {return d.name;});
  }

  $.getJSON("/nba/api/rankings/2016", function(data) {
    data = data.results;


    for (var i=0; i < data.length; i++) {
      draw_line(data[i]);
    }
    draw_labels(data);
  });

}

