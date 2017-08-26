package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	wordCount := make(map[string]int)
	words := strings.Fields(s)
	for _, word := range words {
		old_count := wordCount[word]
		wordCount[word] = old_count + 1
	}
	return wordCount
}

func main() {
	wc.Test(WordCount)
}