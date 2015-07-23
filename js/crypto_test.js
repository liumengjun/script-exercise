var a = '18613888646';
name = a.substr(0,3)+'****'+a.substr(a.length-4);
console.log(name);

var privateKey = '-----BEGIN RSA PRIVATE KEY-----\n'
  +'MIICXQIBAAKBgQCpidSSiOVoH/UA5+7ycAl7tuQ9en61kgb6AP5gqAnABZHRFF19\n'
  +'EsheIxJKKiVwg2d46HU50LxTMgeiFigcWtf1yiBBzXaq3ozv2qFZvcWOy3Uwxk1R\n'
  +'r6whHGbpIaWwj497IYETLrNHt52x6Nyk+4PyZwdNFq5s774ZPvc784g5xwIDAQAB\n'
  +'AoGAIMayv/mTUEQNW7V7LoeWbcJ38aLC6Fto2eBjTVBvQh5RiHhFcq606e4h1RC8\n'
  +'2DmvQWK/dwPxxKvBagaajpDJezyDOR0d778cgFenCW8iZ7/g/EABPqHWFUiQ71Yg\n'
  +'+AvsL+SBUhEgaKgSmteiptA2vkp/Hb96YNR/+bBloMzKCkECQQDbz+XvTkXfjaPR\n'
  +'7EF05OrmaPj14OCNXpKKir5JgBmNqj/URY3XuwvzqO180wicemCZEmJIt8NSnP4a\n'
  +'b+Y9vS5RAkEAxXMeju6hbcwwWYpwnk7xWxJbmQf4AIu51hGC1jNydVfhNn9RZz7V\n'
  +'uCvUA/2uQWzttpIwinm/auxd2k76ftFolwJBAJalRe2bFFIg7XwqUbX+SWq92JoS\n'
  +'k3LvtLjUW5NeAqVPX81oGc0W+Rr11EUvEIDFcjyWF9vEbU3KIHAX7pCzffECQEak\n'
  +'4ZISHv/BxqrCtXhuljwXXV5rU3gehebpbP5medUyFAoDk4R1HtI+HCUxZl9SMdrY\n'
  +'gzWIScxftVSeXVFyaxECQQDGGk4JKAw4z6y1ZJZcZ6HOAjfXGAGoyNfQJYZSoOYa\n'
  +'d5zEmFWs4uaBRmoMkeM9S+UC532b41dHAUc6uIFqT2Ye\n'
  +'-----END RSA PRIVATE KEY-----';
var publicKey = '-----BEGIN PUBLIC KEY-----\n'
  +'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpidSSiOVoH/UA5+7ycAl7tuQ9\n'
  +'en61kgb6AP5gqAnABZHRFF19EsheIxJKKiVwg2d46HU50LxTMgeiFigcWtf1yiBB\n'
  +'zXaq3ozv2qFZvcWOy3Uwxk1Rr6whHGbpIaWwj497IYETLrNHt52x6Nyk+4PyZwdN\n'
  +'Fq5s774ZPvc784g5xwIDAQAB\n'
  +'-----END PUBLIC KEY-----';

var crypto = require('crypto');
// var ciphers = crypto.getCiphers();
// var hashes = crypto.getHashes();
// console.log(ciphers);
// console.log(hashes);

// var cipher = crypto.createCipher('RSA', privateKey); // wrong, todo
var cipher = crypto.createCipher('aes-256-ecb', '123');
var encStr = cipher.update(a, 'utf8');
encStr = cipher.final();
console.log(encStr);

// var decipher = crypto.createDecipher('RSA', publicKey); // wrong, todo
var decipher = crypto.createDecipher('aes-256-ecb', '123');
var decStr = decipher.update(encStr).toString('utf8');
decStr = decipher.final().toString();
console.log(decStr);

var sign = crypto.createSign('RSA-SHA1');
sign.update(a);
var mysign = sign.sign(privateKey,'base64');
console.log(mysign);

var verifier = crypto.createVerify('RSA-SHA1');
verifier.update(a);
var verifyResult = verifier.verify(publicKey, mysign, 'base64');
console.log(verifyResult);
