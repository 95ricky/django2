function DelCard(username, card_index){
	//confirm('하이'); 출력잘됌
	if(confirm('정말 삭제 하시겠습니까?')){
		//alert('삭제가 되었습니다') 잘됌
		//alert(username)
		//alert(card_index)
		url="/deleteCard?uname=" + username + "&index=" + card_index
		location.href=url;
	}
	
}

function GoWeb(company){
	//alert(company)
	if(company == '현대'){
      location.href = 'https://www.hyundaicard.com/';
   }else if(company == '국민'){
      location.href = 'https://card.kbcard.com/';
   }else if(company == '삼성'){
      location.href = 'https://www.samsungcard.com/';
   }else if(company == '농협'){
      location.href = 'https://card.nonghyup.com/';
   }else if(company == '우리'){
      location.href = 'https://www.wooricard.com/';
   }else if(company == '신한'){
      location.href = 'https://www.shinhancard.com/';
   }
	
}