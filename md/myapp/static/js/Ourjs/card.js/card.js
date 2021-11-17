function prev(){
   //alert("a");
   let link = document.location.href.split("=");
   let no = parseInt(link[1]) - 1;
   console.log(no)
   let newlink = link[0] + "=" + no;
   console.log(newlink)  // +1 된 url
   if(no < 1){
      alert("이전 카드가 없습니다.");
   }else{
      location.href=newlink;
   }   
}

function next(){
   //alert("a");
   let link = document.location.href.split("=");
   let no = parseInt(link[1]) + 1;
   console.log(no)
   let newlink = link[0] + "=" + no;
   console.log(newlink)  // +1 된 url
   if(no > 60){
      alert("다음 카드가 없습니다.");
   }else{
      location.href=newlink;
   }   
}

   
function oklogin(card_code, card_index, username){
        //alert("안녕");
       	//alert(card_code);
		window.open('/oklogin?code=' + card_code + '&idx='+ card_index+ "&uname=" + username, '알림', "width=364, height=200, top=150, left=400, toolbar=no")
       //127.0.0.1/oklogin?idx="3"&uname="abc";
}
    
    function nologin(){
       alert("로그인이 필요한 서비스입니다.");
       // username, card_index -> urls.py -> views.py 저장
}
    


function prev(){
   //alert("a");
   let link = document.location.href.split("=");
   let no = parseInt(link[1]) - 1;
   console.log(no)
   let newlink = link[0] + "=" + no;
   console.log(newlink)  // +1 된 url
   if(no < 1){
      alert("이전 카드가 없습니다.");
   }else{
      location.href=newlink;
   }   
}

function next(){
   //alert("a");
   let link = document.location.href.split("=");
   let no = parseInt(link[1]) + 1;
   console.log(no)
   let newlink = link[0] + "=" + no;
   console.log(newlink)  // +1 된 url
   if(no > 60){
      alert("다음 카드가 없습니다.");
   }else{
      location.href=newlink;
   }   
}

   function writesignup(){

    //document.form.submit();
    //alert("a")
   
   if (writetitle.value == ""){
            alert("제목을 입력해주세요!")
            $("#writetitle").focus()
            return false
         };

    if (writemessage.value == ""){
            alert("후기를 입력해주세요!")
            $("#writemessage").focus()
            return false
         } 
   else
   //window.open('/cardshow?idx='+index)
   alert("후기가 등록되었습니다")
   document.form.submit()
   
   
 
   }

function nowritesignup(){
   alert("로그인이 필요한 서비스입니다.");
}

//후기 내용 글자수 제한
$(document).ready(function() {
    $('#writemessage').on('keyup', function() {
        $('#test_cnt').html("("+$(this).val().length+" / 50)");
 
        if($(this).val().length > 50) {
            $(this).val($(this).val().substring(0, 50));
            $('#test_cnt').html("(50 / 50)");
        }
    });
});
// 제목 내용 글자수 제한
$(document).ready(function() {
    $('#writetitle').on('keyup', function() {
        $('#title_cnt').html("("+$(this).val().length+" / 15)");
 
        if($(this).val().length > 15) {
            $(this).val($(this).val().substring(0, 15));
            $('#title_cnt').html("(15 / 15)");
        }
    });
});
