// スクロールしてカーテン的なやつ
const showElements = document.querySelectorAll(".animation-target");
window.addEventListener("scroll",function(){
    for (let i = 0 ; i < showElements.length; i ++) {
        const getElementDistance = showElements[i].getBoundingClientRect().top + showElements[i].clientHeight * .5;
        if (window.innerHeight > getElementDistance ){
            showElements[i].classList.add("show");
        }
    }
})

// フワッとフェードインするやつ各商品ページ使っているやつ
const targetElement = document.querySelectorAll(".animationTarget");
// console.log(targetElement);
document.addEventListener("scroll",function(){
    for (let i = 0; i < targetElement.length; i++){
        const getElementDistance = targetElement[i].getBoundingClientRect().top + targetElement[i].clientHeight * .3
        // console.log(getElementDistance);
        if(window.innerHeight > getElementDistance){
            targetElement[i].classList.add("fadein");
        }
    }
})

const spTargetElement = document.querySelectorAll(".sp-animationTarget");
// console.log(targetElement);
document.addEventListener("scroll",function(){
    for (let i = 0; i < spTargetElement.length; i++){
        const getElementDistance = spTargetElement[i].getBoundingClientRect().top + spTargetElement[i].clientHeight * .3
        // console.log(getElementDistance);
        if(window.innerHeight > getElementDistance){
          spTargetElement[i].classList.add("slide-bottom");
        }
    }
});



// 2個目のハンバーガー
(function($) {
  var $nav   = $('#navArea');
  var $btn   = $('.toggle_btn');
  var $mask  = $('#mask');
  var open   = 'open'; // class
  // menu open close
  $btn.on( 'click', function() {
    if ( ! $nav.hasClass( open ) ) {
      $nav.addClass( open );
    } else {
      $nav.removeClass( open );
    }
  });
  // mask close
  $mask.on('click', function() {
    $nav.removeClass( open );
  });
} )(jQuery)

// ここらかスワイパー

var galleryThumbs = new Swiper('.gallery-thumbs', {
  spaceBetween: 10,
  slidesPerView: 3,
  freeMode: true,
  watchSlidesVisibility: true,
  watchSlidesProgress: true,
 
});
var galleryTop = new Swiper('.gallery-top', {
  spaceBetween: 10,
  loop: true,
  autoplay: {
    delay: 4000,
    disableOnInteraction: true
  },
  
  thumbs: {
    swiper: galleryThumbs
  }
});



// カート内の増減
var check = false;

function changeVal(el) {
  var qt = parseFloat(el.parent().children(".qt").html());
  var price = parseFloat(el.parent().children(".price").html());
  var eq = price * qt;
  
  el.parent().children(".full-price").html( eq+ "円" );
  
  changeTotal();			
}

function changeTotal() {
  
  var price = 0;
  
  $(".full-price").each(function(index){
    price += parseFloat($(".full-price").eq(index).html());
  });
  
  
  price = Math.round(price * 100) / 100;
  console.log(price)
  var tax = Math.round(price * 0.08);
  var shipping = parseFloat($(".shipping span").html());
  var fullPrice = price + tax + shipping;
  
  if(price == 0) {
    fullPrice = 0;
  }
  
  $(".subtotal span").html(price.toLocaleString());
  $(".tax span").html(tax.toLocaleString());
  $("#total-amount").html("合計 : " + fullPrice.toLocaleString() + "円");
}

$(document).ready(function(){
  
  $(".sp-remove").click(function(){
    var el = $(this);
    el.parent().parent().addClass("removed");
    window.setTimeout(
      function(){
        el.parent().parent().slideUp(1500, function() { 
          el.parent().parent().remove(); 
          if($(".product").length == 0) {
            if(check) {
              $("#cart").html("<h1>The shop does not function, yet!</h1><p>If you liked my shopping cart, please take a second and heart this Pen on <a href='https://codepen.io/ziga-miklic/pen/xhpob'>CodePen</a>. Thank you!</p>");
            } else {
              $("#cart").html("<h1>No products!</h1>");
            }
          }
          changeTotal(); 
        });
      }, 300);
  });
  
  $(".qt-plus").click(function(){
    $(this).parent().children(".qt").html(parseInt($(this).parent().children(".qt").html()) + 1);
    
    $(this).parent().children(".full-price").addClass("added");
    
    var el = $(this);
    window.setTimeout(function(){el.parent().children(".full-price").removeClass("added"); changeVal(el);}, 150);
  });
  
  $(".qt-minus").click(function(){
    
    child = $(this).parent().children(".qt");
    
    if(parseInt(child.html()) > 1) {
      child.html(parseInt(child.html()) - 1);
    }
    
    $(this).parent().children(".full-price").addClass("minused");
    
    var el = $(this);
    window.setTimeout(function(){el.parent().children(".full-price").removeClass("minused"); changeVal(el);}, 150);
  });
  
  window.setTimeout(function(){$(".is-open").removeClass("is-open")}, 1200);
  
  $(".btn").click(function(){
    check = true;
    $(".remove").click();
  });
});

window.onload = function(){
  changeTotal();	
  }


  // ここから問い合わせ用
  $(function() {
    // validate
    $("#contact").validate({
        // Set the validation rules
        rules: {
            name: "required",
            email: {
                required: true,
                email: true
            },
            message: "required",
        },
        // Specify the validation error messages
        messages: {
            name: "Please enter your name",
            email: "Please enter a valid email address",
            message: "Please enter a message",
        },
        // submit handler
        submitHandler: function(form) {
          //form.submit();
           $(".message").show();
           $(".message").fadeOut(4500);
        }
    });
  });