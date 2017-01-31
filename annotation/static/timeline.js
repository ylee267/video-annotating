/* ------------------------------------------------------------- *\
 * Script for creating and updating timeline
 *
 * funcions
 * 1) repaintTimelineInitial()
\* ------------------------------------------------------------- */

function timestampDOM(idx, time, type) {
    var type_idx = type + '_' + idx;
    var dom = '<div class="timestamp">'
        + '<input type="hidden" class="timestamp-time" name="' + type_idx + '" value="' + time + '">'
        + '</div>';
    return dom;
}

function repaintTimelineInitial() {
    // called each annotation and create the time line
    var comment_type = '';
    var bar_width = $('.bar').width();
    var video_duration = 5227; // [magic number alert][special alert]

    var node_idx = 0;
    var timestampDOMs = '';
    var time = 0;
    $('tr.annotation').each(function() {
        comment_type = $(this).find('td.comment_type').find('span').html();
        if (comment_type == 'question') {
            time = $(this).find('td.time').find('span.time').html();
            timestampDOMs += timestampDOM(node_idx, time, comment_type);
            node_idx = node_idx + 1;
        }
    });

    $('.bar-container').append( timestampDOMs );

    // style the timeline
    var node_diameter = 14;
    bar_width = parseInt(bar_width) - 14;
    node_idx = 0;
    $('tr.annotation').each(function() {
    	comment_type = $(this).find('td.comment_type').find('span').html();
	if (comment_type == 'question') {
	    time = $(this).find('td.time').find('span.time').html();
	    var pos = parseInt( parseInt(time) / video_duration * bar_width);
	    $('input[name="' + comment_type + '_' + node_idx + '"]')
	        .parent()
	        .css('left', pos + 'px');
    	    node_idx = node_idx + 1;
	}
    });

    // add timestamp action
    $('.timestamp').each(function() {
        $(this).prop('title', $(this).find('input').val() + ' secs');
    });
}

function addTimestamp(type, time) {
    var stamp_nums = 0;
    $('tr.annotation').each(function() {
	comment_type = $(this).find('td.comment_type').find('span').html();
	if (comment_type == type) {
	    stamp_nums = stamp_nums + 1;
	}
    });


    var dom = timestampDOM(stamp_nums, time, type);

    $('.bar-container').append( dom );

    // style
    var bar_width = $('.bar').width();
    var video_duration = 5227; // [magic number alert][special alert]
    var node_diameter = 14;
    bar_width = parseInt(bar_width) - node_diameter;
    var pos = parseInt( parseInt(time) / video_duration * bar_width);
    $('input[name="' + type + '_' + stamp_nums + '"]')
        .parent()
	.css('left', pos + 'px');

    // add timestamp action
    $('input[name="' + type + '_' + stamp_nums + '"]').each(function() {
        $(this).prop('title', $(this).find('input').val() + ' secs');
    });

}
