package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"math"
)

func pageCount(n int32, p int32) int32 {
	front := float64(p / 2)
	back := float64((n - p) / 2)
	if n % 2 == 0 && p % 2 == 1 && n > p {
		back++
	}
	return int32(math.Min(front, back))
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	pTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	p := int32(pTemp)

	result := pageCount(n, p)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
