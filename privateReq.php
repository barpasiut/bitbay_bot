<?php
$key = $argv[1];
$secret = $argv[2];
$params_helper = explode(",",$argv[4]);
foreach ($params_helper as $param)
{
	$keyAndValue = explode(":",$param);
	$params[$keyAndValue[0]] = $keyAndValue[1];
}

$params["method"] = $argv[3];
$params["moment"] = time();
//print_r($params);

$post = http_build_query($params, "", "&");
$sign = hash_hmac("sha512", $post, $secret);
$headers = array(
    "API-Key: " . $key,
    "API-Hash: " . $sign,
);
$curl = curl_init();
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_URL, "https://bitbay.net/API/Trading/tradingApi.php");
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_POSTFIELDS, $post);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, 0);
$ret = curl_exec($curl);

print_r($ret)
?>
