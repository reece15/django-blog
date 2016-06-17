(function($){
	
	var opts = {};
	var option={
		url:"/upload/",
		dragleave: fun,
		drop: fun,
		dragenter: fun,
		dragover: fun,
		copy:copys,
		loadpic:loadpic
	};
	
	$.fn.addUpload=function(opt){
		opts = $.extend({}, option, opt);
		$.event.props.push("dataTransfer");
		$(document).bind("dragleave", fileleave).bind("dragenter", fileenter).bind("dragover", fileover).bind("drop", fun);
		return this.each(function(){
			$(this).bind("dragleave", fileleave).bind("dragenter", fileenter).bind("dragover", fileover).bind("drop", drop);
		});
	}
	
	function copys(str){
		if(window.clipboardData && window.clipboardData.setData){
			window.clipboardData.setData('text', str); 

		}
	}
	function fileenter(e){
		e.preventDefault();
		e.stopPropagation();
	}
	function fileleave(e){
		e.preventDefault();
		e.stopPropagation();
	}
	function fileover(e){
		e.preventDefault();
		e.stopPropagation();
	}
	function loadpic(file){
		var filename = file.name;
		var filesize = Math.floor(file.size);
		console.log(filename);
		
		var img = window.URL.createObjectURL(file);
		var $str = $("<div class='photobox' style='background:url("+img+")'><p>name:"+filename+"</p><p>"+"size:"+filesize+"</p></div>");
		$(this).append($str);
		return $str;
	}
	
	function drop(e){
		e.preventDefault();
		var files = e.dataTransfer.files;
		
		if(files != null && files != undefined && files.length != 0){
			$(this).find("span").hide();
			for(var i = 0; i < files.length; i++){
				if(files[i].type.indexOf('image') != -1){
					if(files[i].size > 5000000){
						alert(" file size too big , max size is 5mb");
						break;
					}
					upload(loadpic(files[i]), files[i]);
				}
			}
		}
		
		e.stopPropagation();
	}
	function fun(e){
		e.preventDefault();
		return false;
	}
	function upload(obj, f){
		
		var form = new FormData();
		form.append("photo",f);
		$.ajax({
			type:"post",
			url:opts.url,
			data:form,
			processData:false,  
			contentType:false,
			success:function(data){
				opts.copy(data);
			}
		});
	}
})(jQuery);
