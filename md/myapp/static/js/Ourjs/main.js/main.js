
function check2(){
	//alert('a'); -> 잘됌
	if(frm.tag.value === ""){
		frm.tag.focus();
		alert('검색창을 까먹었어 너!! 빨리 !!');
		return;
	}if(frm.tag.value !== ""){ //QQQ값이 있다
		//alert('d');// ㅇㅋ
		url="/search/?tag=" + frm.tag.value;
		location.href=url;
	}
}

