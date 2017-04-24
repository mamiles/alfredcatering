<?php
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $_REQUEST["date"] = $_REQUEST["time"];
    unset($_REQUEST["time"]);
    $_REQUEST["time"] = null;
    $indexCompleted = array_search( 'arp_scroll_position', $_REQUEST );
    unset( $_REQUEST[$indexCompleted] );
    $str = "<table><tr style = 'background:#ddd;color:#333;'><td colspan='20'><b>New Catering Request Received!</b><br/>Someone filled out catering request form at Alfred's Catering website<br/>Request was made on " .
    date("M D Y h:m", time()) . "</tr><tr><td>" . str_replace("=", "</td><td>", http_build_query($_REQUEST));
    $str = str_replace("&", "</td></tr><tr><td>", $str);
    $str = str_replace("+", " ", $str);
    $str .= "</table>";
    $str = urldecode($str);
    mail("alfred@alfredcatering.com", "+1 Lead Received - Alfred's Catering - From IP = " . $_SERVER["REMOTE_ADDR"], $str, $headers);
    mail("greg.sidelnikov@gmail.com", "+1 Lead Received - Alfred's Catering - From IP = " . $_SERVER["REMOTE_ADDR"], $str, $headers);
?>