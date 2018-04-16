// 禁止右键
$(document).ready(function(){
    $(document).bind("contextmenu",function(e){
        return false;
    });
});