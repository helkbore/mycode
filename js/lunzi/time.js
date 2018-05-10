// CST 转 GMT 并格式化
// 时间格式化
// 输入: Wed May 09 14:08:45 CST 2018
// 输出: Wed May 09 2018 14:08:45 GMT+0800
function CST2GMT(time) {
    if ( null == time || '' == time ) {
        return "";
    }

    var dateStr = time.trim().split(" ");
    var strGMT = dateStr[0]+" "+dateStr[1]+" "+dateStr[2]+" "+dateStr[5]+" "+dateStr[3]+" GMT+0800";
    return strGMT;


}

// 输入GMT时间 Wed May 09 2018 14:08:45 GMT+0800 (其他时间应该也可)
// 转换为 2018年5月9日 14:50:27 这种格式
function dataFormat(dateStr) {
    var date = new Date(Date.parse(dateStr));
    var y = date.getFullYear();
    var m = date.getMonth() + 1;
    m = m < 10 ? ('0' + m) : m;
    var d = date.getDate();
    d = d < 10 ? ('0' + d) : d;
    var h = date.getHours();
    var minute = date.getMinutes();
    minute = minute < 10 ? ('0' + minute) : minute;
    var second = date.getSeconds();
    second = second < 10 ? ('0' + second) : second;

    return y + "-" + m + "-" + d + " " + h + ":" + minute + ":" + second;;
}