function build_chart(selector) {
  var border_left = 120;
  var border_right = 10;
  var border_top = 10;
  var border_bottom = 40;

  var svgContainer = d3.select(selector);
  var width = parseInt(svgContainer.style('width'));
  var height = parseInt(svgContainer.style('height'));

  var max_weeks = Math.floor(width / 100);

  if (max_weeks > 18) {
    max_weeks = 18;
  }

  var x = d3.scale.linear()
    .domain([0, max_weeks])
    .range([border_left, width - border_right]);
  var y = d3.scale.linear()
    .domain([1,30])
    .range([border_top, height - border_bottom]);

  var line = d3.svg.line()
    .x(function(d) {return x(d.week);})
    .y(function(d) {return y(d.rank) ;})
    .interpolate('linear');

  var xAxis = d3.svg.axis()
    .ticks(max_weeks)
    .scale(x);


  var lineClass = function(data) {
    var classes = 'team ';
    // can't have a css class named 76ers
    classes += data.name === '76ers' ? 'philly' : data.name;
      if (data.conference === 'Eastern') {
        classes += ' eastern';
      }
      if (data.conference === 'Western') {
        classes += ' western';
      }
      return classes;
  };

  $.getJSON("/nba/api/rankings/2016", function(data) {
    data = data.results;
    var black_warriors = function() {
      data[0].color = '#000';
    };

    var lines = svgContainer.selectAll('path')
      .data(data)
      .enter().append('path')
      .attr('d', function(d) { return line(d.rankings); })
      .attr('class', lineClass)
      .attr('fill', 'none')
      .attr('stroke-width', 2);


    var bubbles = svgContainer.selectAll('circle')
      .data(data)
      .enter().append('circle')
      .attr('cx', function(d) {
        return x(d.rankings[d.rankings.length-1].week);
      })
      .attr('cy', function(d) {
        return y(d.rankings[d.rankings.length-1].rank);
      })
      .attr('r', '5')
      .attr('class', lineClass);

    var labels = svgContainer.selectAll('text')
      .data(data)
      .enter()
      .append('text')
      .attr('x', function(d) {return border_left - 5;}) // -5 to add margin
      .attr('y', function(d) {
        return y(d.rankings[0].rank) + 5; // +5 to center text
      })
      .attr('class', lineClass)
      .style('text-anchor', 'end')
      .text(function(d) {return d.name;});

    svgContainer.append('g')
      .attr('class', 'axis')
      // -10 for 10px border
      .attr('transform', 'translate(0,' + ( height - (border_bottom - 10) ) + ')')
      .call(xAxis);

      svgContainer.append('text')
        .attr('x', width/2)
        .attr('y', height)
        .text('Week');
  });

}
