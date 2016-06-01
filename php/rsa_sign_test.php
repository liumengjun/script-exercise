<?php

$content = 'api_id=aotuapi_version=1partner=aotuuid=00011';
$pri_str = file_get_contents('/Users/liumengjun/.ssh/mala_kuailexue_pri_key.pem');
$pub_str = file_get_contents('/Users/liumengjun/.ssh/mala_to_kuailexue.pub');
var_dump($pub_str);

echo("\n");
echo(md5($content));
echo("\n");

// 默认hash算法是SHA1，此处改为MD5
$prikey = openssl_pkey_get_private($pri_str);
if (openssl_sign($content, $out, $prikey, OPENSSL_ALGO_MD5))
$sig = base64_encode($out);
echo("\n");
echo($sig);
echo("\n");

$sig_bytes = base64_decode($sig);
$pubkey = openssl_pkey_get_public($pub_str);
$verify_result = openssl_verify($content, $sig_bytes, $pubkey, OPENSSL_ALGO_MD5);
echo("\n");
echo("verify_result: $verify_result");
echo("\n");
