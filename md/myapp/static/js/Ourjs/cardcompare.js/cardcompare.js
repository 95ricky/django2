function send(card_img, card_name, card_type, card_tag, card_af, card_pm, card_benefit1, card_benefit2, card_benefit3, card_detail){
	opener.document.getElementById("card-select1").innerHTML='<img src="/'+card_img+'">';
	opener.document.getElementById("1-4").innerHTML = card_name;	
	opener.document.getElementById("1-5").innerHTML = card_type;
	opener.document.getElementById("1-6").innerHTML = card_tag;
	opener.document.getElementById("1-7").innerHTML = card_af + '원';
	opener.document.getElementById("1-8").innerHTML = card_pm + '원';
	opener.document.getElementById("1-9").innerHTML = card_benefit1 +", "+ card_benefit2 +", "+ card_benefit3;
  	opener.document.getElementById("1-10").innerHTML = card_detail;
    window.close();


}

function send2(card_img, card_name, card_type, card_tag, card_af, card_pm, card_benefit1, card_benefit2, card_benefit3, card_detail){
	
	opener.document.getElementById("card-select2").innerHTML='<img src="/'+card_img+'">';
	opener.document.getElementById("2-4").innerHTML = card_name;	
	opener.document.getElementById("2-5").innerHTML = card_type;
	opener.document.getElementById("2-6").innerHTML = card_tag;
	opener.document.getElementById("2-7").innerHTML = card_af + '원';
	opener.document.getElementById("2-8").innerHTML = card_pm + '원';
	opener.document.getElementById("2-9").innerHTML = card_benefit1 +", "+ card_benefit2 +", "+ card_benefit3;
  	opener.document.getElementById("2-10").innerHTML = card_detail;
	window.close();   
}
