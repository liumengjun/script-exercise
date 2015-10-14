function generateRandWords(len) {　　
  var $chars = ' qwert yuiop asdfg hjkl zxcvbnm '; // qwert键盘按键顺序
  var maxPos = $chars.length;　　
  var str = '';　　
  for (i = 0; i < len; i++) {　　　　
    str += $chars.charAt(Math.floor(Math.random() * maxPos));　　
  }　　
  return str;
}

for (i=0;i<100;i++) {
  console.log(generateRandWords(i));
}
