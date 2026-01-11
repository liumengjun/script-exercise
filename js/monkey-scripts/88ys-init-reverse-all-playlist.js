// ==UserScript==
// @name         88ys-init-reverse-all-playlist
// @namespace    http://tampermonkey.net/
// @version      2026-01-10
// @description  try to take over the world!
// @author       You
// @match        https://www.88hd.org/vod-play-id-*-src-*-num-*.html
// @icon         https://www.google.com/s2/favicons?sz=64&domain=88hd.org
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    const videoNumRe = new RegExp('/vod-play-id-\\d+-src-(\\d+)-num-(\\d+)\.html');
    const videoNumMatch = videoNumRe.exec(location.pathname);
    if (!videoNumMatch) return false;
    const curSrcNum = parseInt(videoNumMatch[1]);
    // alert(curSrcNum);
    const curVideoNum = parseInt(videoNumMatch[2]);
    // alert(curVideoNum);

    const numRe = new RegExp('\\d+');
    const spanSrcIdRe = new RegExp('vlink_(\\d+)_');

    function markSelectedVideo(event) {
        var srcId = curSrcNum;
        if (event) {
            //console.log(event);
            //console.log(event.target);
            //console.log(event.currentTarget);
            var theSpan = event.currentTarget;
            var idStr = theSpan.id;
            var idMatch = spanSrcIdRe.exec(idStr);
            //console.log(idMatch);
            if (idMatch) {
                srcId = parseInt(idMatch[1]);
            }
        }
        //console.log(srcId);
        var allList = document.querySelectorAll('.playlist > div[id=vlink_'+srcId+'] > ul > li');
        for (var li of allList) {
            var text = li.innerText;
            var numMatch = numRe.exec(text);
            if (!numMatch || curVideoNum != parseInt(numMatch[0])) continue;
            if (srcId == curSrcNum) {
                li.classList.add('selected');
            } else {
                li.children[0].style.color = '#F06000';
            }
        }
    }

    function markSelectedSrc() {
        var srcList = document.querySelectorAll('.playfrom > ul > li');
        for (var i = 0; i < srcList.length; i++) {
            var li = srcList[i];
            if (curSrcNum == i+1) {
                li.style.backgroundColor = '#F06000';
                li.style.color = '#FFFFFF';
            }
        }
    }

    // 监听`span > em` click event, 加在外层的<span>上(冒泡时处理), <em>使用'onclick'会导致 addEventListener 失效
    var allBtnList = document.querySelectorAll('.playlist > div > .jj > span');
    for (let span of allBtnList) {
        span.addEventListener('click', markSelectedVideo);
    }

    // reverse video list
    var rEmBtnList = document.querySelectorAll('.playlist > div > .jj > span[id$=_s1] > em');
    for (let em of rEmBtnList) {
        em.click();
    }

    //markSelectedVideo();
    markSelectedSrc();
})();
