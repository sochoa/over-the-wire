<?php


function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';
    for($i=0;$i<strlen($text);$i++) {
      $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}

$default_data = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
$decoded_ciphertext = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D';
echo xor_encrypt($default_data, base64_decode(urldecode($decoded_ciphertext)));
echo "\n";

//'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D' XOR '{"showpassword": "no", "bgcolor: "#ffffff"}' = key
$updated_data = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
echo urlencode(base64_encode(xor_encrypt($updated_data, 'qw8J')));
echo "\n";
?>

