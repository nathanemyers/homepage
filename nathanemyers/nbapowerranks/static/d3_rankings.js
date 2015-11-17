function build_chart(selector) {
  var border_left = 120;
  var border_right = 50;
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
    
  var yAxis = d3.svg.axis()
    .ticks(6)
    .orient('right')
    .scale(y);

  // can't have a css class named 76ers
  var team2class = function(team) {
    return (team === '76ers') ? 'philly' : team;
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
      .enter().append('g')
        .attr('class', lineClass);

    var color_lines = team_lines
      .append('path')
        .attr('d', function(d) { return line(d.rankings); });

    var labels = team_lines
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

    var bubbles = team_lines.selectAll('circle')
      .data(function(d) {return d.rankings;})
      .enter().append('circle')
        .attr('cx', function(d) {
          return x(d.week);
        })
        .attr('cy', function(d) {
          return y(d.rank);
        })
        .attr('r', '8')
        .style('fill', 'none');
        

    // This grouping is for all mouse related callbacks, contains a bunch of
    // fat lines and circles layered over the colored display versions.
    // We have to declare this stuff after the colored lines so they'll take
    // precidence in the DOM
    var line_handles = svgContainer.selectAll('.line-handle')
      .data(data)
      .enter().append('g');

    line_handles
      .append('path')
      .attr('d', function(d) { return line(d.rankings); })
      .attr('class', 'line-handle')
      .on('mouseenter', function(d) {
        $('.chart').addClass('highlight ' + team2class(d.name));
      })
      .on('mouseout', function(d) {
        $('.chart').removeClass('highlight ' + team2class(d.name));
      });
        
    line_handles.selectAll('circle')
      .data(function(d) {return d.rankings;})
      .enter().append('circle')
        .attr('cx', function(d) {
          return x(d.week);
        })
        .attr('cy', function(d) {
          return y(d.rank);
        })
        .attr('r', '6')
        .style('fill', 'red')
        .style('opacity', '0')
        .on('mouseenter', function(d) {
          var name = d3.select(this.parentNode).datum().name;
          $('.chart').addClass('highlight ' + team2class(name));
          tooltip.show(d);
        })
        .on('mouseout', function(d) {
          var name = d3.select(this.parentNode).datum().name;
          $('.chart').removeClass('highlight ' + team2class(name));
          tooltip.hide();
        });

    svgContainer.append('g')
      .attr('class', 'axis')
      // -12 for 12px border
      .attr('transform', 'translate(0,' + ( height - (border_bottom - 12) ) + ')')
      .call(xAxis);

      svgContainer.append('text')
        .attr('x', width / 2)
        .attr('y', height)
        .text('Week');


    yAxisSvg = svgContainer
      .append('g')
        .attr('class', 'axis')
        .attr('transform', 'translate(' + ( width - border_right ) + ',0)')
        .call(yAxis);

    svgContainer.append('text')
      .attr('x', 0 - (height / 2))
      .attr('y', width - 10)
      .attr('transform', 'rotate(-90)')
      .text('Rank');



  });

}
