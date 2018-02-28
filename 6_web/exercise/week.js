var year=Number(window.prompt('年'));
var month=Number(window.prompt('月'));
var day=Number(window.prompt('日'));
totalDay = 0;
for(var i=1900;i<year;i++){
    days = i%4===0&&i%100!==0||i%400===0 ? 366 : days = 365;
    totalDay += days;
}
switch(month-1){
    case 11:totalDay+=30;
    case 10:totalDay+=31;
    case 9:totalDay+=30;
    case 8:totalDay+=31;
    case 7:totalDay+=31;
    case 6:totalDay+=30;
    case 5:totalDay+=31;
    case 4:totalDay+=30;
    case 3:totalDay+=31;
    case 2:year%4===0&&year%100!==0||year%400===0 ? totalDay+=29 :totalDay+=28;
    case 1:totalDay+=31;
    }
totalDay += day-1;
console.log(totalDay);
switch (totalDay%7){
    case 0:console.log('星期1');break;
    case 1:console.log('星期2');break;
    case 2:console.log('星期3');break;
    case 3:console.log('星期4');break;
    case 4:console.log('星期5');break;
    case 5:console.log('星期6');break;
    case 6:console.log('星期7');break;
}