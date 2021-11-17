function check1(){
	//alert('a');잘됌 
	if(frm1.tag.value === ""){
		alert('검색창이 비어있습니다.'); // 잘됌
		frm1.tag.focus();
		return;
	}if(frm1.tag.value !== ""){
		//alert('b');// ㅇㅋ
		url="search/?tag=" + frm1.tag.value;
		location.href=url;
	}
}