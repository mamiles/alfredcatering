<script rel="stylesheet" href = "datepicker.css"></script>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<style>
	#serv td { padding-top: 20px }
    .innerPadding { width: 300px; }
</style>
<table id = "serv">
    <tr>
        <td>Your Full Name</td>
        <td><input class = "innerPadding" placeholder = "First and Last Name" type = "text" name = "name" id = "name" /></td>
    </tr>
    <tr>
        <td>Email Address</td>
        <td><input class = "innerPadding" placeholder = "Email Address" type = "text" name = "email" id = "email_address" /></td>
    </tr>
    <tr>
        <td>Cell Phone</td>
        <td><input class = "innerPadding" placeholder = "Cell Phone #" type = "text" name = "phone" id = "phone" /></td>
    </tr>
    <tr>
        <td>Venue/Location of Event</td>
        <td><input class = "innerPadding" placeholder = "Venue Location / Address" type = "text" name = "venue_address" id = "zip" /></td>
    </tr>
    <tr>
        <td>Select Service Requested &nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td>
            <select style = "border: 2px solid #333; padding: 4px; max-width: 100%; width: 213px;" id = "service">
                <option value = "None selected">-- Select One --</option>
                <option>Corporate</option>
                <option>Weddings</option>
                <option>Birthday</option>
                <option>Social</option>
                <option>Concierge</option>
                <option>Other Event</option>
            </select>
        </td>
    </tr>
    <tr>
        <td>Event Date</td>
        <td style = "vertical-align: top;">

            <input type = "text" name = "date" id = "time">
            <script src = "https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
            <script>
                $(document).ready(function(){
                   $("#time").datepicker();
                });
            </script>
        </td>
    </tr>
    <tr><td style = "height: 50px;"></td></tr>
    <tr>
        <td></td>
        <td>
            <a onclick = "book_appt()" id = "sndreq" class = "" style = "color: white; cursor: pointer;">Send Request</a>
            <div id = "msg" style = "padding-top: 32px;"></div>
        </td>
    </tr>
</table>
