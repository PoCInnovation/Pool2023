<?php
include("config.php");

if ( isset($_POST["username"]) && isset($_POST["password"]) ){
   if ($_POST["username"]==$username && $_POST["password"]==$password){
     print("<h2>Welcome back !</h2>");
     print("To validate the challenge use this password<br/><br/>");
   } else {
     print("<h3>Error : no such user/password</h2><br />");
   }
} else {
?>

<form action="" method="post">
 Login&nbsp;<br/>
 <input type="text" name="username" /><br/><br/>
 Password&nbsp;<br/>
 <input type="password" name="password" /><br/><br/>
 <br/><br/>
 <input type="submit" value="connect" /><br/><br/>
</form>

<?php } ?>