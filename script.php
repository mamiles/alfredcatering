jQuery( document ).ready(function() {
jQuery("#owl-demo").owlCarousel({
navigation : true, // Show next and prev buttons
slideSpeed : 15000,
paginationSpeed : 1500,
singleItem:true,
items : 1,
autoPlay : 10000,
});

var	menuRight = document.getElementById( 'cbp-spmenu-s2' ),
showRightPush = document.getElementById( 'showRightPush' ),
body = document.body;


showRightPush.onclick = function() {
classie.toggle( this, 'active' );
classie.toggle( body, 'cbp-spmenu-push-toleft' );
classie.toggle( menuRight, 'cbp-spmenu-open' );
disableOther( 'showRightPush' );
};



function disableOther( button ) {
if( button !== 'showRightPush' ) {
classie.toggle( showRightPush, 'disabled' );
}
}

jQuery("#close").click(function(){
jQuery("body").removeClass("cbp-spmenu-push-toleft");
jQuery("#cbp-spmenu-s2").removeClass("cbp-spmenu-open");
});


var $document = jQuery(document),
$element = jQuery('#top-100'),
className = 'scroll';

$document.scroll(function() {
if ($document.scrollTop() >= 50) {
// user scrolled 50 pixels or more;
// do stuff
$element.addClass(className);
} else {
$element.removeClass(className);
}
});
});