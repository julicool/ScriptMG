$(".form").form({
    fields: {
        mobname: {identifier: 'mobname', rules:[{type: 'empty'}]},
        mobmodel: {identifier: 'mobmodel', rules:[{type: 'empty'}]},
        mobstat: {identifier: 'mobstat', rules:[{type: 'empty'}]},
        resolution_x: {identifier: 'resolution_x', rules:[{type: 'empty'},{type: 'number', prompt: '必须为数字'}]},
        resolution_y: {identifier: 'resolution_y', rules:[{type: 'empty'},{type: 'number', prompt: '必须为数字'}]},
        system_type: {identifier: 'system_type', rules:[{type: 'empty'}]},
        system_numb: {identifier: 'system_numb', rules:[{type: 'empty'}]}
    }
})

$("#mobname").change(function (){
    var t = $("#mobname option:selected").val();
    if (t==4){
        $("#systype").empty();
        $("#sysnumb").empty();
        $("#systype").append('<option value="1">iOS</option>');
        $("#sysnumb").append('<option value="a">全部</option>\
                              <option value="8">8</option>\
                              <option value="9">9</option>\
                              <option value="10">10</option>\
                              <option value="11">11</option>\
                              <option value="12">12</option>');
    }
    else if (t=="a"){
        $("#systype").empty();
        $("#sysnumb").empty();
        $("#systype").append('<option value="a">全部</option>');
        $("#systype").append('<option value="0">Android</option>');
        $("#systype").append('<option value="1">iOS</option>');
        $("#sysnumb").append('<option value="a">全部</option>\
                              <option value="8">iOS-8</option>\
                              <option value="9">iOS-9</option>\
                              <option value="10">iOS-10</option>\
                              <option value="11">iOS-11</option>\
                              <option value="12">iOS-12</option>\
                              <option value="4.0">And-4.0</option>\
                              <option value="4.1">And-4.1</option>\
                              <option value="4.2">And-4.2</option>\
                              <option value="4.3">And-4.3</option>\
                              <option value="4.4">And-4.4</option>\
                              <option value="5.0">And-5.0</option>\
                              <option value="6.0">And-6.0</option>\
                              <option value="7.0">And-7.0</option>\
                              <option value="8.0">And-8.0</option>\
                              <option value="9.0">And-9.0</option>');
    }
    else {
        $("#systype").empty();
        $("#sysnumb").empty();
        $("#systype").append('<option value="0">Android</option>');
        $("#sysnumb").append('<option value="a">全部</option>\
                              <option value="4.0">4.0</option>\
                              <option value="4.1">4.1</option>\
                              <option value="4.2">4.2</option>\
                              <option value="4.3">4.3</option>\
                              <option value="4.4">4.4</option>\
                              <option value="5.0">5.0</option>\
                              <option value="6.0">6.0</option>\
                              <option value="7.0">7.0</option>\
                              <option value="8.0">8.0</option>\
                              <option value="9.0">9.0</option>');
    }
})

$("#systype").change(function (){
    var t = $("#systype option:selected").val()
    if (t==1){
        $("#sysnumb").empty();
        $("#sysnumb").append('<option value="a">全部</option>\
                              <option value="8">8</option>\
                              <option value="9">9</option>\
                              <option value="10">10</option>\
                              <option value="11">11</option>\
                              <option value="12">12</option>');
    }
    else if (t==0){
        $("#sysnumb").empty();
        $("#sysnumb").append('<option value="a">全部</option>\
                                <option value="4.0">4.0</option>\
                                <option value="4.1">4.1</option>\
                                <option value="4.2">4.2</option>\
                                <option value="4.3">4.3</option>\
                                <option value="4.4">4.4</option>\
                                <option value="5.0">5.0</option>\
                                <option value="6.0">6.0</option>\
                                <option value="7.0">7.0</option>\
                                <option value="8.0">8.0</option>\
                                <option value="9.0">9.0</option>');
    }
    else {
        $("#sysnumb").empty();
        $("#sysnumb").append('<option value="a">全部</option>\
                                    <option value="8">iOS-8</option>\
                                    <option value="9">iOS-9</option>\
                                    <option value="10">iOS-10</option>\
                                    <option value="11">iOS-11</option>\
                                    <option value="12">iOS-12</option>\
                                    <option value="4.0">And-4.0</option>\
                                    <option value="4.1">And-4.1</option>\
                                    <option value="4.2">And-4.2</option>\
                                    <option value="4.3">And-4.3</option>\
                                    <option value="4.4">And-4.4</option>\
                                    <option value="5.0">And-5.0</option>\
                                    <option value="6.0">And-6.0</option>\
                                    <option value="7.0">And-7.0</option>\
                                    <option value="8.0">And-8.0</option>\
                                    <option value="9.0">And-9.0</option>');
    }
})

$("#addmob").change(function cho_iphone(){
    var t = $("#addmob option:selected").val()
    if (t==4){
        $("#system_type").empty();
        $("#system_numb").empty();
        $("#system_type").append('<option value="1">iOS</option>');
        $("#system_numb").append('<option value="8">8</option>\
                                  <option value="9">9</option>\
                                  <option value="10">10</option>\
                                  <option value="11">11</option>\
                                  <option value="12" selected="selected">12</option>');
    }
    else {
        $("#system_type").empty();
        $("#system_numb").empty();
        $("#system_type").append('<option value="0">Android</option>');
        $("#system_numb").append('<option value="4.0">4.0</option>\
                                  <option value="4.1">4.1</option>\
                                  <option value="4.2">4.2</option>\
                                  <option value="4.3">4.3</option>\
                                  <option value="4.4">4.4</option>\
                                  <option value="5.0">5.0</option>\
                                  <option value="6.0">6.0</option>\
                                  <option value="7.0">7.0</option>\
                                  <option value="8.0" selected="selected">8.0</option>\
                                  <option value="9.0">9.0</option>');
    }
})

$("#edits_mobname").change(function cho_iphone(){
    var t = $("#edits option:selected").val()
    if (t==4){
        $("#edits_system_type").empty();
        $("#edits_system_numb").empty();
        $("#edits_system_type").append('<option value="1">iOS</option>');
        $("#edits_system_numb").append('<option value="8">8</option>\
                                    <option value="9">9</option>\
                                    <option value="10">10</option>\
                                    <option value="11">11</option>\
                                    <option value="12" selected="selected">12</option>');
    }
    else {
        $("#edits_system_type").empty();
        $("#edits_system_numb").empty();
        $("#edits_system_type").append('<option value="0">Android</option>');
        $("#edits_system_numb").append('<option value="4.0">4.0</option>\
                                <option value="4.1">4.1</option>\
                                <option value="4.2">4.2</option>\
                                <option value="4.3">4.3</option>\
                                <option value="4.4">4.4</option>\
                                <option value="5.0">5.0</option>\
                                <option value="6.0">6.0</option>\
                                <option value="7.0">7.0</option>\
                                <option value="8.0" selected="selected">8.0</option>\
                                <option value="9.0">9.0</option>');
    }
})


function imgshow(btn){
    var id = $(btn).parent().prev().text()
    $("#imgs img").attr("src", oss_host+id+".jpg?x-oss-process=image/resize,h_500");
    $("#imgs").dimmer("show");
}

function upshow(btn){
    var id = $(btn).parent().prevAll().last().text();
    console.log(id);
    $("#mobid").attr("value", id);
    $("#upimg").modal("show");
}

function addshow(){
    $("#adds").modal({autofocus: false,closable: false}).modal("show");
}

function suredel(id){
    x = $(id).parent().prevAll().last().next().next().text();
    y = $(id).parent().prevAll().last().text();
    $("#del_name").text(x);
    $("#del_id").attr("onclick", "delmob(" + y + ")");
    $("#suredel").modal("show");
}

var moblist = {};
function getmoblist(n){
//    $("#mbshow").append('<div class="ui inverted active dimmer"><div class="ui big loader"></div></div>');
    $.ajax({
        type: "post",
        url: "/getmob",
        data: {'start': n},
        dataType: "json",
        success: function(data){
            moblist = data['moblist'];
            show_list(n);
            $("#foot_menu").empty();
            $("#foot_menu").append('<a class="item"><</a>');
            for(i=data['sum_inf']['start'];i<=data['sum_inf']['end'];i++){
                $("#foot_menu").append('<a class="item">' + (i+1) + '</a>');
            }
            $("#foot_menu").append('<a class="item">></a>');
        }
    })
    show_dev();
}

function show_dev(){
    $.ajax({
        url: "/get_mob_list",
        type: "post",
        data: "",
        dataType: "json",
        success: function(data){
            $.each(data['dev_list'], function(i, v){
                var opt1 = document.createElement('option');
                var opt2 = document.createElement('option');
                opt1.innerHTML = v['deploy_name'];
                opt2.innerHTML = v['deploy_name'];
                $("#mobname").append(opt1);
                $("#mobname option:last").attr("value", v['id']);
                $("#addmob").append(opt2);
                $("#addmob option:last").attr("value", v['id']);
            })
        }
    })
}

function show_list(n){
    $("#mbshow").empty();
    $.each(moblist[n], function(i, v){
        <!--列表赋值-->
        var tr = document.createElement('tr');
        var img = document.createElement('td');
        var mobname = document.createElement('td');
        var mobstat = document.createElement('td');
        var resolution = document.createElement('td');
        var system_type = document.createElement('td');
        var system_numb = document.createElement('td');
        var bott = document.createElement('td');
        var id = "<td style='display:none;'>" + v['id'] + "</td>";
        img.innerHTML = '<img class="ui mini image" src="' + v['imgurl'] + '" onclick="imgshow(this)">';
        mobname.innerHTML = v['mobname__deploy_name'] + " " + v['mobmodel'];
        if (v['mobstat']==0){
            mobstat.innerHTML = "可用";
        }
        else if(v['mobstat']==1){
            mobstat.innerHTML = "不可用";
        }
        resolution.innerHTML = v['resolution'];
        if (v['system_type']==0){
            system_type.innerHTML = "Android";
        }
        else if (v['system_type']==1){
            system_type.innerHTML = "iOS";
        }
        system_numb.innerHTML = v['system_numb'];
        bott.innerHTML = '<div class="ui blue button" onclick="upshow(this)">图片上传</div><div class="ui green button" onclick="editmob_1(this)">编辑</div><div class="ui red button" onclick="suredel(this)">删除</div>';
        $("#mbshow").append(tr);
        $("#mbshow tr:last-child").append(id, img, mobname, system_type, system_numb, resolution, mobstat, bott);
    })
}


function delmob(id){
    var y = {}
    y.id = id;
     $.ajax({
        type: "post",
        url: "/delmob",
        data: y,
        dataType: "json",
        success:function (data){
            if (data['resultCode']==0){
                self.location.href="/mobman";
            }
        }
    })
}

function editmob_1(btn){
    var id = $(btn).parent().prevAll().last().text();
    var dev_id = 0;
    $("#edits_id").attr("value", id);
    $.ajax({
        type: "get",
        url: "/getmob" + "?w=" + id,
        dataType: "json",
        success: function(data){
            data = data[0];
            dev_id = data['mobname_id'];
            $("#edits_mobmodel").attr("value", data['mobmodel']);
            $("#edits_mobstat").empty();
            if (data['mobstat']==0){
                $("#edits_mobstat").append('<option value="0" selected="selected">可用</option><option value="1">不可用</option>');
            }
            else if(data['mobstat']==1){$("#edits_mobstat").append('<option value="0">可用</option><option value="1" selected="selected">不可用</option>');}
            $("#edits_mobstat").children("[value=" + data['mobstat'] + "]").attr("selected", "selected");
            var resolution = data['resolution'].split("*");
            $("#edits_x").attr("value", resolution[0]);
            $("#edits_y").attr("value", resolution[1]);
            editmob_2(data['system_numb'], dev_id);
            console.log("xxxx");
            $("#edits").modal({autofocus: false,closable: false}).modal("show");
        }
    })
}

function editmob_2(edits_system_numb, dev_id){
    $.ajax({
        type: "post",
        url: "/get_mob_list",
        data: "",
        dataType: "json",
        success: function(data){
            $("#edits_mobname").empty();
            $.each(data['dev_list'], function(i, v){
                var opt3 = document.createElement('option');
                opt3.innerHTML = v['deploy_name'];
                $("#edits_mobname").append(opt3);
                $("#edits_mobname option:last").attr("value", v['id']);
                if (v['id']==dev_id && dev_id==4){
                    $("#edits_mobname option:last").attr("selected", true);
                    $("#edits_system_type").empty();
                    $("#edits_system_numb").empty();
                    $("#edits_system_type").append('<option value="1">iOS</option>');
                    $("#edits_system_numb").append('<option value="8">8</option>\
                                                    <option value="9">9</option>\
                                                    <option value="10">10</option>\
                                                    <option value="11">11</option>\
                                                    <option value="12">12</option>');
                    $("#edits_system_numb").children("option[value='"+edits_system_numb+"']").attr("selected", true);
                }
                else if (v['id']==dev_id &&dev_id!=4){
                    $("#edits_mobname option:last").attr("selected", true);
                    $("#edits_system_type").empty();
                    $("#edits_system_numb").empty();
                    $("#edits_system_type").append('<option value="0">Android</option>');
                    $("#edits_system_numb").append('<option value="4.0">4.0</option>\
                                                    <option value="4.1">4.1</option>\
                                                    <option value="4.2">4.2</option>\
                                                    <option value="4.3">4.3</option>\
                                                    <option value="4.4">4.4</option>\
                                                    <option value="5.0">5.0</option>\
                                                    <option value="6.0">6.0</option>\
                                                    <option value="7.0">7.0</option>\
                                                    <option value="8.0">8.0</option>\
                                                    <option value="9.0">9.0</option>');
                    $("#edits_system_numb").children("option[value='"+edits_system_numb+"']").attr("selected", true);
                }
            })
        }
    })
}

$("#foot_menu").on("click", ".item", function(){
    var n = $(this).text();
    if(n=="<"){
        var m = Number($(this).next().text())-5;
        if(m>0){
            getmoblist(m-1);
        }
    }
    else if(n==">"){
        var m = Number($(this).prev().text())+1;
        if(((m-1)%5)==0){
            getmoblist(m-1);
        }
    }
    else {
        show_list(n-1);
    }
})