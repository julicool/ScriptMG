
var moblist = {};
function getmoblist(n){
//    $("#mbshow").append('<div class="ui inverted active dimmer"><div class="ui big loader"></div></div>');
    $.ajax({
        type: "post",
        url: "/exprmob",
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
}

function show_list(n){
    $("#mbshow").empty();
    console.log(moblist);
    if(moblist[0]==null){
        tr = '<tr style="height:100px"><td colspan="5"><h4 class="ui centered header">暂时没有设备需要归还</h4></td></tr>';
        $("#mbshow").append(tr);
    }
    else{
    $.each(moblist[n], function(i, v){
        <!--列表赋值-->
        var tr = document.createElement('tr');
        var mobname = document.createElement('td');
        var username = document.createElement('td');
        var frist_time = document.createElement('td');
        var last_time = document.createElement('td');
        var bott = document.createElement('td');
        var id = "<td style='display:none;'>" + v['id'] + "</td>";
        mobname.innerHTML = v['mobname__deploy_name'] + " " + v['mobmodel'];
        username.innerHTML = v['username']
        frist_time.innerHTML = v['frist_time']
        last_time.innerHTML = v['last_time']
        if(v['urgent']==1){bott.innerHTML = '<div class="ui red button" onclick="sureret(this)">确认归还</div>';}
        else if(v['urgent']==0){bott.innerHTML = '<div class="ui green button" onclick="sureret(this)">确认归还</div>';}
        $("#mbshow").append(tr);
        $("#mbshow tr:last-child").append(id, mobname, username, frist_time, last_time, bott);
    })
}}



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


function sureret(id){
    x = $(id).parent().prevAll().last().next().text();
    y = $(id).parent().prevAll().last().text();
    $("#ret_name").text(x);
    $("#ret_id").attr("onclick", "retmob(" + y + ")");
    $("#sureret").modal("show");
}

function retmob(id){
    var y = {}
    y.id = id;
    $.ajax({
        type: "post",
        url: "/returnmob",
        data: y,
        dataType: "json",
        success:function (data){
            if (data['resultCode']==0){
                self.location.href="/mobche";
            }
            else if (data['resultCode']==1){
                alert(data['resultMess']);
            }
        }
    })
}
