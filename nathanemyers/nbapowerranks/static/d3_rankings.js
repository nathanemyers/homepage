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

  // can't have a css class named 76ers
  var team2class = function(team) {
    if (team === '76ers') {
      return 'philly';
    } else {
      return team;
    }
  };

  var lineClass = function(data) {
    var classes = 'team ';
    classes += team2class(data.name);
      if (data.conference === 'Eastern') {
        classes += ' eastern';
      }
      if (data.conference === 'Western') {
        classes += ' western';
      }
      return classes;
  };

  var tooltip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
      return d.summary;
    });
  svgContainer.call(tooltip);

  $.getJSON("/nba/api/rankings/2016", function(data) {
    data = data.results;
    var black_warriors = function() {
      data[0].color = '#000';
    };

    var team_lines = svgContainer.selectAll('g')
      .data(data)
      .enter().append('g');

    var color_lines = team_lines
      .append('path')
        .attr('d', function(d) { return line(d.rankings); })
        .attr('class', lineClass);

    var line_handles = team_lines
      .append('path')
        .attr('d', function(d) { return line(d.rankings); })
        .attr('class', 'line-handle')
        .on('mouseenter', function(d) {
          $('.chart').addClass('highlight ' + team2class(d.name));
        })
        .on('mouseout', function(d) {
          $('.chart').removeClass('highlight ' + team2class(d.name));
        });


    var bubbles = svgContainer.selectAll('circle')
      .data(data)
      .enter().append('circle')
        .attr('cx', function(d) {
          return x(d.rankings[d.rankings.length-1].week);
        })
        .attr('cy', function(d) {
          return y(d.rankings[d.rankings.length-1].rank);
        })
        .on('mouseenter', function(d) {
          $('.chart').addClass('highlight ' + team2class(d.name));
          tooltip.show(d.rankings[d.rankings.length-1]);
        })
        .on('mouseout', function(d) {
          $('.chart').removeClass('highlight ' + team2class(d.name));
          tooltip.hide(d);
        })
        .attr('r', '4')
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
        .on('mouseenter', function(d) {
          $('.chart').addClass('highlight ' + team2class(d.name));
        })
        .on('mouseout', function(d) {
          $('.chart').removeClass('highlight ' + team2class(d.name));
        })
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
