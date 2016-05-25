<?php
// http://www.w3school.com.cn/php/php_ref_array.asp
$aa = array(1231, 2343,"sdfj");
echo join(',', $aa);
echo "\n";
$serialized_aa = serialize($aa);
echo $serialized_aa;
echo "\n";
echo json_encode($aa);
echo "\n";
echo "whether 1231 in the array: ".in_array(1231, $aa);
echo "\n";
$bb = array(24234,2343,'asdsdf');
echo json_encode($bb)."\n";
$cc = array_merge($aa, $bb);
echo json_encode($cc)."\n";
