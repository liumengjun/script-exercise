// ==UserScript==
// @name        halihali下一集按钮
// @namespace   Violentmonkey Scripts
// @match       http*://halihali*.com/*/*/*.html
// @grant       none
// @version     1.0
// @author      -
// @description 2025/2/18 12:07:47
// ==/UserScript==
const scriptCode = 'LmjtWboBZ5hUX';
const floatWindowId = 'floatWindow'+scriptCode;
const nextVideoBtnId = 'nextVideoBtn'+scriptCode;

var domStr = '  <button id="'+nextVideoBtnId+'" class="'+nextVideoBtnId+'">下一集</button>';
// create element such as '<div id="floatWindow" class="floatWindow" style="display: none;">' + domStr + '</div>'
var newDiv = document.createElement('div');
newDiv.id = floatWindowId;
newDiv.className = floatWindowId;
newDiv.innerHTML = domStr;
newDiv.style = 'position: fixed;'+
    'z-index: 10;'+
    'top: 100px;'+
    'right: 10px;';
document.body.appendChild(newDiv);

var nextVideoBtn = document.getElementById(nextVideoBtnId);
nextVideoBtn.onclick = function() {
  var url = document.location.href;
  // alert(url);
  var videoNumRe = new RegExp('http?://halihali.*.com/.*/.*/(\\d+)\.html');
  var videoNumMatch = videoNumRe.exec(location.href);
  if (!videoNumMatch) return false;
  var curVideoNum = videoNumMatch[1];
  // alert(curVideoNum);
  var nextVideoNum = 1+parseInt(curVideoNum);
  var nextVideoUrl = url.replace(curVideoNum+'.html', nextVideoNum+'.html');
  // alert(nextVideoUrl);
  location.href = nextVideoUrl;
};
