

function build_chart(select_target, bounds) {

  var svgContainer = d3.select('.chart').append('svg')
    .attr('width', 500)
    .attr('height', 500);

  var lineFunction = d3.svg.line()
    .x(function(d) {return d.week * 50;})
    .y(function(d) {return d.rank * 5;})
    .interpolate('linear');

  function draw_line(chart, team) {
    svgContainer.append('path')
      .attr('d', lineFunction(team))
      .attr('stroke', 'blue')
      .attr('stroke-width', 2)
      .attr('fill', 'none');
  }

  $.getJSON("/nba/api/rankings/2016", function(data) {
    data = data;
    var x = d3.scale.linear()
      .range([0, bounds.plot.width]);
    var y = d3.scale.linear()
      .range([0, bounds.plot.height]);


    for (var team in data.rankings) {
      draw_line(svgContainer, data.rankings[team]);
    }
  });

}

