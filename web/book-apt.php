function book_appt() {
var $ = jQuery;
var name = $('#name').val();
var email_address = $('#email_address').val();
var phone = $('#phone').val();
var zip = $('#zip').val();
var service = $('#service').val();
var time = $('#time').val();
time = time.replace("/", "-");
time = time.replace("/", "-");
time = time.replace("/", "-");
var data = { "name":name, "email_address":email_address, "phone":phone, "zip":zip, "service":service, "time":time };
$.ajax({"url":"book_appt.php",
"type":"post",
"data": data,
success: function(msg) {
console.log(msg);
$("#sndreq").html("Request Sent! Thank You.");
$("#msg").html("<br/><br/><br/><br/><br/><br/>Your message has been received, we'll call you shortly to confirm your appointment.");

}});
}