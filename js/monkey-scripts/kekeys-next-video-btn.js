// ==UserScript==
// @name         kekeys-next-video-btn
// @namespace    http://tampermonkey.net/
// @version      2025-12-11
// @description  try to take over the world!
// @author       You
// @match        https://www.kkys05.com/play/*-*-*.html
// @icon         https://www.google.com/s2/favicons?sz=64&domain=kkys05.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    const scriptCode = 'LmjtWboBZ5hUX';
    const floatWindowId = 'floatWindow'+scriptCode;
    const nextVideoBtnId = 'nextVideoBtn'+scriptCode;

    var domStr = '  <button id="'+nextVideoBtnId+'" class="'+nextVideoBtnId+'" style="padding:2px; border:0px; border-radius:5px;">下一集</button>';
    // create element such as '<div id="floatWindow" class="floatWindow" style="display: none;">' + domStr + '</div>'
    var newDiv = document.createElement('div');
    newDiv.id = floatWindowId;
    newDiv.className = floatWindowId;
    newDiv.innerHTML = domStr;
    newDiv.style = 'position: fixed;'+
        'z-index: 99;'+
        'top: 53px;'+
        'right: 0px;';
    document.body.appendChild(newDiv);

    var nextVideoBtn = document.getElementById(nextVideoBtnId);
    nextVideoBtn.onclick = function() {
        var node = document.getElementById('nextEspicodesBtn');
        node.click();
    };
})();
