// Boton scroll arriba
$(document).ready( () => {

    $(window).scroll(function(){

        if($(window).scrollTop() > 200){
            $('.scroll-top').css({
                "opacity": "1", "pointer-events":"auto"
            });
        }else{
            $('.scroll-top').css({
                "opacity": "0", "pointer-events":"none"
            });
        }
    });

    $('.scroll-top').click(function(){
        $('html').animate({scrollTop:0}, 500);
    });
});