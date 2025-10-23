// ==UserScript==
// @name        nowcoder.com padding output
// @namespace   Violentmonkey Scripts
// @match       *://*nowcoder.com/*
// @grant       none
// @version     1.0
// @author      -
// @description 2024/3/4 22:21:26
// ==/UserScript==

function paddingOutput() {
  for (node of document.querySelectorAll(".output-flex-row")) {
    node.style.paddingBottom = "10px";
  }
  // document.querySelector(".main.terminal-main").style.paddingBottom = "30px";
  document.querySelector(".code-submit-result").style.paddingBottom = "30px";
}

console.log("Violentmonkey nowcoder 1");
$(document).ready(function(){

  console.log("Violentmonkey nowcoder 3");
  waitingInt = setInterval(function() {
    // 循环检测待目标出现
    console.log("Violentmonkey nowcoder 5");
    if($(".self-submit-btn").length >= 1) {
      clearInterval(waitingInt);
      console.log("Violentmonkey nowcoder 6");
      $(".self-submit-btn").click(function(){
        console.log("Violentmonkey nowcoder 7");
        setTimeout(function(){
          console.log("Violentmonkey nowcoder 8");
          paddingOutput();
        }, 3000);
      });
    }
  },3000);

  console.log("Violentmonkey nowcoder 4");
});
console.log("Violentmonkey nowcoder 2");
