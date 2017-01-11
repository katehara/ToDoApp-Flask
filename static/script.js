$(document).ready(function() {
    $('select').material_select();

    $('.tasks .del').click(function(){
    	f = $(this).parent().parent().prop('className')
    	console.log(f)
    	$.ajax({
	        url: '/rem-task',
	        data: {id : f},
	        type: 'GET'
    	});
    })

    $('.tasks .add').click(function(){
    	f = $('.tasks form div #newTask').val()
    	e = $('#selCat').val()
    	g = $('#selPri').val()
    	$.ajax({
	        url: '/new-task',
	        data: {
	        	d:f,
	        	c:e,
	        	p:g
	        },
	        type: 'GET'
    	});
    })
    
    $('.categories .del').click(function(){
    	f = $(this).parent().parent().prop('className')
    	console.log(f)
    	$.ajax({
	        url: '/rem-category',
	        data: {nm : f},
	        type: 'GET'
    	});
    })

    $('.categories .add').click(function(){
    	f = $('.categories form div #newCat').val()
    	console.log(f)
    	$.ajax({
	        url: '/new-category',
	        data: {nm : f},
	        type: 'GET'
    	});
    })

    $('.priorities .del').click(function(){
    	f = $(this).parent().parent().prop('className')
    	console.log(f)
    	$.ajax({
	        url: '/rem-priority',
	        data: {nm : f},
	        type: 'GET'
    	});
    })

    $('.priorities .add').click(function(){
    	f = $('.priorities form div #addPri').val()
    	console.log(f)
    	$.ajax({
	        url: '/new-priority',
	        data: {nm : f},
	        type: 'GET'
    	});
    })


});