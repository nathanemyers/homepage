

function build_chart(select_target, bounds) {
  var border_left = 120;
  var border_right = 10;
  var border_top = 10;
  var border_bottom = 10;
  var width = 900;
  var height = 500;

  var x = d3.scale.linear()
    .range([border_left, width - ( border_left + border_right )]);
  var y = d3.scale.linear()
    .range([border_top, height - ( border_top + border_bottom )]);

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
      .attr('x', function(d) {return border_left - 5;}) // -5 to add margin
      .attr('y', function(d) {
        return y(d.rankings[0].rank/30) + 5; // +5 to center text
      })
      .style('text-anchor', 'end')
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

