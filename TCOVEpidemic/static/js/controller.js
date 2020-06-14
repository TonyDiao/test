function gettime() {
	$.ajax({
		url: '/time',
		type: "get",
		success: function(data) {
			$('#time').html(data)
		},
		error: function() {

		}

	});
}

function get_c1_data() {
	$.ajax({
		url: '/center1',
		type: "get",
		success: function(data) {
			$('.num h1').eq(0).text(data.confirm);
			$('.num h1').eq(1).text(data.suspect);
			$('.num h1').eq(2).text(data.heal);
			$('.num h1').eq(3).text(data.dead);
		},
		error: function() {

		}

	});
}

function get_c2_data() {
    $.ajax({
        url: "/center2",
        success: function (data) {
            ec_center.hideLoading();
            ec_center_option.series[0].data=data.data
            ec_center.setOption(ec_center_option);
        }
    })
}
function get_l1_data() {
    $.ajax({
        url: "/left1",
        success: function (data) {
	    ec_left1.hideLoading();
            ec_left1_Option.xAxis[0].data=data.day;
            ec_left1_Option.series[0].data=data.confirm;
            ec_left1_Option.series[1].data=data.suspect;
            ec_left1_Option.series[2].data=data.heal;
            ec_left1_Option.series[3].data=data.dead;
            ec_left1.setOption(ec_left1_Option);
        }
    })
}

function get_l2_data() {
    $.ajax({
        url: "/left2",
        success: function (data) {
	    ec_left2.hideLoading();
            ec_left2_Option.xAxis[0].data=data.day;
            ec_left2_Option.series[0].data=data.confirm_add;
            ec_left2_Option.series[1].data=data.suspect_add;
            ec_left2.setOption(ec_left2_Option);
        }
    })
}

function get_r1_data() {
    $.ajax({
        url: "/right1",
        success: function (data) {
	    ec_right1.hideLoading();
            ec_right1_option.xAxis.data=data.city;
            ec_right1_option.series[0].data=data.confirm;
            ec_right1.setOption(ec_right1_option);
        }
    })
}

function get_r2_data() {
    $.ajax({
        url: "/right2",
        success: function (data) {
	    ec_right2.hideLoading();
            ec_right2_option.series[0].data=data.kws;
            ec_right2.setOption(ec_right2_option);
        }
    })
}


gettime();
get_c1_data();
get_c2_data();
get_l1_data();
get_l2_data();
get_r1_data();
get_r2_data();
//setInterval(gettime, 1000)
//  setInterval(get_c1_data,1000)